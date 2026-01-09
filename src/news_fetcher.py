# src/news_fetcher.py
"""
Real-Time News Fetcher
Fetches actual financial news from NewsAPI
"""

import os
import re
import requests
from datetime import datetime, timedelta
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()


class NewsFetcher:
    """Fetches real financial news from NewsAPI"""
    
    def __init__(self):
        self.api_key = os.getenv("NEWS_API_KEY")
        self.base_url = "https://newsapi.org/v2/everything"
        
        if not self.api_key:
            raise ValueError("❌ NEWS_API_KEY not found in .env file!")
        
        print("✅ NewsAPI initialized")
    
    def fetch_news(
        self, 
        query: str, 
        days: int = 7, 
        max_articles: int = 10
    ) -> List[Dict]:
        """Fetch real news articles from NewsAPI"""
        
        from_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
        to_date = datetime.now().strftime("%Y-%m-%d")
        
        params = {
            "q": f'"{query}" AND (stock OR shares OR market OR earnings OR investor)',
            "from": from_date,
            "to": to_date,
            "sortBy": "publishedAt",
            "language": "en",
            "pageSize": min(max_articles, 100),
            "apiKey": self.api_key
        }
        
        try:
            print(f"🔍 Fetching news for: {query}")
            response = requests.get(self.base_url, params=params, timeout=15)
            
            if response.status_code == 401:
                raise ValueError("❌ Invalid NewsAPI key!")
            elif response.status_code == 429:
                raise ValueError("❌ NewsAPI rate limit exceeded.")
            
            response.raise_for_status()
            data = response.json()
            
            if data.get("status") != "ok":
                raise ValueError(f"❌ NewsAPI error: {data.get('message', 'Unknown')}")
            
            articles = []
            for article in data.get("articles", []):
                if not article.get("title") or article.get("title") == "[Removed]":
                    continue
                if not article.get("url"):
                    continue
                
                articles.append({
                    "title": article.get("title", "").strip(),
                    "description": (article.get("description", "") or "").strip(),
                    "content": self._clean_content(article.get("content", "")),
                    "url": article.get("url", ""),
                    "source": article.get("source", {}).get("name", "Unknown"),
                    "published_at": self._format_date(article.get("publishedAt", "")),
                    "author": article.get("author") or "Staff Reporter",
                    "image_url": article.get("urlToImage", "")
                })
            
            print(f"✅ Found {len(articles)} articles for '{query}'")
            
            if not articles:
                return self._fetch_broader_search(query, days, max_articles)
            
            return articles
            
        except requests.exceptions.Timeout:
            raise ValueError("❌ Request timeout. Please try again.")
        except requests.exceptions.RequestException as e:
            raise ValueError(f"❌ Network error: {str(e)}")
    
    def _fetch_broader_search(self, query: str, days: int, max_articles: int) -> List[Dict]:
        """Broader search if specific search returns no results"""
        from_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
        
        params = {
            "q": query,
            "from": from_date,
            "sortBy": "relevancy",
            "language": "en",
            "pageSize": max_articles,
            "apiKey": self.api_key
        }
        
        try:
            response = requests.get(self.base_url, params=params, timeout=15)
            response.raise_for_status()
            data = response.json()
            
            articles = []
            for article in data.get("articles", []):
                if not article.get("title") or article.get("title") == "[Removed]":
                    continue
                
                articles.append({
                    "title": article.get("title", "").strip(),
                    "description": (article.get("description", "") or "").strip(),
                    "content": self._clean_content(article.get("content", "")),
                    "url": article.get("url", ""),
                    "source": article.get("source", {}).get("name", "Unknown"),
                    "published_at": self._format_date(article.get("publishedAt", "")),
                    "author": article.get("author") or "Staff Reporter",
                    "image_url": article.get("urlToImage", "")
                })
            
            return articles
            
        except Exception as e:
            print(f"⚠️ Broader search failed: {e}")
            return []
    
    def _clean_content(self, content: str) -> str:
        """Remove truncation markers"""
        if not content:
            return ""
        content = re.sub(r'\[\+\d+ chars\]', '', content)
        return content.strip()
    
    def _format_date(self, date_str: str) -> str:
        """Format date for display"""
        if not date_str:
            return "Unknown date"
        try:
            dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            return dt.strftime("%B %d, %Y at %I:%M %p")
        except:
            return date_str