from typing import Dict, Any

from utils.tokenize import tokenize_text
from inverted_index import load_movies, InvertedIndex


def movie_matches(movie: Dict[str, Any], key: str) -> bool:
    """Return True if the keyword appears in the movie title."""
    key_tokens = tokenize_text(key)
    title_tokens = tokenize_text(movie.get("title", ""))

    return any(
        key_token in title_token
        for key_token in key_tokens
        for title_token in title_tokens
    )


def search_command(key: str, limit: int = 5):
    if not key:
        return []

    idx = InvertedIndex()

    # load
    idx.load()

    key_tokens = tokenize_text(key)

    # get
    seen, results = set(), []
    for token in key_tokens:
        doc_ids = idx.get_documents(token)
        
        if doc_ids not in
        matched_movies.extend(docs)

    matched_movies.sort(key=lambda m: m.get("id", 0))

    return [m["title"] for m in matched_movies[:limit]]
