#!/usr/bin/env python3

import argparse
from helper import search_command

from inverted_index import InvertedIndex


def show_matched_movies(word):
    matched_movies_title = search_command(word)

    for idx, title in enumerate(matched_movies_title):
        print(idx + 1, title, sep=". ")


def build_index():
    idx = InvertedIndex()
    idx.build()
    idx.save()

    # docs = idx.get_documents("merida")
    # print(f"First document for token 'merida' = {docs[0]}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    # Add this line for the build command
    build_parser = subparsers.add_parser("build", help="Build and save inverted index")

    args = parser.parse_args()

    match args.command:
        case "search":
            # print the search query here
            print("Searching for:", args.query)

            word = args.query
            show_matched_movies(word)
        case "build":
            build_index()

        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
