from sentence_transformers import SentenceTransformer
from utils.file_utils import File


class SemanticSearch:
    def __init__(self, model="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def generate_embedding(self, text: str):
        text = text.strip()
        if not text:
            raise ValueError("Text is empty")
        
        embedddings = self.model.encode([text])
        return embedddings[0]


def verify_model():
    search_model = SemanticSearch()

    model = search_model.model

    print(f"Model loaded: {model}")
    print(f"Max sequence length: {model.max_seq_length}")


def embed_text(text):
    search_model = SemanticSearch()
    return search_model.generate_embedding(text)
