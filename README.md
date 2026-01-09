div align="center">

# 📈 AI-Powered Equity Research Tool

### Real-time Financial News Analysis & Investment Insights Powered by AI

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Click_Here-00C7B7?style=for-the-badge)](https://equity-research-ai-tool-by-sai-kiran.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

<p align="center">
  <img src="https://img.shields.io/badge/Groq-Llama_3.1-orange?style=flat-square&logo=meta" alt="Groq">
  <img src="https://img.shields.io/badge/OpenAI-GPT--4-412991?style=flat-square&logo=openai" alt="OpenAI">
  <img src="https://img.shields.io/badge/NewsAPI-Powered-blue?style=flat-square" alt="NewsAPI">
  <img src="https://img.shields.io/badge/TF--IDF-Vector_Search-yellow?style=flat-square" alt="TF-IDF">
</p>

---

**An intelligent equity research assistant that fetches real-time financial news, processes it using NLP, and generates comprehensive investment analysis using state-of-the-art LLMs.**

[Features](#-features) • [Demo](#-live-demo) • [Architecture](#-architecture) • [Installation](#-installation) • [Usage](#-usage) • [Tech Stack](#-tech-stack) • [API Setup](#-api-setup)

---

</div>

## 🎯 What It Does

This tool automates the tedious process of equity research by:

1. **📰 Fetching Real-Time News** - Pulls latest financial articles from 80,000+ sources via NewsAPI
2. **🔧 Processing & Cleaning** - Removes noise, extracts key information using NLP
3. **🧠 Building Knowledge Base** - Creates searchable vector index using TF-IDF
4. **🤖 Generating AI Analysis** - Produces investment insights with sentiment, catalysts, risks & recommendations
5. **💬 Interactive Q&A** - Answer follow-up questions using RAG (Retrieval Augmented Generation)

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🔍 Smart Search
- Search by company name or ticker symbol
- Quick picks for popular stocks
- Configurable date range (1-30 days)
- Adjustable article limit (5-20)

### 🤖 AI-Powered Analysis
- **Sentiment Analysis** - Bullish/Bearish/Neutral
- **Key Findings** - Top 3 insights from news
- **Growth Catalysts** - Positive factors identified
- **Risk Assessment** - Potential concerns highlighted
- **Investment Recommendation** - Buy/Hold/Sell with reasoning

</td>
<td width="50%">

### 💬 Interactive Q&A
- Pre-built quick questions
- Custom question input
- Context-aware responses
- Full conversation history

### 📊 Dashboard Metrics
- Article count analyzed
- Number of unique sources
- Total words processed
- Active AI model indicator

</td>
</tr>
</table>

---

## 🚀 Live Demo

**[👉 Try the Live App Here](https://equity-research-ai-tool-by-sai-kiran.streamlit.app/)**

### Screenshot Preview
╔══════════════════════════════════════════════════════════════════════════════════╗
║ 📈 AI EQUITY RESEARCH TOOL ║
║ Real-time financial news analysis powered by AI ║
╠══════════════════════════════════════════════════════════════════════════════════╣
║ ║
║ 🔍 Enter company name or ticker: ║
║ ┌────────────────────────────────────────────────────┐ ┌────────┐ ┌────────┐ ║
║ │ Apple │ │🚀Analyze│ │❌ Clear│ ║
║ └────────────────────────────────────────────────────┘ └────────┘ └────────┘ ║
║ ║
║ 🔥 Quick picks: ║
║ ┌───────┐ ┌───────┐ ┌─────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌──────┐ ║
║ │ Apple │ │ Tesla │ │Microsoft│ │ NVIDIA │ │ Amazon │ │ Google │ │ Meta │ ║
║ └───────┘ └───────┘ └─────────┘ └────────┘ └────────┘ └────────┘ └──────┘ ║
║ ║
╠══════════════════════════════════════════════════════════════════════════════════╣
║ ║
║ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ║
║ │ 10 │ │ 7 │ │ 3,245 │ │ Groq │ ║
║ │ 📰 Articles │ │ 📡 Sources │ │ 📝 Words │ │ 🤖 Model │ ║
║ └──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘ ║
║ ║
╠══════════════════════════════════════════════════════════════════════════════════╣
║ ║
║ 🤖 AI Investment Analysis ║
║ ╔════════════════════════════════════════════════════════════════════════════╗ ║
║ ║ ║ ║
║ ║ ## APPLE Analysis ║ ║
║ ║ ║ ║
║ ║ ### Sentiment: 🟢 BULLISH ║ ║
║ ║ ║ ║
║ ║ ### Key Points ║ ║
║ ║ • iPhone 16 pre-orders exceed analyst expectations by 15% ║ ║
║ ║ • Services revenue hits all-time high of $24.2B in Q4 ║ ║
║ ║ • Apple Intelligence features driving upgrade cycle momentum ║ ║
║ ║ ║ ║
║ ║ ### Catalysts ║ ║
║ ║ • AI integration across product lineup ║ ║
║ ║ • Strong holiday season outlook ║ ║
║ ║ ║ ║
║ ║ ### Risks ║ ║
║ ║ • China market headwinds persist ║ ║
║ ║ • Regulatory scrutiny in EU markets ║ ║
║ ║ ║ ║
║ ║ ### Recommendation: 📈 BUY ║ ║
║ ║ Strong fundamentals and AI catalyst support continued growth. ║ ║
║ ║ ║ ║
║ ╚════════════════════════════════════════════════════════════════════════════╝ ║
║ ║
╠══════════════════════════════════════════════════════════════════════════════════╣
║ ║
║ 💬 Ask Questions About Apple ║
║ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ║
║ │ 🚀 Growth? │ │ ⚠️ Risks? │ │📊 Analysts? │ │ 🔮 Outlook? │ ║
║ └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘ ║
║ ║
║ ┌──────────────────────────────────────────────────────────┐ ┌──────┐ ║
║ │ Ask anything about Apple... │ │ Ask │ ║
║ └──────────────────────────────────────────────────────────┘ └──────┘ ║
║ ║
║ 📜 Answers (2) ║
║ ┌────────────────────────────────────────────────────────────────────────────┐ ║
║ │ ❓ What are the key growth catalysts and opportunities? │ ║
║ │ ┌────────────────────────────────────────────────────────────────────────┐ │ ║
║ │ │ Apple's key growth catalysts include: 1) AI integration with Apple │ │ ║
║ │ │ Intelligence driving iPhone upgrades, 2) Services hitting record │ │ ║
║ │ │ revenues with 1B+ paid subscribers, 3) Vision Pro opening new AR/VR │ │ ║
║ │ │ market opportunities... │ │ ║
║ │ └────────────────────────────────────────────────────────────────────────┘ │ ║
║ │ 🕐 02:45 PM • Groq │ ║
║ └────────────────────────────────────────────────────────────────────────────┘ ║
║ ║
╠══════════════════════════════════════════════════════════════════════════════════╣
║ ║
║ 📰 News Sources ☐ Show AI summaries ║
║ ┌────────────────────────────────────────────────────────────────────────────┐ ║
║ │ 📄 Apple Reports Record Q4 Services Revenue of $24.2 Billion... [+] │ ║
║ ├────────────────────────────────────────────────────────────────────────────┤ ║
║ │ 📄 iPhone 16 Pre-Orders Surpass Wall Street Expectations... [+] │ ║
║ ├────────────────────────────────────────────────────────────────────────────┤ ║
║ │ 📄 Apple Intelligence: Everything You Need to Know About Apple AI... [+] │ ║
║ └────────────────────────────────────────────────────────────────────────────┘ ║
║ ║
╠══════════════════════════════════════════════════════════════════════════════════╣
║ Built by Sai Kiran Patirla • For educational purposes only ║
╚══════════════════════════════════════════════════════════════════════════════════╝

---

## 🏗 Architecture

### System Overview
┌─────────────────────────────────────────────────────────────────────────────────┐
│ │
│ 👤 USER INTERFACE │
│ ┌─────────────────────┐ │
│ │ Streamlit Frontend │ │
│ │ • Search Bar │ │
│ │ • Quick Picks │ │
│ │ • Results Display │ │
│ │ • Q&A Interface │ │
│ └──────────┬──────────┘ │
│ │ │
│ ▼ │
│ ┌───────────────────────────────────────────────────────────────────────────┐ │
│ │ 📱 app.py (Main Controller) │ │
│ │ • Session State Management • UI Components & Custom CSS │ │
│ │ • Search Flow Orchestration • Q&A Flow Control │ │
│ └───────────────────────────────────────────────────────────────────────────┘ │
│ │ │
│ ┌───────────────────────────┼───────────────────────────┐ │
│ │ │ │ │
│ ▼ ▼ ▼ │
│ ┌───────────────┐ ┌───────────────┐ ┌───────────────┐ │
│ │ 📰 News │ │ 🔧 Text │ │ 🔍 Vector │ │
│ │ Fetcher │ │ Processor │ │ Store │ │
│ ├───────────────┤ ├───────────────┤ ├───────────────┤ │
│ │ • NewsAPI │ │ • HTML Clean │ │ • TF-IDF │ │
│ │ • 80K Sources │ ──▶ │ • Text Norm │ ──▶ │ • Indexing │ │
│ │ • Real-time │ │ • Word Count │ │ • Similarity │ │
│ └───────────────┘ └───────────────┘ └───────────────┘ │
│ │ │
│ ▼ │
│ ┌───────────────────────────────────────────────────────────────────────────┐ │
│ │ 🤖 summarizer.py │ │
│ │ • Investment Analysis Generation • Article Summarization │ │
│ │ • Sentiment Detection • Q&A Response Generation │ │
│ └───────────────────────────────────────┬───────────────────────────────────┘ │
│ │ │
│ ▼ │
│ ┌───────────────────────────────────────────────────────────────────────────┐ │
│ │ 🔄 llm_router.py │ │
│ │ │ │
│ │ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ │ │
│ │ │ 🚀 GROQ │ │ 🧠 OPENAI │ │ 💾 LOCAL │ │ │
│ │ │ Llama 3.1 │ ───▶ │ GPT-3.5 │ ───▶ │ Fallback │ │ │
│ │ │ (Primary) │ │ (Backup) │ │ (Keywords) │ │ │
│ │ └─────────────┘ └─────────────┘ └─────────────┘ │ │
│ │ │ │
│ │ ✓ Auto-failover ✓ Quota Detection ✓ Provider Tracking │ │
│ └───────────────────────────────────────────────────────────────────────────┘ │
│ │
└─────────────────────────────────────────────────────────────────────────────────┘

text


### Data Flow
┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐
│ User │ │ Fetch │ │ Process │ │ Index │ │ Generate │
│ Query │───▶│ News │───▶│ Text │───▶│ Docs │───▶│ Analysis │
│ │ │ (API) │ │ (NLP) │ │ (TF-IDF) │ │ (LLM) │
└──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────────┘
│ │
│ │
│ ┌──────────────────────────────────────────┐ │
│ │ 💬 Q&A Flow │ │
│ │ │ │
└─────────▶│ Question ──▶ Context Retrieval ──▶ LLM │◀───────┘
│ │
└──────────────────────────────────────────┘

---

## 📁 Project Structure
equity-research-ai-tool/
│
├── 📄 app.py # Main Streamlit application
│
├── 📁 src/ # Source modules
│ ├── init.py # Package initializer
│ ├── news_fetcher.py # NewsAPI integration
│ ├── text_processor.py # NLP text cleaning
│ ├── summarizer.py # AI summarization logic
│ ├── vector_store.py # TF-IDF search engine
│ └── llm_router.py # Multi-LLM router with fallback
│
├── 📁 .streamlit/
│ └── config.toml # Streamlit theme configuration
│
├── 📄 requirements.txt # Python dependencies
├── 📄 .env.example # Environment variables template
├── 📄 .gitignore # Git ignore rules
├── 📄 LICENSE # MIT License
└── 📄 README.md # This file

---

## 🛠 Tech Stack

<div align="center">

| Category | Technology | Purpose |
|:--------:|:----------:|:-------:|
| **Frontend** | Streamlit | Interactive Web UI |
| **Language** | Python 3.9+ | Core Programming |
| **Primary LLM** | Groq (Llama 3.1) | Fast AI Inference (~100ms) |
| **Backup LLM** | OpenAI GPT-3.5 | Reliable Fallback |
| **News Source** | NewsAPI | Real-time Financial News |
| **Search** | Scikit-learn TF-IDF | Document Similarity |
| **NLP** | NLTK, BeautifulSoup | Text Processing |

</div>


## 📦 Installation

### Prerequisites

- Python 3.9 or higher
- pip package manager
- API keys (see [API Setup](#-api-setup))

### Quick Start

```bash
# Clone the repository
git clone https://github.com/saikiran-patirla/equity-research-ai-tool.git
cd equity-research-ai-tool

# Create virtual environment
python -m venv venv

# Activate virtual environment
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create environment file
cp .env.example .env

# Add your API keys to .env file
# Then run the app
streamlit run app.py
The app will open at http://localhost:8501 🎉

🔑 API Setup
Required APIs
API	Required	Free Tier	Get Key
NewsAPI	✅ Yes	100 req/day	Get Free Key →
Groq	⭐ Recommended	✅ Free	Get Free Key →
OpenAI	Optional	$5 credit	Get Key →
Environment Configuration
Create a .env file:

env

NEWS_API_KEY=your_newsapi_key_here
GROQ_API_KEY=your_groq_key_here
OPENAI_API_KEY=your_openai_key_here
🎮 Usage
Search - Enter company name or click quick pick
Analyze - Wait 5-10 seconds for AI processing
Review - Read sentiment, insights, recommendations
Ask - Use quick questions or type custom queries
Quick Questions
Button	Question
🚀 Growth?	What are the key growth catalysts?
⚠️ Risks?	What are the main risks to watch?
📊 Analysts?	What do analysts recommend?
🔮 Outlook?	What is the future outlook?
⚡ Performance
Operation	Time
News Fetch	~1-2s
Text Processing	~0.5s
AI Analysis (Groq)	~1-3s
AI Analysis (OpenAI)	~3-5s
Total	~5-10s
🔄 LLM Failover
text

┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│    GROQ     │────▶│   OPENAI    │────▶│   LOCAL     │
│  (Primary)  │     │  (Backup)   │     │ (Fallback)  │
└─────────────┘     └─────────────┘     └─────────────┘
      ⚡                  🧠                  💾
   Fastest            Reliable           Always Works
✅ Auto-failover on quota/errors
✅ Seamless provider switching
✅ Provider tracking in UI
📄 License
MIT License - see LICENSE file.

⚠️ Disclaimer
This tool is for educational purposes only.

Not financial advice
Always consult a qualified financial advisor
AI analysis may contain errors
👨‍💻 Author
<div align="center">
Sai Kiran Patirla

GitHub
LinkedIn

⭐ Star this repo if you find it useful!

</div> ```
