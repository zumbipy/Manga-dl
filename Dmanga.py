import os
import os.path

import requests
import wget
from bs4 import BeautifulSoup



class DownloadManga():

    def __init__(self, url):
        self.page = self.site_connect(url)
        self.url = url
        self.list_link = self.all_link_cap()
        self.titulo_manga = self.page.find("h2").text

    def __repr__(self):
        return f"""Infor:
        Url: {self.url}
        Nome do Manga: {self.titulo_manga}
        Total de Capitulos: {len(self.list_link)}"""

    def site_connect(self, url):
        'Verifica se o site esta com codigo 200 é retorna um objeto beautifulSoup'
        
        cont_erro = 1
        site = None

        while cont_erro < 11:
            try:
                site = requests.get(url)
                if site.status_code == 200:
                    print("Site Ok")
                    return BeautifulSoup(site.content, 'html.parser')
            except:
                print(f"Tentativa de connectar {cont_erro}")
                cont_erro += 1
        exit()

    def all_link_cap(self):
        'Analiza a pagina é pega todos os links dos capitulos, retorna uma lista.'

        list_link = []
        div_link = self.page.find_all(class_='row lancamento-linha')

        for link in div_link:
            list_link.append(link.find('a').get('href'))
        return list_link

    def down_cap(*lista_link):
        "Recebe uma lista de link da pagina do capitulo."

        self.down.page = None

        if self.verifica_dir_titulo():
            

    def verifica_dir_titulo(self):
        'Verificar se existe um diretorio com nome do titulo do manga'
        titulo_manga = self.titulo_manga.replace(' ','')
        lista_conteudo = os.listdir()
        if titulo_manga in lista_conteudo:
            return True
        else:
            return False


