from sentence_transformers import SentenceTransformer
from utils.file_utils import File
from collections import defaultdict

from typing import List, Dict


class SemanticSearch:
    def __init__(self, model="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.embeddings = None
        self.documents: List[Dict] = None
        self.document_map = defaultdict(dict)

        self._embeddings_path = "cache/movie_embeddings.npy"

    def generate_embeddings(self, strings: str, show_progress_bar: bool = False):
        return self.model.encode(strings, show_progress_bar=show_progress_bar)

    def build_embeddings(self, documents):
        self.documents = documents
        self.document_map = {doc["id"]: doc for doc in documents}

        strings: List[str] = [
            f"{doc['title']}: {doc['description']}" for doc in documents
        ]

        self.embeddings = self.generate_embeddings(strings, show_progress_bar=True)

        File.dump_npy(self._embeddings_path, self.embeddings)
        return self.embeddings

    def load_or_create_embeddings(self, documents):
        self.documents = documents
        self.document_map = {doc["id"]: doc for doc in documents}

        try:
            embeddings = File.load_npy(self._embeddings_path)

            if len(embeddings) != len(documents):
                raise ValueError("Embeddings length mismatch")

            self.embeddings = embeddings
            return self.embeddings
        except (FileNotFoundError, ValueError):
            return self.build_embeddings(documents)


def verify_model():
    search_model = SemanticSearch()

    model = search_model.model

    print(f"Model loaded: {model}")
    print(f"Max sequence length: {model.max_seq_length}")


def embed_text(text):
    search_model = SemanticSearch()
    if not text.strip():
        raise ValueError("Text empty")

    embeddings = search_model.generate_embedding([text])
    return embeddings[0]


def verify_embeddings():
    search_model = SemanticSearch()

    data = File.load_json("data/movies.json")
    documents = data.get("movies", [])

    embeddings = search_model.load_or_create_embeddings(documents)

    print(f"Number of docs: {len(documents)}")
    print(
        f"Embeddings shape: {embeddings.shape[0]} vectors in {embeddings.shape[1]} dimensions"
    )
