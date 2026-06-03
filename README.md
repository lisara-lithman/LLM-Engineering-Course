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

## Prerequisites

- Python 3.8+
- OpenAI API key — [get one here](https://platform.openai.com/api-keys)
- Jupyter Notebook or JupyterLab
