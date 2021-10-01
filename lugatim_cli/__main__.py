from .cli import plain, rich
import argparse

__version__ = "0.0.1"

ap = argparse.ArgumentParser()
ap.add_argument(
    "word",
    type=str,
    nargs="*",
    help="<word>",
)
ap.add_argument(
    "-p",
    "--plain",
    action="store_true",
    default=False,
    help="returns plain text output",
)
ap.add_argument(
    "-a",
    "--all",
    action="store_true",
    default=False,
    help="show all results",
)
ap.add_argument("-v", "--version", action="version", version="%(prog)s v" + __version__)
args = ap.parse_args()


def cli():
    word = " ".join(args.word)
    if word == "":
        print("Please enter a word.")
    elif args.plain:
        plain(word, args.all)
    else:
        rich(word, args.all)


if __name__ == "__main__":
    cli()
