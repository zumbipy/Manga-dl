import requests
import re
from bs4 import BeautifulSoup

class UnioMangas(object):
    """Este modulo usa um link de uma pagina de manga do site uniomangas e converte
    pra uma dicionario."""

    def __init__(self, url):
        self.soup = self.pagina_soup(url)
        self.Titulo = self.soup.h2.text

        self.dic_conteudo = {
            'Titulo': self.Titulo,
            'LinksCapitulos': self.lista_capitulos(),
            'TotalCapitulos': self.Total_cap,
            }
    
    def __call__(self):
        return self.dic_conteudo
    
    def lista_capitulos(self):
        lista_cap = self.soup.find_all('a', string=re.compile("Cap. "))
        self.Total_cap = len(lista_cap)
        dic = {}

        for link in lista_cap:
            dic[link.text] = self.lista_img(link.get('href'))

        return dic

    def lista_img(self, url):
        img_list =[]
        soup = self.pagina_soup(url)
        lista_link = soup.find_all('img')

        for link_img in lista_link:
            img_list.append(link_img.get('src'))

        return img_list
    
    def pagina_soup(self, url):
        tentativas = 1
        while tentativas <= 10:
            try:
                return BeautifulSoup(requests.get(url).content, 'html.parser')
            except:
                print(f"Tentativa de connectar {tentativas}")
                tentativas += 1
        print("Ops Ocorreu um erro o programa foi finalizado.")
        exit()