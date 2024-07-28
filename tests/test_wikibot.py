# import scrape from ../wikibot.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from wikibot import scrape


def test_scrape():
    assert "Microsoft" in scrape("Microsoft")