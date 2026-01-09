# app.py
"""
AI-Powered Equity Research Tool
Built by Sai Kiran Patirla
"""

import streamlit as st
import os
from dotenv import load_dotenv
from datetime import datetime

# MUST BE FIRST STREAMLIT COMMAND
st.set_page_config(
    page_title="AI Equity Research Tool",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_dotenv()

# API Keys
def get_api_key(key_name):
    """Get API key from environment or Streamlit secrets"""
    # First trying for local development
    env_value = os.getenv(key_name)
    if env_value:
        return env_value
    
    # If not, try for streamlit cloud deployment
    try:
        if hasattr(st, 'secrets') and key_name in st.secrets:
            return st.secrets[key_name]
    except Exception:
        pass
    
    return None

NEWS_API_KEY = get_api_key("NEWS_API_KEY")
OPENAI_API_KEY = get_api_key("OPENAI_API_KEY")
GROQ_API_KEY = get_api_key("GROQ_API_KEY")

# Set environment variables for other modules
if OPENAI_API_KEY:
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
if GROQ_API_KEY:
    os.environ["GROQ_API_KEY"] = GROQ_API_KEY

# CSS Styles
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    html, body, .main {
        font-family: 'Inter', sans-serif;
    }
    
    /* Remove default Streamlit top padding */
    .stApp > header {
        display: none !important;
    }
    
    header[data-testid="stHeader"] {
        display: none !important;
        height: 0 !important;
    }
    
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
        max-width: 100% !important;
    }
    
    /* SIDEBAR - Full height with small top gap */
    [data-testid="stSidebar"] {
        min-height: 100vh !important;
        height: 100% !important;
    }
    
    [data-testid="stSidebar"] > div:first-child {
        min-height: 100vh !important;
        height: 100% !important;
        padding-top: 0.5rem !important;
        padding-bottom: 2rem !important;
        background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%) !important;
    }
    
    section[data-testid="stSidebar"] {
        min-height: 100vh !important;
        background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%) !important;
    }
    
    [data-testid="stSidebarContent"] {
        padding-top: 0 !important;
    }
    
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:first-child {
        margin-top: 0 !important;
        padding-top: 0 !important;
    }
    
    /* Main header styles */
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #0ea5e9;
        text-align: center;
        margin: 0 0 0.25rem 0 !important;
        padding: 0 !important;
    }
    
    .header-subtitle {
        color: #94a3b8;
        font-size: 1.05rem;
        text-align: center;
        margin: 0 0 0.75rem 0 !important;
        padding: 0 !important;
    }
    
    .header-line {
        height: 3px;
        background: linear-gradient(90deg, transparent, #0ea5e9, #3b82f6, #8b5cf6, transparent);
        margin: 0.5rem 0 1.25rem 0;
        border-radius: 3px;
    }
    
    .metric-card {
        background: linear-gradient(145deg, #1e293b, #0f172a);
        border: 1px solid #334155;
        border-radius: 16px;
        padding: 1.25rem;
        text-align: center;
        margin-bottom: 0.75rem;
    }
    
    .metric-value {
        font-size: 1.75rem;
        font-weight: 700;
        color: #0ea5e9;
    }
    
    .metric-label {
        font-size: 0.8rem;
        color: #64748b;
        text-transform: uppercase;
        margin-top: 0.25rem;
    }
    
    .article-source {
        background: linear-gradient(135deg, #0ea5e9, #3b82f6);
        color: white;
        padding: 0.35rem 0.85rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        display: inline-block;
        margin-right: 0.5rem;
    }
    
    .insight-box {
        background: linear-gradient(145deg, #0c4a6e, #1e3a5f);
        border-radius: 16px;
        padding: 1.5rem;
        margin: 0.75rem 0;
        border-left: 5px solid #0ea5e9;
        line-height: 1.7;
    }
    
    .qa-box {
        background: linear-gradient(145deg, #1e293b, #0f172a);
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 1.25rem;
        margin: 0.75rem 0;
    }
    
    .qa-question {
        color: #22d3ee;
        font-weight: 600;
        font-size: 0.95rem;
        margin-bottom: 0.5rem;
    }
    
    .qa-answer {
        background: linear-gradient(145deg, #0c4a6e, #1e3a5f);
        border-radius: 10px;
        padding: 1rem;
        border-left: 4px solid #22d3ee;
        margin-top: 0.5rem;
        line-height: 1.6;
    }
    
    .qa-time {
        color: #64748b;
        font-size: 0.7rem;
        margin-top: 0.5rem;
    }
    
    .provider-badge {
        background: linear-gradient(135deg, #10b981, #059669);
        color: white;
        padding: 0.25rem 0.65rem;
        border-radius: 20px;
        font-size: 0.7rem;
        font-weight: 600;
        display: inline-block;
    }
    
    /* Button styles */
    .stButton > button {
        background: linear-gradient(135deg, #0ea5e9, #3b82f6);
        color: white;
        border: none;
        border-radius: 10px;
        font-weight: 600;
        padding: 0.5rem 1rem;
        transition: all 0.2s ease;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #0284c7, #2563eb);
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(14, 165, 233, 0.3);
    }
    
    /* Disabled button style */
    .stButton > button:disabled {
        background: linear-gradient(135deg, #475569, #334155) !important;
        color: #94a3b8 !important;
        cursor: not-allowed !important;
        transform: none !important;
        box-shadow: none !important;
    }
    
    .welcome-box {
        text-align: center;
        padding: 2.5rem;
        background: linear-gradient(145deg, #1e293b, #0f172a);
        border-radius: 16px;
        border: 1px solid #334155;
        margin: 1.5rem 0;
    }
    
    .footer {
        text-align: center;
        color: #64748b;
        padding: 1.5rem 0;
        margin-top: 2rem;
        border-top: 1px solid #334155;
        font-size: 0.85rem;
    }
    
    .footer a { color: #0ea5e9; text-decoration: none; }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    .section-title {
        color: #f1f5f9;
        font-size: 1.3rem;
        font-weight: 600;
        margin: 1rem 0 0.75rem 0;
    }
    
    /* Search input styling */
    .stTextInput > div > div > input {
        border-radius: 10px !important;
        border: 2px solid #334155 !important;
        padding: 0.75rem 1rem !important;
        font-size: 1rem !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #0ea5e9 !important;
        box-shadow: 0 0 0 2px rgba(14, 165, 233, 0.2) !important;
    }
    
    /* Sidebar header with small top gap */
    .sidebar-header {
        text-align: center;
        padding: 0.5rem 0 0 0 !important;
        margin: 0 0 0.5rem 0 !important;
    }
    
    .current-search {
        background: linear-gradient(135deg, #0ea5e9, #3b82f6);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem 0;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Check NewsAPI
if not NEWS_API_KEY:
    st.error("❌ NEWS_API_KEY not found! Add it to .env file or Streamlit secrets.")
    st.stop()

# ============ SESSION STATE ============
def init_session_state():
    defaults = {
        'articles': [],
        'company': "",
        'insight': "",
        'current_provider': "",
        'qa_history': [],
        'qa_input_key': 0,
        'search_key': 0,
        'asked_quick_questions': set(),
        'last_search': "",
        'search_query': "",
        'trigger_search': False,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            if key == 'asked_quick_questions':
                st.session_state[key] = set()
            else:
                st.session_state[key] = value

init_session_state()

# ============ COMPONENTS ============
@st.cache_resource
def load_components():
    from src.news_fetcher import NewsFetcher
    from src.text_processor import TextProcessor
    from src.summarizer import Summarizer
    from src.vector_store import VectorStore
    return {
        "news": NewsFetcher(),
        "processor": TextProcessor(),
        "summarizer": Summarizer(),
        "vectors": VectorStore()
    }

try:
    components = load_components()
    init_success = True
except Exception as e:
    init_success = False
    init_error = str(e)

# ============ HELPER FUNCTIONS ============
def clear_all_state():
    """Clear all search-related state"""
    st.session_state.articles = []
    st.session_state.company = ""
    st.session_state.insight = ""
    st.session_state.qa_history = []
    st.session_state.asked_quick_questions = set()
    st.session_state.last_search = ""
    st.session_state.search_query = ""
    st.session_state.current_provider = ""
    st.session_state.search_key += 1

def perform_search(search_term: str, days: int, max_arts: int):
    """Perform the actual search and analysis"""
    st.session_state.articles = []
    st.session_state.insight = ""
    st.session_state.qa_history = []
    st.session_state.asked_quick_questions = set()
    st.session_state.company = search_term
    st.session_state.last_search = search_term
    st.session_state.search_query = search_term
    
    with st.status(f"🔍 Analyzing **{search_term}**...", expanded=True) as status:
        st.write("📰 Fetching news...")
        try:
            articles = components["news"].fetch_news(search_term, days, max_arts)
        except Exception as e:
            st.error(f"❌ {e}")
            st.session_state.company = ""
            return False
        
        if not articles:
            status.update(label="⚠️ No articles found", state="error")
            st.warning(f"No news for **{search_term}**. Try another company.")
            st.session_state.company = ""
            return False
        
        st.write(f"🔧 Processing {len(articles)} articles...")
        processed = components["processor"].process_articles(articles)
        st.session_state.articles = processed
        
        st.write("🧠 Building search index...")
        components["vectors"].add_documents(processed)
        
        st.write("💡 Generating AI analysis...")
        insight = components["summarizer"].generate_investment_insight(processed, search_term)
        st.session_state.insight = insight
        st.session_state.current_provider = components["summarizer"].get_current_provider()
        
        status.update(label="✅ Analysis complete!", state="complete", expanded=False)
    
    st.success(f"🎉 Analyzed **{len(processed)} articles** about **{search_term}**")
    return True

def ask_question(question: str, question_id: str = None):
    """Process a question and add to history"""
    context_parts = []
    for a in st.session_state.articles[:3]:
        title = a.get('title', '')
        content = a.get('processed_text', '') or a.get('content', '') or a.get('description', '')
        context_parts.append(f"{title}\n{content[:300]}")
    context = "\n---\n".join(context_parts)
    
    answer = components["summarizer"].answer_question(
        question, context, st.session_state.company
    )
    st.session_state.current_provider = components["summarizer"].get_current_provider()
    
    st.session_state.qa_history.insert(0, {
        "question": question,
        "answer": answer,
        "time": datetime.now().strftime("%I:%M %p"),
        "provider": st.session_state.current_provider,
        "id": question_id
    })
    
    if question_id:
        st.session_state.asked_quick_questions.add(question_id)

# ============ SIDEBAR ============
with st.sidebar:
    st.markdown("""
    <div class="sidebar-header">
        <div style="font-size: 2.5rem;">📈</div>
        <div style="font-size: 1.1rem; font-weight: 700; color: #f1f5f9;">AI Equity Research</div>
        <div style="font-size: 0.75rem; color: #64748b;">by Sai Kiran Patirla</div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.session_state.company:
        st.markdown(f'''
        <div class="current-search">
            🔍 {st.session_state.company}
        </div>
        ''', unsafe_allow_html=True)
    
    st.markdown("---")
    days_back = st.slider("📅 Days to look back", 1, 30, 7)
    max_articles = st.slider("📰 Maximum articles", 5, 20, 10)
    
    st.markdown("---")
    st.markdown("**🔌 API Status**")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"{'✅' if NEWS_API_KEY else '❌'} NewsAPI")
        st.markdown(f"{'✅' if GROQ_API_KEY else '⭕'} Groq")
    with col2:
        st.markdown(f"{'✅' if OPENAI_API_KEY else '⭕'} OpenAI")
    
    if st.session_state.current_provider:
        st.markdown(f"**Active:** `{st.session_state.current_provider}`")
    
    st.markdown("---")
    st.markdown("**🛠️ Actions**")
    
    if st.button("🔄 Reset LLM", use_container_width=True):
        if init_success:
            components["summarizer"].router.reset_failed_providers()
            st.toast("✅ LLM providers reset!", icon="🔄")
    
    if st.session_state.qa_history:
        if st.button("🗑️ Clear Q&A", use_container_width=True):
            st.session_state.qa_history = []
            st.session_state.asked_quick_questions = set()
            st.rerun()
        st.caption(f"*{len(st.session_state.qa_history)} questions*")
    
    if st.session_state.articles:
        st.markdown("---")
        if st.button("🔍 New Search", use_container_width=True, type="primary"):
            clear_all_state()
            st.rerun()
    
    st.markdown("<br>" * 5, unsafe_allow_html=True)

# ============ MAIN CONTENT ============
if not init_success:
    st.error(f"❌ Error: {init_error}")
    st.stop()

# ============ HEADER ============
st.markdown("""
<h1 class="main-header">📈 AI Equity Research Tool</h1>
<p class="header-subtitle">Real-time financial news analysis powered by AI</p>
""", unsafe_allow_html=True)

st.markdown('<div class="header-line"></div>', unsafe_allow_html=True)

# ============ SEARCH SECTION ============
st.markdown("**🔍 Enter company name or ticker:**")

with st.form(key=f"search_form_{st.session_state.search_key}", clear_on_submit=False):
    col1, col2, col3 = st.columns([5, 1, 1])
    
    with col1:
        query = st.text_input(
            "Search",
            value=st.session_state.search_query,
            placeholder="e.g., Apple, AAPL, Tesla, PayPal...",
            label_visibility="collapsed",
            key=f"search_input_{st.session_state.search_key}"
        )
    
    with col2:
        search_submitted = st.form_submit_button("🚀 Analyze", use_container_width=True)
    
    with col3:
        clear_clicked = st.form_submit_button("❌ Clear", use_container_width=True)

if clear_clicked:
    clear_all_state()
    st.rerun()

st.markdown("**🔥 Quick picks:**")
cols = st.columns(8)
quick_companies = ["Apple", "Tesla", "Microsoft", "NVIDIA", "Amazon", "Google", "Meta", "PayPal"]

for i, company in enumerate(quick_companies):
    with cols[i]:
        if st.button(company, key=f"q_{company}_{st.session_state.search_key}", use_container_width=True):
            st.session_state.search_query = company
            st.session_state.trigger_search = True
            st.session_state.search_key += 1
            st.rerun()

st.markdown("---")

# ============ EXECUTE SEARCH ============
search_term = None

if search_submitted and query and query.strip():
    search_term = query.strip()
    st.session_state.search_query = search_term

elif st.session_state.trigger_search and st.session_state.search_query:
    search_term = st.session_state.search_query
    st.session_state.trigger_search = False

if search_term:
    if search_term.lower() != st.session_state.last_search.lower() or not st.session_state.articles:
        if perform_search(search_term, days_back, max_articles):
            st.rerun()
    elif st.session_state.articles:
        pass

# ============ RESULTS ============
if st.session_state.articles:
    articles = st.session_state.articles
    company = st.session_state.company
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f'''
        <div class="metric-card">
            <div class="metric-value">{len(articles)}</div>
            <div class="metric-label">📰 Articles</div>
        </div>
        ''', unsafe_allow_html=True)
    
    with col2:
        st.markdown(f'''
        <div class="metric-card">
            <div class="metric-value">{len(set(a["source"] for a in articles))}</div>
            <div class="metric-label">📡 Sources</div>
        </div>
        ''', unsafe_allow_html=True)
    
    with col3:
        st.markdown(f'''
        <div class="metric-card">
            <div class="metric-value">{sum(a.get("word_count", 0) for a in articles):,}</div>
            <div class="metric-label">📝 Words</div>
        </div>
        ''', unsafe_allow_html=True)
    
    with col4:
        provider = st.session_state.current_provider or "AI"
        st.markdown(f'''
        <div class="metric-card">
            <div class="metric-value">{provider}</div>
            <div class="metric-label">🤖 Model</div>
        </div>
        ''', unsafe_allow_html=True)
    
    st.markdown('<p class="section-title">🤖 AI Investment Analysis</p>', unsafe_allow_html=True)
    st.markdown(f'<div class="insight-box">{st.session_state.insight}</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown(f'<p class="section-title">💬 Ask Questions About {company}</p>', unsafe_allow_html=True)
    
    quick_questions = [
        ("qq_growth", "🚀 Growth?", "What are the key growth catalysts and opportunities?"),
        ("qq_risks", "⚠️ Risks?", "What are the main risks investors should watch?"),
        ("qq_analysts", "📊 Analysts?", "What do analysts recommend? Any upgrades or downgrades?"),
        ("qq_outlook", "🔮 Outlook?", "What is the future outlook based on recent news?"),
    ]
    
    qcols = st.columns(4)
    
    for i, (qid, label, full_question) in enumerate(quick_questions):
        with qcols[i]:
            is_asked = qid in st.session_state.asked_quick_questions
            
            if is_asked:
                st.button(
                    f"✅ Asked",
                    key=f"{qid}_{st.session_state.search_key}",
                    use_container_width=True,
                    disabled=True,
                    help=f"Already asked: {label}"
                )
            else:
                if st.button(
                    label,
                    key=f"{qid}_{st.session_state.search_key}",
                    use_container_width=True
                ):
                    with st.spinner("🤔 Thinking..."):
                        ask_question(full_question, qid)
                    st.rerun()
    
    with st.form(key=f"qa_form_{st.session_state.qa_input_key}", clear_on_submit=True):
        col1, col2 = st.columns([5, 1])
        with col1:
            custom_question = st.text_input(
                "Your question:",
                placeholder=f"Ask anything about {company}...",
                label_visibility="collapsed"
            )
        with col2:
            ask_submitted = st.form_submit_button("Ask", use_container_width=True)
        
        if ask_submitted and custom_question and custom_question.strip():
            with st.spinner("🤔 Thinking..."):
                ask_question(custom_question.strip())
            st.session_state.qa_input_key += 1
            st.rerun()
    
    if st.session_state.qa_history:
        st.markdown(f"**📜 Answers ({len(st.session_state.qa_history)})**")
        
        for qa in st.session_state.qa_history:
            st.markdown(f'''
            <div class="qa-box">
                <div class="qa-question">❓ {qa["question"]}</div>
                <div class="qa-answer">{qa["answer"]}</div>
                <div class="qa-time">🕐 {qa["time"]} • {qa.get("provider", "AI")}</div>
            </div>
            ''', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown('<p class="section-title">📰 News Sources</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    with col2:
        show_summaries = st.checkbox("Show AI summaries", value=False)
    
    for i, article in enumerate(articles):
        with st.expander(f"📄 {article['title'][:70]}...", expanded=False):
            cols = st.columns([2, 1])
            with cols[0]:
                st.markdown(f'''
                <span class="article-source">{article["source"]}</span>
                <span style="color: #64748b; font-size: 0.85rem;">📅 {article["published_at"]}</span>
                ''', unsafe_allow_html=True)
            with cols[1]:
                if article.get('url'):
                    st.link_button("🔗 Read Full", article['url'], use_container_width=True)
            
            if article.get('description'):
                st.markdown(f"*{article['description']}*")
            
            if show_summaries:
                with st.spinner("Generating..."):
                    summary = components["summarizer"].summarize_article(article)
                st.info(f"**🤖 AI Summary:** {summary}")

else:
    st.markdown("""
    <div class="welcome-box">
        <div style="font-size: 3rem;">🚀</div>
        <h2 style="color: #f1f5f9; margin: 0.75rem 0; font-size: 1.5rem;">Welcome to AI Equity Research</h2>
        <p style="color: #94a3b8; font-size: 1rem; margin: 0.5rem 0;">
            Enter a company name above or click a quick pick to get started.
        </p>
        <div style="margin-top: 1rem; padding: 0.75rem; background: rgba(14, 165, 233, 0.1); border-radius: 10px;">
            <p style="color: #22d3ee; margin: 0; font-size: 0.9rem;">
                💡 <strong>Try:</strong> Click "Apple" or "Tesla" above!
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div style="font-size: 1.5rem;">📰</div>
            <div style="color: #f1f5f9; font-weight: 600; margin: 0.5rem 0;">Real-time News</div>
            <div style="color: #64748b; font-size: 0.85rem;">Latest articles from top sources</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div style="font-size: 1.5rem;">🤖</div>
            <div style="color: #f1f5f9; font-weight: 600; margin: 0.5rem 0;">AI Analysis</div>
            <div style="color: #64748b; font-size: 0.85rem;">Powered by Groq & GPT-4</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div style="font-size: 1.5rem;">💬</div>
            <div style="color: #f1f5f9; font-weight: 600; margin: 0.5rem 0;">Ask Questions</div>
            <div style="color: #64748b; font-size: 0.85rem;">Interactive Q&A on any company</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    Built by <a href="https://github.com/saikiran-patirla">Sai Kiran Patirla</a> • 
    ⚠️ For educational purposes only
</div>
""", unsafe_allow_html=True)