#!/usr/bin/env python3

import argparse

from lib.semantic_search import verify_model, embed_text


def verify_command():
    verify_model()
    
def embed_text_command(text):
    return embed_text(text)


def main():
    parser = argparse.ArgumentParser(description="Semantic Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    verify_parser = subparsers.add_parser(
        "verify", help="verify the semantic seacrh model"
    )
    
    embed_text_parser = subparsers.add_parser("embed_text", help="Find embedding")
    embed_text_parser.add_argument("text", type=str, help="Text you want to find embedding for")
    
    args = parser.parse_args()

    match args.command:
        case "verify":
            verify_command()
        case "embed_text":
            text = args.text
            embedding = embed_text_command(args.text)
            
            print(f"Text: {text}")
            print(f"First 3 dimensions: {embedding[:3]}")
            print(f"Dimensions: {embedding.shape[0]}")
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
