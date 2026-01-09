# src/llm_router.py
"""
Fast LLM Router
"""

import os
from typing import Optional, List
from dotenv import load_dotenv

load_dotenv()


class LLMRouter:
    """Fast LLM Router"""
    
    def __init__(self):
        self.current_provider = None
        self.failed_providers = set()
        self._groq_client = None
        self._openai_client = None
        
        # Initialize Groq (primary)
        groq_key = os.getenv("GROQ_API_KEY")
        if groq_key:
            try:
                from groq import Groq
                self._groq_client = Groq(api_key=groq_key)
                print("   ✅ Groq ready")
            except Exception as e:
                print(f"   ❌ Groq: {e}")
        
        # Initialize OpenAI (backup)
        openai_key = os.getenv("OPENAI_API_KEY")
        if openai_key:
            try:
                from openai import OpenAI
                self._openai_client = OpenAI(api_key=openai_key)
                print("   ✅ OpenAI ready")
            except Exception as e:
                print(f"   ❌ OpenAI: {e}")
        
        print(f"✅ LLM Router ready")
    
    def generate(self, prompt: str, system_prompt: str = "", max_tokens: int = 300, temperature: float = 0.3) -> str:
        """Generate response quickly"""
        
        # Try Groq first (fastest)
        if self._groq_client and "Groq" not in self.failed_providers:
            try:
                return self._call_groq(prompt, system_prompt, max_tokens, temperature)
            except Exception as e:
                print(f"⚠️ Groq: {str(e)[:50]}")
                if "quota" in str(e).lower():
                    self.failed_providers.add("Groq")
        
        # Try OpenAI
        if self._openai_client and "OpenAI" not in self.failed_providers:
            try:
                return self._call_openai(prompt, system_prompt, max_tokens, temperature)
            except Exception as e:
                print(f"⚠️ OpenAI: {str(e)[:50]}")
                if "quota" in str(e).lower():
                    self.failed_providers.add("OpenAI")
        
        # Local fallback
        return self._local_fallback(prompt)
    
    def _call_groq(self, prompt: str, system_prompt: str, max_tokens: int, temperature: float) -> str:
        """Fast Groq call"""
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})
        
        # Use fastest model
        response = self._groq_client.chat.completions.create(
            model="llama-3.1-8b-instant",  # Fastest
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature
        )
        
        self.current_provider = "Groq"
        return response.choices[0].message.content
    
    def _call_openai(self, prompt: str, system_prompt: str, max_tokens: int, temperature: float) -> str:
        """OpenAI call"""
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})
        
        response = self._openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature
        )
        
        self.current_provider = "OpenAI"
        return response.choices[0].message.content
    
    def _local_fallback(self, prompt: str) -> str:
        """Extract key info locally"""
        self.current_provider = "Local"
        
        lines = prompt.split('\n')
        keywords = ['revenue', 'profit', 'growth', 'analyst', 'upgrade', 'downgrade', 
                   'buy', 'sell', 'hold', 'bullish', 'bearish', 'billion', 'million', '%']
        
        relevant = []
        for line in lines:
            line = line.strip()
            if len(line) > 30 and any(k in line.lower() for k in keywords):
                relevant.append(line)
        
        if relevant:
            return "**Key Points:**\n\n• " + "\n• ".join(relevant[:4])
        return "Please check your API keys for AI analysis."
    
    def get_current_provider(self) -> str:
        return self.current_provider or ""
    
    def reset_failed_providers(self):
        self.failed_providers = set()


class EmbeddingRouter:
    def __init__(self):
        self.use_tfidf = True
        print("✅ Embeddings: TF-IDF")
    
    def get_embedding(self, text: str) -> Optional[List[float]]:
        return None
    
    def should_use_tfidf(self) -> bool:
        return True