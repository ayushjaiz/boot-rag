from inverted_index import InvertedIndex


def tf_command(doc_id, term):
    if not doc_id or not term:
        raise ValueError("doc id or term missing")

    idx = InvertedIndex()

    # load
    idx.load()

    return idx.get_tf(doc_id, term)
