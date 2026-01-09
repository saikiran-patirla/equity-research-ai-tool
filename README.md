# 📈 AI-Powered Equity Research Tool

Real-time financial news analysis powered by AI.

## 🚀 Live Demo
[**Try it here!**]([https://equity-research-ai-tool-by-sai-kiran.streamlit.app/])

## ✨ Features
- 📰 **Real-time News** - Fetches latest articles from NewsAPI
- 🤖 **AI Analysis** - Investment insights powered by Groq/GPT-4
- 💬 **Interactive Q&A** - Ask follow-up questions about any company
- 🔍 **Smart Search** - Quick picks for popular companies

## 🛠️ Tech Stack
- **Frontend**: Streamlit
- **AI/LLM**: Groq (Llama 3), OpenAI GPT-4
- **News**: NewsAPI
- **Vector Search**: FAISS + Sentence Transformers
- **NLP**: NLTK, BeautifulSoup

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/saikiran-patirla/equity-research-ai-tool.git
cd equity-research-ai-tool

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file with your API keys
echo "NEWS_API_KEY=your_key_here" >> .env
echo "GROQ_API_KEY=your_key_here" >> .env
echo "OPENAI_API_KEY=your_key_here" >> .env

# Run the app
streamlit run app.py
