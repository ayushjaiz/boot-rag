import argparse
from search_command import search_command
from build_command import build_command


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
            search_command(word)
        case "build":
            build_command()

        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
