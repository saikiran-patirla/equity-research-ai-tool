# src/text_processor.py
"""
Text Processing Module
"""

import re
import html
from typing import List, Dict


class TextProcessor:
    """Processes text for AI analysis"""
    
    def __init__(self):
        print("✅ Text Processor initialized")
    
    def clean_text(self, text: str) -> str:
        """Clean and normalize text"""
        if not text:
            return ""
        
        text = html.unescape(text)
        text = re.sub(r'https?://\S+', '', text)
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
    
    def process_articles(self, articles: List[Dict]) -> List[Dict]:
        """Process articles for analysis"""
        processed = []
        
        for article in articles:
            parts = []
            if article.get("title"):
                parts.append(article["title"])
            if article.get("description"):
                parts.append(article["description"])
            if article.get("content"):
                parts.append(article["content"])
            
            combined = " ".join(parts)
            cleaned = self.clean_text(combined)
            
            processed.append({
                **article,
                "processed_text": cleaned,
                "word_count": len(cleaned.split())
            })
        
        return processed