import math

from typing import Dict, Set, Counter
from collections import defaultdict, Counter
from utils.file_utils import File
from utils.tokenize import tokenize_text


def load_movies(movies_data_path="data/movies.json"):
    movies = File.load_json(movies_data_path).get("movies", [])
    return movies


class InvertedIndex:
    def __init__(self):
        # index maps tokens to sets of document IDs
        self.index: Dict[str, Set[int]] = defaultdict(set)

        # docmap stores document metadata by document ID
        self.docmap: Dict[int, Dict] = defaultdict(dict)

        self.term_frequencies: Dict[str, Counter] = defaultdict(Counter)

        # initialise cache file fath
        self.index_pickle_path = "cache/index.pkl"
        self.docmap_pickle_path = "cache/docmap.pkl"
        self.tf_pickle_path = "cache/tf.pkl"

    # updates index dict with text given
    def __add_document(self, doc_id, text):
        tokens = tokenize_text(text)

        for token in set(tokens):
            self.index[token].add(doc_id)

        self.term_frequencies[doc_id].update(tokens)

    # updates docmap
    def __add_data(self, doc_id, data):
        self.docmap[doc_id] = data

    def build(self):
        movies = load_movies()
        for movie in movies:
            doc_id = movie["id"]
            text = f"{movie['title']} {movie['description']}"

            self.__add_document(doc_id, text)
            self.__add_data(doc_id, data=movie)

    # save index, docmap and tf to disk
    def save(self):
        File.dump_pickle(self.index_pickle_path, self.index)
        File.dump_pickle(self.docmap_pickle_path, self.docmap)
        File.dump_pickle(self.tf_pickle_path, self.term_frequencies)

    # load index, docmap and tf from disk
    def load(self):
        self.index = File.load_pickle(self.index_pickle_path)
        self.docmap = File.load_pickle(self.docmap_pickle_path)
        self.term_frequencies = File.load_pickle(self.tf_pickle_path)

    def get_documents(self, key):
        doc_ids = self.index.get(key, set())
        return sorted(list(doc_ids))

    def get_tf(self, doc_id: int, term: str) -> int:
        tokens = tokenize_text(term)
        
        if len(tokens) != 1:
            raise ValueError("term must be a single token")
        token = tokens[0]

        return self.term_frequencies[doc_id][token]
    
    def get_idf(self, term: str):
        tokens = tokenize_text(term)
        
        if len(tokens) != 1:
            raise ValueError("term must be a single token")
        token = tokens[0]
        
        doc_count = len(self.docmap)
        term_doc_count = len(self.index[token])
        
        return math.log((doc_count + 1) / (term_doc_count + 1))
    
