"""This script of the program creates an ArgumentParser object that parses console input.

This file contains the following variables:
    - args - stores the arguments parsed from the console input.
"""

import argparse


# create the stdin parser object
parser = argparse.ArgumentParser(
    prog="RSS Parser",
    usage=f"rss_reader.py [-h] [--version] [--json] [--table] [--verbose] [--limit LIMIT]\n{'source': >27}",
    description="Pure Python command-line RSS reader.",
    allow_abbrev=False,
    epilog="Enjoy the program :)",
)

# version
parser.version = "Version 1.0"

# Add the arguments
# RSS | a link to an rss feed
parser.add_argument("RSS", metavar="source", type=str, help="the link to the rss feed")

# --version
parser.add_argument("--version", action="version", help="an optional argument")

# --json
parser.add_argument(
    "--json", action="store_true", help="Print result as JSON in stdout"
)

# --verbose
parser.add_argument("--verbose", action="store_true", help="an optional argument")

# --limit [int] | the number of entries to print
parser.add_argument(
    "--limit",
    action="store",
    type=int,
    help="Limit news topics if this parameter provided",
)

# -table | print the data as table
parser.add_argument("--table", action="store_true", help="Print result as table")


args = parser.parse_args()
