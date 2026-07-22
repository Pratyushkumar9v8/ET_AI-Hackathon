from app.rag.mitre_kb import MITRE_ATTACK_KNOWLEDGE_BASE, search_mitre_kb

class SimpleVectorStore:
    """
    Lightweight vector RAG fallback store using keyword + semantic matching
    for fast execution in any environment.
    """
    def __init__(self):
        self.kb = MITRE_ATTACK_KNOWLEDGE_BASE

    def similarity_search(self, query: str, top_k: int = 3) -> list[dict]:
        return search_mitre_kb(query)[:top_k]

vector_store = SimpleVectorStore()
