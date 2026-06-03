# Company Brochure Generator

An AI-powered tool that scrapes a company's website and uses an LLM to generate a professional company brochure in Markdown. Includes a French translation and a Gradio web UI.

---

## File Structure

```
Company-Brochure/
├── llm-company-brochure.ipynb   # Main notebook
├── scraper.py                   # Web scraping utilities
└── README.md
```

---

## How It Works

1. Scrapes all links from the company's landing page
2. Uses GPT to filter only relevant links (About, Careers, Enterprise, etc.)
3. Fetches and cleans the content from those pages
4. Generates a structured Markdown brochure using GPT-4.1-mini
5. Translates the brochure into French using a second GPT call
6. Launches two Gradio UIs — one for English output, one for French

---

## Setup

**1. Install dependencies**
```bash
pip install openai python-dotenv requests beautifulsoup4 gradio
```

**2. Create a `.env` file in this folder**
```
OPENAI_API_KEY=sk-proj-...
```

**3. Run the notebook**
```bash
jupyter notebook llm-company-brochure.ipynb
```

Run all cells from top to bottom. The Gradio UI will launch automatically — enter any company name and website URL to generate a brochure.

---

## Gradio Web UIs

| Interface | URL | Output |
|-----------|-----|--------|
| English Brochure Generator | `http://127.0.0.1:7862` | English Markdown brochure |
| French Brochure Generator | `http://127.0.0.1:7863` | French Markdown brochure |

Both accept a **Company Name** and **Website URL** as inputs, with built-in examples for HuggingFace, OpenAI, and Google.

---

## Technologies

| Library | Purpose |
|---------|---------|
| `openai` | GPT calls for brochure generation, link filtering, and translation |
| `beautifulsoup4` | HTML parsing and content extraction |
| `requests` | Fetching web pages |
| `gradio` | Web UI |
| `python-dotenv` | Loading API key from `.env` |

---

## Notes

- Page content is truncated to **2,000 characters** per page
- The brochure prompt is truncated to **5,000 characters** before being sent to GPT
- The French translation preserves all Markdown formatting (headings, bullets, bold, etc.)
