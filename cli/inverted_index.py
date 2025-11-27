from typing import Dict, Set, List
from collections import defaultdict
from utils.file_utils import File


def load_movies(movies_data_path="data/movies.json"):
    movies = File.load_json(movies_data_path).get("movies", [])
    return movies


def tokenize(text: str) -> List[str]:
    return [token.lower() for token in text.split()]


class InvertedIndex:
    def __init__(self):
        ## index maps tokens to sets of document IDs
        self.index: Dict[str, Set] = defaultdict(set)
        # docmap stores document metadata by document ID
        self.docmap: Dict[str, Dict] = defaultdict(dict)

    def __add_document(self, doc_id, text):
        tokens = tokenize(text)

        for token in tokens:
            self.index[token].add(doc_id)

    def __add_data(self, doc_id, data):
        self.docmap[doc_id] = data

    def build(self):
        movies = load_movies()
        for movie in movies:
            doc_id = movie["id"]
            text = f"{movie['title']} {movie['description']}"

            self.__add_document(doc_id, text)
            self.__add_data(doc_id, data=movie)

    def save(self):
        index_pickle_path = "cache/index.pkl"
        docmap_pickle_path = "cache/docmap.pkl"

        File.dump_pickle(index_pickle_path, self.index)
        File.dump_pickle(docmap_pickle_path, self.docmap)

    # extra
    def load(self):
        index_pickle_path = "cache/index.pkl"
        docmap_pickle_path = "cache/docmap.pkl"

        self.index = File.load_pickle(index_pickle_path)
        self.docmap = File.load_pickle(docmap_pickle_path)

    def get_documents(self, key):
        doc_ids = self.index.get(key, set())
        return sorted(list(doc_ids))
