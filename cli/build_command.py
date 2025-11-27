import json
import requests

from utils.file_utils import File
from inverted_index import InvertedIndex


def load_data():
    response = requests.get(
        "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/course-rag-movies.json"
    )
    data = response.json()

    File.dump_json(data)


def build_command():
    load_data()

    idx = InvertedIndex()
    idx.build()
    idx.save()

    # docs = idx.get_documents("merida")
    # print(f"First document for token 'merida' = {docs[0]}")
