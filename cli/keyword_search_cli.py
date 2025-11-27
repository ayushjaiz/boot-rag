import argparse
from search_command import search_command
from build_command import build_command
from tf_command import tf_command


def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    subparsers.add_parser("build", help="Build and save inverted index")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    tf_parser = subparsers.add_parser("tf", help="Find frequency of a term in a doc")
    tf_parser.add_argument("doc_id", type=int, help="Document ID")
    tf_parser.add_argument("term", type=str, help="Term to get frequency for")

    args = parser.parse_args()

    match args.command:
        case "build":
            build_command()
        case "search":
            # print the search query here
            print("Searching for:", args.query)

            word = args.query
            search_command(word)
        case "tf":
            tf = tf_command(args.doc_id, args.term)
            print(f"Term frequency of '{args.term}' in document '{args.doc_id}': {tf}")

        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
