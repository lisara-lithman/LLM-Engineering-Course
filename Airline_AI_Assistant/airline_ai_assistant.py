import os
import json
import sqlite3
import base64

from io import BytesIO
from PIL import Image
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr

from database import DB

# -------------------------
# Setup
# -------------------------

load_dotenv(override=True)

openai_api_key = os.getenv("OPENAI_API_KEY")

if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set")

MODEL = "gpt-4.1-mini"
client = OpenAI()

# -------------------------
# System Prompt
# -------------------------

system_message = """
You are a helpful assistant for an Airline called FlightAI.
Give short, courteous answers, no more than 1 sentence.
Always be accurate.
If you don't know the answer, say so.
"""

# -------------------------
# Database Tool
# -------------------------

def get_ticket_price(city):
    with sqlite3.connect(DB) as conn:
        cursor = conn.cursor()

        cursor.execute(
            "SELECT price FROM prices WHERE city = ?",
            (city.lower(),)
        )

        result = cursor.fetchone()

        if result:
            return f"The ticket price to {city.title()} is ${result[0]:.2f}."
        else:
            return f"Sorry, I don't have the ticket price for {city.title()}."


price_function = {
    "name": "get_ticket_price",
    "description": "Get the price of a return ticket to the destination city.",
    "parameters": {
        "type": "object",
        "properties": {
            "destination_city": {
                "type": "string",
                "description": "The city that the customer wants to travel to"
            }
        },
        "required": ["destination_city"],
        "additionalProperties": False
    }
}

tools = [
    {
        "type": "function",
        "function": price_function
    }
]

# -------------------------
# Image Generation
# -------------------------

def artist(city):

    image_response = client.images.generate(
        model="dall-e-3",
        prompt=(
            f"An image representing a vacation in {city}, "
            f"showing tourist attractions and everything unique "
            f"about {city}, in a vibrant pop-art style"
        ),
        size="1024x1024"
    )

    # New SDKs return URL
    image_url = image_response.data[0].url

    return image_url

# -------------------------
# Text To Speech
# -------------------------

def talker(message):

    response = client.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="onyx",
        input=message
    )

    filename = "speech.mp3"

    with open(filename, "wb") as f:
        f.write(response.content)

    return filename

# -------------------------
# Tool Handler
# -------------------------

def handle_tool_calls_and_return_cities(message):

    responses = []
    cities = []

    for tool_call in message.tool_calls:

        if tool_call.function.name == "get_ticket_price":

            arguments = json.loads(
                tool_call.function.arguments
            )

            city = arguments.get("destination_city")

            cities.append(city)

            result = get_ticket_price(city)

            responses.append(
                {
                    "role": "tool",
                    "content": result,
                    "tool_call_id": tool_call.id
                }
            )

    return responses, cities

# -------------------------
# Main Chat Function
# -------------------------

def chat(history):

    messages = [
        {
            "role": "system",
            "content": system_message
        }
    ]

    for item in history:
        messages.append(
            {
                "role": item["role"],
                "content": item["content"]
            }
        )

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=tools
    )

    cities = []
    image = None

    while response.choices[0].finish_reason == "tool_calls":

        assistant_message = response.choices[0].message

        tool_responses, cities = (
            handle_tool_calls_and_return_cities(
                assistant_message
            )
        )

        messages.append(assistant_message)

        messages.extend(tool_responses)

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=tools
        )

    reply = response.choices[0].message.content

    history.append(
        {
            "role": "assistant",
            "content": reply
        }
    )

    voice = talker(reply)

    if cities:
        image = artist(cities[0])

    return history, voice, image

# -------------------------
# Gradio Callback
# -------------------------

def put_message_in_chatbot(message, history):

    return (
        "",
        history + [
            {
                "role": "user",
                "content": message
            }
        ]
    )

# -------------------------
# UI
# -------------------------

with gr.Blocks() as ui:

    with gr.Row():
        chatbot = gr.Chatbot(
            height=500,
            type="messages"
        )

        image_output = gr.Image(
            height=500,
            interactive=False
        )

    with gr.Row():
        audio_output = gr.Audio(
            autoplay=True
        )

    with gr.Row():
        message = gr.Textbox(
            label="Chat with FlightAI"
        )

    message.submit(
        put_message_in_chatbot,
        inputs=[message, chatbot],
        outputs=[message, chatbot]
    ).then(
        chat,
        inputs=chatbot,
        outputs=[
            chatbot,
            audio_output,
            image_output
        ]
    )

ui.launch(
    inbrowser=True,
    auth=("ed", "bananas")
)