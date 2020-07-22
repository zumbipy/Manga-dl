import time
import requests
import re
import sys
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
            "Chapters": self.__dict_chapters_link(),
            "Url": self.url,
        }
    
    def __list_url_image(self, url):
        # create souce the page the cap
        lista_saida = []
        c = BeautifulSoup(requests.get(url).content, "html.parser")
        lista_tag_img = c.findAll("img", "wp-manga-chapter-img img-responsive lazyload effect-fade")

        # create list with all url the image
        for link in lista_tag_img:
            img_link = link.get("data-src")
            lista_saida.append(img_link.strip())
        return lista_saida

    def __list_url_chapters(self):
        # create a list of the url of the chapters
        lista_saida = []
        lista_tag_cap = self.souce_page.findAll("li", "wp-manga-chapter")
        for link in lista_tag_cap:
            lista_saida.append(link.find("a").get("href")+"?style=list")
        return lista_saida

    def __dict_chapters_link(self):
        dict_saida = {}
        lista = self.__list_url_chapters()

        for url in lista:
            chave = url.split('/')[-2]
            dict_saida[chave] = self.__list_url_image(url)
        return dict_saida



    def __scraping_page(self, url=None):
        r = requests.get(self.url)
        if r.status_code == 200:
            return BeautifulSoup(r.content, "html.parser")
        else:
            print("Problema com a pagina.")
            sys.exit()

    def __title_cap(self):
        title = self.souce_page.find("div", "post-title").text
        return title.strip()
