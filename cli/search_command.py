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


def show_matched_movies(key: str, limit: int = 5):
    if not key:
        return []

    idx = InvertedIndex()

    # load
    idx.load()

    key_tokens = tokenize_text(key)

    # search
    seen_doc_ids, matched_movies = set(), []
    for token in key_tokens:
        doc_ids = idx.get_documents(token)

        for doc_id in doc_ids:
            if doc_id not in seen_doc_ids:
                seen_doc_ids.add(doc_id)
                matched_movies.append(idx.docmap[doc_id])

                if len(matched_movies) >= limit:
                    break

    matched_movies.sort(key=lambda m: m.get("id", 0))

    return [movie["title"] for movie in matched_movies]


def search_command(word):
    matched_movies_title = show_matched_movies(word)

    for idx, title in enumerate(matched_movies_title):
        print(idx + 1, title, sep=". ")
