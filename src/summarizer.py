# src/summarizer.py
"""
AI Summarization - Optimized for Speed
"""

from typing import List, Dict
from .llm_router import LLMRouter


class Summarizer:
    """Fast financial summarization"""
    
    def __init__(self):
        self.router = LLMRouter()
        print("✅ Summarizer: Ready")
    
    def get_current_provider(self) -> str:
        return self.router.get_current_provider()
    
    def summarize_article(self, article: Dict) -> str:
        """Quick article summary"""
        title = article.get("title", "")
        content = article.get("processed_text", "") or article.get("content", "") or article.get("description", "")
        
        if not content or len(content) < 30:
            return "Insufficient content."
        
        prompt = f"""Summarize in 3 bullet points:
{title}
{content[:1000]}

• KEY: 
• IMPACT: 
• ACTION:"""

        return self.router.generate(prompt=prompt, max_tokens=150, temperature=0.2)
    
    def generate_investment_insight(self, articles: List[Dict], company: str) -> str:
        """Generate investment analysis"""
        
        if not articles:
            return "No articles available."
        
        # Compact article summaries
        summaries = []
        for i, a in enumerate(articles[:4], 1):
            title = a.get("title", "")
            content = a.get("processed_text", "") or a.get("content", "")
            summaries.append(f"{i}. {title}\n{content[:300]}")
        
        articles_text = "\n\n".join(summaries)
        
        prompt = f"""Investment analysis for {company.upper()}:

{articles_text}

Write:
## {company.upper()} Analysis

### Sentiment: [BULLISH/BEARISH/NEUTRAL]

### Key Points
• [3 specific findings]

### Catalysts
• [2 positive factors]

### Risks
• [2 concerns]

### Recommendation
[BUY/HOLD/SELL with reason]"""

        return self.router.generate(prompt=prompt, max_tokens=600, temperature=0.3)
    
    def answer_question(self, question: str, context: str, company: str) -> str:
        """Quick Q&A response"""
        
        prompt = f"""About {company}: {context[:1500]}

Question: {question}

Answer concisely and specifically. Be helpful."""

        return self.router.generate(prompt=prompt, max_tokens=300, temperature=0.3)