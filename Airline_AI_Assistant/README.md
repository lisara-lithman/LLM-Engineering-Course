# ✈️ FlightAI — Airline AI Assistant

A multimodal AI chatbot for a fictional airline called **FlightAI**, built with the OpenAI API and Gradio. Ask about ticket prices and get a spoken response alongside a DALL-E generated destination image.

---

## Features

- 💬 **Conversational Chat** — Powered by `gpt-4.1-mini` with a short, courteous airline assistant persona
- 🔧 **Tool Calling** — Queries a local SQLite database for real ticket prices
- 🎨 **Image Generation** — Uses DALL-E 3 to generate a pop-art city image when a destination is mentioned
- 🔊 **Text-to-Speech** — Reads out assistant replies using `gpt-4o-mini-tts` (Onyx voice)
- 🖥️ **Gradio UI** — Side-by-side chat + image panel with audio playback below

---

## Project Structure

```
Airline_AI_Assistant/
├── airline_ai_assistant.py   # Main app — chat, tools, image gen, TTS, Gradio UI
├── database.py               # SQLite DB setup and ticket price seeder
├── prices.db                 # SQLite database (auto-created on first run)
└── README.md                 # You are here
```

---

## Seeded Destinations

| City   | Return Ticket Price |
|--------|-------------------|
| London | $799.00           |
| Paris  | $899.00           |
| Tokyo  | $1,420.00         |
| Sydney | $2,999.00         |

> Prices are seeded into `prices.db` automatically when `database.py` is imported.

---

## Setup

### 1. Install dependencies

```bash
pip install openai python-dotenv gradio pillow
```

### 2. Configure your API key

Create a `.env` file in this folder:

```
OPENAI_API_KEY=sk-proj-...
```

### 3. Run the app

```bash
python airline_ai_assistant.py
```

The Gradio UI will open automatically in your browser at `http://localhost:7860`.

**Login credentials:** `ed` / `bananas`

---

## How It Works

1. The user types a message in the Gradio textbox
2. The message is added to the chat history and sent to `gpt-4.1-mini`
3. If the model calls the `get_ticket_price` tool, the app queries `prices.db` and feeds the result back
4. The final reply is:
   - Displayed in the chatbot
   - Spoken aloud via TTS (`speech.mp3`)
   - Accompanied by a DALL-E 3 destination image (if a city was mentioned)

---

## Models Used

| Purpose | Model |
|---------|-------|
| Chat + tool calling | `gpt-4.1-mini` |
| Image generation | `dall-e-3` |
| Text-to-speech | `gpt-4o-mini-tts` |

---

## Notes

- `speech.mp3` is saved to whichever directory the script is run from
- To add more destinations, call `set_ticket_price(city, price)` from `database.py`
- Auth credentials (`ed` / `bananas`) are hardcoded — move them to `.env` for production use
