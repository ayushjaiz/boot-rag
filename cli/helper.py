import json
from pathlib import Path
from typing import Dict, List, Any
import string

from nltk.stem import PorterStemmer

stemmer = PorterStemmer()


def load_movies(path: str = "data/movies.json"):
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError("Movie file not found:", file_path)

    with file_path.open() as f:
        data = json.load(f)

        return data.get("movies", [])


def load_stop_words(path="data/stopwords.txt") -> List[str]:
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError("Movie file not found:", file_path)

    with file_path.open() as f:
        return f.read().splitlines()


def stemmed_token(token):
    return stemmer.stem(token)


def preprocess_text(s):
    PUNCT_TABLE = str.maketrans("", "", string.punctuation)

    return s.lower().translate(PUNCT_TABLE)


def tokenize_text(text):
    stop_words = load_stop_words()

    tokens = preprocess_text(text).split()
    tokens = [stemmed_token(token) for token in tokens if token not in stop_words]

    return tokens


def movie_matches(movie: Dict[str, Any], key: str) -> bool:
    """Return True if the keyword appears in the movie title."""
    key_tokens = tokenize_text(key)
    title_tokens = tokenize_text(movie.get("title", ""))

    return any(
        key_token in title_token
        for key_token in key_tokens
        for title_token in title_tokens
    )


def search(keyword: str, limit: int = 5):
    if not keyword:
        return []

    movies = load_movies()

    matched = [m for m in movies if movie_matches(m, keyword)]

    matched.sort(key=lambda m: m.get("id", 0))

    return [m["title"] for m in matched[:limit]]
