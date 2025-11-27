from inverted_index import InvertedIndex

def idf_command(term):
    idx = InvertedIndex()
    idx.load()
    
    return idx.get_idf(term)