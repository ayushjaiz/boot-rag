from inverted_index import InvertedIndex


def tfidf_command(doc_id, term):
    idx = InvertedIndex()

    idx.load()

    return idx.get_tfidf(doc_id, term)
