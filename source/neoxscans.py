import time
import requests
import re
from bs4 import BeautifulSoup
from tqdm import tqdm


class NeoxScans():
    """This module uses a url to a manga page on the uniomangas website and converts it to a dictionary."""

    def __init__(self, url):
        self.url = url
        self.souce_page = self.__scraping_page()
        self.title = self.__title_cap()

        self.content = {
            "Title": self.title,
            "Chapters": self.__list_url_chapters(),
            "Url": self.url,
        }

    def __list_url_image(self, url):
        # create souce the page the cap

        # create list with all url the image
        pass

    def __list_url_chapters(self):
        # create a list of the url of the chapters
        pass

    def __scraping_page(self, url=None):
        pass

    def __title_cap(self):
        title = ''
        return title
