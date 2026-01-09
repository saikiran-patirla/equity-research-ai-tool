# src/vector_store.py
"""
Vector Store with TF-IDF Search
"""

from typing import List, Dict
import numpy as np


class VectorStore:
    """Document store with TF-IDF search"""
    
    def __init__(self):
        self.documents: List[Dict] = []
        self.tfidf_matrix = None
        self.vectorizer = None
        
        try:
            from sklearn.feature_extraction.text import TfidfVectorizer
            self.vectorizer = TfidfVectorizer(
                max_features=5000,
                stop_words='english',
                ngram_range=(1, 2)
            )
            print("✅ Vector Store: Ready")
        except ImportError:
            print("⚠️ Vector Store: sklearn not installed")
    
    def add_documents(self, documents: List[Dict]):
        """Add documents and build search index"""
        self.documents = documents
        
        if not documents:
            print("⚠️ No documents to index")
            return
        
        if not self.vectorizer:
            print("⚠️ No vectorizer available")
            return
        
        # Build text corpus
        texts = []
        for doc in documents:
            text_parts = []
            if doc.get("title"):
                text_parts.append(doc["title"])
            if doc.get("description"):
                text_parts.append(doc["description"])
            if doc.get("processed_text"):
                text_parts.append(doc["processed_text"])
            elif doc.get("content"):
                text_parts.append(doc["content"])
            
            combined = " ".join(text_parts)
            texts.append(combined if combined else "empty")
        
        try:
            self.tfidf_matrix = self.vectorizer.fit_transform(texts)
            print(f"✅ Indexed {len(texts)} documents")
        except Exception as e:
            print(f"⚠️ Indexing error: {e}")
    
    def search(self, query: str, top_k: int = 3) -> List[Dict]:
        """Search for relevant documents"""
        if not self.documents:
            return []
        
        # If TF-IDF available, use it
        if self.tfidf_matrix is not None and self.vectorizer:
            try:
                from sklearn.metrics.pairwise import cosine_similarity
                
                query_vec = self.vectorizer.transform([query])
                similarities = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
                
                # Get top results
                top_indices = np.argsort(similarities)[-top_k:][::-1]
                results = [self.documents[idx] for idx in top_indices]
                return results
                
            except Exception as e:
                print(f"⚠️ Search error: {e}")
        
        # Fallback: return first documents
        return self.documents[:top_k]
    
    def get_context(self, question: str) -> str:
        """
        Get context for Q&A - ALWAYS returns something useful
        This is the key fix!
        """
        
        # If no documents, return empty
        if not self.documents:
            print("⚠️ No documents available for context")
            return ""
        
        # Try to search for relevant docs
        docs = self.search(question, top_k=3)
        
        # If search returned nothing, just use all documents
        if not docs:
            docs = self.documents[:3]
            print(f"ℹ️ Using all {len(docs)} documents as context")
        
        # Build context from documents
        context_parts = []
        
        for i, doc in enumerate(docs, 1):
            source = doc.get('source', 'Unknown Source')
            title = doc.get('title', 'Article')
            date = doc.get('published_at', '')
            
            # Get content - try multiple fields
            content = ""
            if doc.get('processed_text'):
                content = doc['processed_text']
            elif doc.get('content'):
                content = doc['content']
            elif doc.get('description'):
                content = doc['description']
            
            # Truncate if too long
            content = content[:1000] if content else "No content available"
            
            context_parts.append(f"""
ARTICLE {i}:
Source: {source}
Date: {date}
Title: {title}
Content: {content}
""")
        
        full_context = "\n---\n".join(context_parts)
        
        print(f"✅ Built context from {len(docs)} articles ({len(full_context)} chars)")
        
        return full_context