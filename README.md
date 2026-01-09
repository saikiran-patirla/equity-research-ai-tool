# 📈 AI-Powered Equity Research Tool

**Real-time financial news analysis and investment insights using Large Language Models**

An intelligent equity research assistant that fetches live financial news, processes it using NLP, and generates structured investment analysis using state-of-the-art LLMs.
Built for **speed, reliability, and explainability**, with automatic LLM failover.

---

## 🚀 Live Demo

👉 **[Try the Live App](#)** *(Streamlit)*

---

## ✨ Key Features

### 📰 Real-Time Financial News

* Fetches latest articles from **80,000+ global sources** via NewsAPI
* Configurable date range and article limits
* Company name or ticker-based search

### 🤖 AI-Driven Investment Analysis

* **Sentiment classification** (Bullish / Neutral / Bearish)
* **Key insights** distilled from multiple articles
* **Growth catalysts** and **risk factors**
* Clear **Buy / Hold / Sell** recommendation with reasoning

### 💬 Interactive Q&A (RAG)

* Ask follow-up questions grounded in retrieved news
* Context-aware responses using TF-IDF retrieval
* Conversation history preserved per session

### ⚡ Multi-LLM Routing with Failover

* **Groq (Llama-3.1)** as primary for ultra-fast inference
* **OpenAI GPT-3.5** as automatic backup
* Local keyword-based fallback for guaranteed responses

---

## 🧠 How It Works (High Level)

1. **Fetch** – Pulls real-time financial news from NewsAPI
2. **Process** – Cleans and normalizes article text using NLP
3. **Index** – Builds a TF-IDF vector index for semantic retrieval
4. **Analyze** – Generates structured investment insights via LLMs
5. **Ask** – Enables RAG-based Q&A on top of retrieved context

---

## 🏗 System Architecture

```
User
  │
  ▼
Streamlit UI
  │
  ▼
app.py (Controller)
  │
  ├── News Fetcher (NewsAPI)
  ├── Text Processor (NLP Cleaning)
  ├── Vector Store (TF-IDF Similarity)
  └── LLM Router
        ├── Groq (Primary)
        ├── OpenAI (Backup)
        └── Local Fallback
```

---

## 📁 Project Structure

```
equity-research-ai-tool/
│
├── app.py                  # Main Streamlit application
├── src/
│   ├── news_fetcher.py     # NewsAPI integration
│   ├── text_processor.py   # NLP cleaning & normalization
│   ├── vector_store.py     # TF-IDF indexing & retrieval
│   ├── summarizer.py       # Investment analysis & Q&A
│   └── llm_router.py       # Multi-LLM routing & failover
│
├── .streamlit/
│   └── config.toml         # Streamlit theming
├── requirements.txt
├── .env.example
├── LICENSE
└── README.md
```

---

## 🛠 Tech Stack

| Category    | Technology            | Purpose             |
| ----------- | --------------------- | ------------------- |
| Frontend    | Streamlit             | Interactive UI      |
| Language    | Python 3.9+           | Core application    |
| Primary LLM | Groq (Llama-3.1)      | Fast inference      |
| Backup LLM  | OpenAI GPT-3.5        | Reliability         |
| Search      | TF-IDF (scikit-learn) | Document similarity |
| NLP         | NLTK, BeautifulSoup   | Text processing     |
| News        | NewsAPI               | Real-time articles  |

---

## 📦 Installation

### Prerequisites

* Python **3.9+**
* `pip`
* API keys (see below)

### Quick Start

```bash
git clone https://github.com/saikiran-patirla/equity-research-ai-tool.git
cd equity-research-ai-tool

python -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

pip install -r requirements.txt

cp .env.example .env
streamlit run app.py
```

App runs at: **[http://localhost:8501](http://localhost:8501)**

---

## 🔑 API Configuration

Create a `.env` file:

```env
NEWS_API_KEY=your_newsapi_key
GROQ_API_KEY=your_groq_key
OPENAI_API_KEY=your_openai_key   # optional
```

| API     | Required      | Notes           |
| ------- | ------------- | --------------- |
| NewsAPI | ✅             | Required        |
| Groq    | ⭐ Recommended | Fast, free tier |
| OpenAI  | Optional      | Backup LLM      |

---

## ⚡ Performance

| Stage                | Time       |
| -------------------- | ---------- |
| News Fetch           | ~1–2s      |
| Text Processing      | ~0.5s      |
| AI Analysis (Groq)   | ~1–3s      |
| AI Analysis (OpenAI) | ~3–5s      |
| **Total**            | **~5–10s** |

---

## 🔄 LLM Failover Strategy

```
Groq (Primary) → OpenAI (Backup) → Local Fallback
```

* Automatic provider switching
* Quota & error detection
* Active model shown in UI

---

## ⚠️ Disclaimer

This project is **for educational purposes only**.

* Not financial advice
* AI outputs may be incorrect
* Always consult a qualified financial advisor

---

## 👨‍💻 Author

**Sai Kiran Patirla**

* GitHub: [https://github.com/saikiran-patirla](https://github.com/saikiran-patirla)
* LinkedIn: [https://linkedin.com/in/saikiran-patirla](https://linkedin.com/in/saikiran-patirla)

⭐ If you find this useful, consider starring the repository.
