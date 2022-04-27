"""RSS feed reader

This is the main script of the program allows the user to extract RSS feed data from the RSS link provided
and format and print the data to the console.

This tool can convert and print the data in a JSON format or as table.

Python 3.9.9 or above is recommended.

This script requires that `tabulate` be installed within the Python
environment you are running this script in.

This file  contains the following
functions:

    * check_url - accepts a url and returns True if the url is valid
    * rss_to_dict - accepts RSS feed data in a string format and returns a dictionary
    * print_rss - accepts a dictionary and prints it in a formatted manner
    * main - the main function of the script
"""

import json
import re
import xml.etree.ElementTree as ET
import textwrap as tr
import requests
import tabulate

from utils import keymap
from stdin_parser import args


# <<<--- check the connection/validate the url --->>>
def check_url(stdin_url: str) -> bool:
    """Check the internet connection and validate the url

    Args:
        stdin_url (str): the url extracted from STDIN

    Returns:
        bool: evaluates to True if the url is valid and the device has internet connection
    """

    status = False

    try:
        print(f"\nChecking the url [{stdin_url}]...")
        url = requests.get(stdin_url)
        url.raise_for_status()
    except requests.exceptions.ConnectionError:
        print("\nNo internet connection :(\n")
        status = False
    except requests.HTTPError as http_err:
        print(f"\nHTTP Error occured\n{http_err}\n")
        status = False
    except requests.exceptions.InvalidURL as url_err:
        print(f"\nAn error occured: {url_err}\n")
        status = False
    except requests.exceptions.InvalidSchema as schema_err:
        print(f"\n{schema_err}")
        status = False
    except requests.exceptions.MissingSchema as missing_schema:
        print(f"\n{missing_schema}")
        status = False
    else:
        print("\nSuccess!\n")
        status = True

    return status


# <<<--- convert rss/xml into a dict --->>>
def rss_to_dict(rss: str, *limit) -> dict[str: dict[int: dict[str:str]]]:
    """Parse string-formatted RSS data and save it into a dictionary

    Returns:
        dict: triple-nested dict containing RSS feed name, numbered entries, and tags with their values.
    """

    root = ET.fromstring(rss)

    # set the right name for the tags
    tags = set()

    for descendant in root.iter():
        tags.add(descendant.tag)

    keys = {}

    for tag in tags:
        for key, _ in keymap.items():
            if keymap[key].__contains__(tag):
                keys[key] = tag

    # root changes to 'channel' or 'feed' tag if there is no 'rss' tag
    if root[0].tag == keys["channel"]:
        root = root[0]

    # create a dict of tags and values
    rss_name = root.find("title").text
    items = root.findall(keys["entry"])

    times = limit[0]

    if limit[0] is None or times > len(items):
        times = len(items)

    news_dict = {}

    for i in range(times):
        title = items[i].find(keys["title"]).text
        link = (
            items[i].find(keys["link"]).text
            if items[i].find(keys["link"]).text is not None
            else items[i].find(keys["guid"]).text
        )
        date = items[i].find(keys["date"]).text
        desc = (
            items[i].find(keys["description"]).text
            if items[i].find(keys["description"]) is not None
            else "None"
        )

        entry = {"title": title, "link": link, "date": date, "desc": desc}

        news_dict[i] = entry

    return {rss_name: news_dict}


# <<<--- tabulate/print the dict object data --->>>
def print_rss(feed_dict: dict) -> None:

    """
    Extract data from a dict, format and print it.
    If the argument '--table' is specified data is printed as table
    """

    # evaluates to True if the argument '--table' is specified
    # if True prints the data as table else prints a simple output
    if args.table:

        for key in feed_dict.keys():
            print(f"Printing {len(feed_dict[key])} entries...")
            print("\n")
            print(f"Feed: {key}")
            print("\n")
            for entry in feed_dict[key]:
                print(f"Entry #{entry+1}")
                table = []
                for tag, text in feed_dict[key][entry].items():
                    if tag == "desc":
                        text = tr.shorten(text, width=120, placeholder=" ...(more)")
                    new_row = [tag.capitalize(), text]
                    table.append(new_row)

                print(tabulate.tabulate(table, tablefmt=("fancy_grid")))
                print("\n")

    else:

        for key in feed_dict.keys():
            print(f"Printing {len(feed_dict[key])} entries...")
            print("\n")
            print(f"Feed: {key}")
            print("\n")
            for entry in feed_dict[key]:
                print(f"Entry #{entry+1}")
                for tag, text in feed_dict[key][entry].items():
                    print(f"{tag.capitalize()}: {text}")
                print("\n")


# <<<--- main function --->>>
def main() -> None:
    """Main function"""

    stdin_url = args.RSS

    connected = check_url(stdin_url)

    if connected:

        rss = requests.get(stdin_url).text

        # regex to remove the xmlns namespace
        rss = re.sub(' xmlns="[^"]+"', "", rss, count=1)

        # extract data from RSS feed string and save it in a dictionary
        rss_dict = rss_to_dict(rss, args.limit)

        # evaluats to True if the argument '--json' is provided
        if args.json:
            json_data = json.dumps(rss_dict, indent=4)
            for key, _ in rss_dict.items():
                print(f"Printing {len(rss_dict[key])} entries...\n")
            print(json_data)
        else:
            print_rss(rss_dict)


if __name__ == '__main__':
    main()
