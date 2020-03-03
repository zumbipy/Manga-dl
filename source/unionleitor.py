import time
import requests
import re
from bs4 import BeautifulSoup
from tqdm import tqdm


class UnionLeitor:
    """This module uses a url to a manga page on the uniomangas website and converts it to a dictionary."""

    def __init__(self, url):
        self.url = url
        self.souce_page = self.__scraping_page()
        self.title = self.souce_page.h2.text

        self.content = {
            "Title": self.title,
            "Chapters": self.__list_url_chapters(),
            "Url": self.url,
        }

    def __list_url_image(self, url):
        # create souce the page the cap
        souce_page_cap = self.__scraping_page(url)

        # create list with all url the image
        list_url_cap = [url.get("src") for url in souce_page_cap.find_all("img")]
        return list_url_cap

    def __list_url_chapters(self):
        # create a list of the url of the chapters
        list_url = self.souce_page.find_all("a", string=re.compile("Cap. "))

        # {Cap. 01: [list url]}
        dict_url = {}
        for url in list_url:
            print(f"Analizando Pagina {url.text}\n", end='')
            dict_url[url.text] = self.__list_url_image(url.get("href"))
        return dict_url

    def __scraping_page(self, url=None):
        conteudo = ''
        if url == None:
            r = requests.get(self.url, stream=True)
            with tqdm(total=100, unit='kb') as barra_download:
                for i in r.iter_content(chunk_size=1024):
                    conteudo += str(i)
                    barra_download.update(1)
                barra_download.update(barra_download.total - barra_download.n)

            return BeautifulSoup(conteudo, "html.parser")
        else:
            
            r = requests.get(url, stream=True)
            with tqdm(total=100, unit='kb') as barra_download:
                for i in r.iter_content(chunk_size=1024):
                    conteudo += str(i)
                    barra_download.update(1)
                barra_download.update(barra_download.total - barra_download.n)
            return BeautifulSoup(conteudo, "html.parser")
