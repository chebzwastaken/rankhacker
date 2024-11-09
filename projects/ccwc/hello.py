import argparse
import os


def get_file_stats(filename):
    """Read file once and calculate bytes, lines, words, and characters."""
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    bytes_size = os.path.getsize(filename)
    num_lines = content.count("\n") + (1 if content and content[-1] != "\n" else 0)
    num_words = len(content.split())
    num_chars = len(content)
    return bytes_size, num_lines, num_words, num_chars


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate file statistics.")
    parser.add_argument("filename", help="Name of the file to analyze.")
    parser.add_argument(
        "-c",
        "--countbytes",
        action="store_true",
        help="Count the number of bytes in the file.",
    )
    parser.add_argument(
        "-l",
        "--numberoflines",
        action="store_true",
        help="Count the number of lines in the file.",
    )
    parser.add_argument(
        "-w",
        "--numberofwords",
        action="store_true",
        help="Count the number of words in the file.",
    )
    parser.add_argument(
        "-m",
        "--numberofchars",
        action="store_true",
        help="Count the number of characters in the file.",
    )

    args = parser.parse_args()

    # Get all stats at once
    try:
        bytes_size, num_lines, num_words, num_chars = get_file_stats(args.filename)
    except FileNotFoundError:
        print(f"Error: File '{args.filename}' not found.")
        exit(1)
    except IOError:
        print(f"Error: Could not read file '{args.filename}'.")
        exit(1)

    # Display results based on the selected flags
    if args.countbytes:
        print(f"Bytes: {bytes_size}")
    if args.numberoflines:
        print(f"Lines: {num_lines}")
    if args.numberofwords:
        print(f"Words: {num_words}")
    if args.numberofchars:
        print(f"Characters: {num_chars}")

    # If no flags are provided, show all statistics
    if not (
        args.countbytes
        or args.numberoflines
        or args.numberofwords
        or args.numberofchars
    ):
        print(
            f"Bytes: {bytes_size}\nLines: {num_lines}\nWords: {num_words}\nCharacters: {num_chars}"
        )
