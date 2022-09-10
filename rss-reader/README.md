# RSS Feed Reader

`rss-reader` is is a command-line interface program to parse, process and save RSS Feeds.


## Installation and usage
1. Clone github repository:

       git clone https://github.com/abdusattorov/rss-reader

2. Change directory to `.../rss-reader`.

       cd .../rss-reader

3. Install necessary dependencies:

       pip install -r requirements.txt

After finishing the installation process and assuming your current directory is `.../rss_feed_reader`, you can run `rss_reader` as a
package:

    python rss_reader
    python -m rss_reader

or, provided, your current directory is `/rss_feed_reader/rss_reader`, you can directly run the
module:

    python rss_reader.py


## Functionality

To see help message, please, use `-h/--help` argument: `rss_feed_reader -h`.

    usage: rss_reader.py [-h] [--version] [--json] [--table] [--verbose] [--limit LIMIT]
                     source

    Pure Python command-line RSS reader.

    positional arguments:
    source         the link to the rss feed

    optional arguments:
    -h, --help     show this help message and exit
    --version      an optional argument
    --json         Print result as JSON in stdout
    --verbose      an optional argument
    --limit LIMIT  Limit news topics if this parameter provided
    --table        Print result as table

*Some notes*:

+ ***IMPORTANT***: Since the name `rss-reader` was already taken on https://pypi.org/, `rss_feed_reader` utility name was
  chosen. However, it is still possible to utilize the application using `rss-reader` word:

      rss-reader {YOUR ARGUMENTS}


## Parsing XML

XML is parsed by parser implemented from scratch, it exploits the idea of XML *tokenization*, dom-tree is created from
tokens.


## Tested RSS links

+ Channels like these are parsed correctly:

  https://realpython.com/atom.xml

  https://news.yahoo.com/rss/

  https://daryo.uz/uz/feed/


  ## Testing

Modules tested:

+ _parser.py

***Test coverage is xx%.***

In order to run tests, please, install dependencies:

    pip install pytest pytest-cov

Then, provided, `/Homework/MarkKanaplianik/final_task` is your current directory, please, use the following command:

    pytest --cov=rss_news_reader tests/


## Known problems:

+ Some problems with a certain type of links exist:

    + http://feeds.feedburner.com/welikedota error parsing data from such links; this error happens because
      of the way xml file of the rss feed is structured; this issue will be fixed in upcoming versions;

    + If you notice any bugs or other issues please let me know. You can reach me out at https://t.me/BackendEngineer