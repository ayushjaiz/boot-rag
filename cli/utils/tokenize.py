from typing import List
import string

from nltk.stem import PorterStemmer
from utils.file_utils import File

stemmer = PorterStemmer()


def load_movies(path: str = "data/movies.json") -> List:
    data = File.load_json(path)
    return data.get("movies", [])


def load_stop_words(path="data/stopwords.txt") -> List[str]:
    return File.load_txt(path).splitlines()


def stemmed_token(token):
    return stemmer.stem(token)


def preprocess_text(s):
    PUNCT_TABLE = str.maketrans("", "", string.punctuation)

    return s.lower().translate(PUNCT_TABLE)


def tokenize_text(text):
    # preprocess text ie convert to lower and remove punctuataion
    text = preprocess_text(text)

    # create tokens
    tokens = text.split()

    # stem over removing stop words
    stop_words = load_stop_words()
    tokens = [stemmed_token(token) for token in tokens if token not in stop_words]

    return tokens
