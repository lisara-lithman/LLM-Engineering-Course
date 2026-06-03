# LLM Engineering Course Projects

All projects from the Udemy LLM Engineering course, enhanced with personal improvements and customizations.

---

## Projects

### 1. Company Brochure Generator
**Folder:** `Company-Brochure/`

An AI-powered tool that scrapes a company website and generates a professional brochure using an LLM. Also translates the brochure into French with a Gradio web UI for both versions.

**Key Features:**
- Scrapes and filters the most relevant pages from a company website
- Generates a structured Markdown brochure (culture, products, careers)
- Translates the brochure to French
- Gradio web UI for both English and French outputs

**Files:**
| File | Description |
|------|-------------|
| `llm-company-brochure.ipynb` | Main notebook — full pipeline |
| `scraper.py` | Web scraping utilities |

**Setup:**
```bash
pip install openai python-dotenv requests beautifulsoup4 gradio
```

Add a `.env` file inside `Company-Brochure/`:
```
OPENAI_API_KEY=sk-proj-...
```

Then run:
```bash
jupyter notebook llm-company-brochure.ipynb
```

---

### 2. Airline AI Assistant
**Folder:** `Airline_AI_Assistant/`

A multimodal AI chatbot for a fictional airline called **FlightAI**. Combines function calling, image generation, and text-to-speech into a single Gradio app — ask about ticket prices and get a spoken response plus a generated destination image.

**Key Features:**
- Conversational assistant powered by `gpt-4.1-mini` with a short, courteous persona
- Tool calling to query real ticket prices from a SQLite database
- DALL-E 3 image generation for destination cities in a vibrant pop-art style
- Text-to-speech replies using `gpt-4o-mini-tts` (Onyx voice)
- Gradio UI with side-by-side chat + image panel and audio playback

**Files:**
| File | Description |
|------|-------------|
| `airline_ai_assistant.py` | Main app — chat loop, tool handling, image gen, TTS, Gradio UI |
| `database.py` | SQLite DB setup and ticket price seeder |
| `prices.db` | SQLite database with destination prices |

**Seeded Destinations:**
| City | Return Ticket Price |
|------|-------------------|
| London | $799 |
| Paris | $899 |
| Tokyo | $1,420 |
| Sydney | $2,999 |

**Setup:**
```bash
pip install openai python-dotenv gradio pillow
```

Add a `.env` file inside `Airline_AI_Assistant/`:
```
OPENAI_API_KEY=sk-proj-...
```

Then run:
```bash
python airline_ai_assistant.py
```

The app will open in your browser at `http://localhost:7860` (default credentials: `ed` / `bananas`).

---

## Prerequisites

- Python 3.8+
- OpenAI API key — [get one here](https://platform.openai.com/api-keys)
- Jupyter Notebook or JupyterLab (for Company Brochure)
