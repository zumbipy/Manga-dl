import requests
import re
from bs4 import BeautifulSoup

class UnioMangas():
    """Este modulo usa um link de uma pagina de manga do site uniomangas e converte
    pra uma dicionario."""

    def get(self, url):
        "Recebe url e rertona um Dict()."

        self.__soup = self.__pagina_soup(url)
        print("Analisando link isso pode demorar alguns minutos.")
        self.__Titulo = self.__soup.h2.text

        self.conteudo = {
            'Titulo': self.__Titulo,
            'LinksCapitulos': self.__linksCapitulos(),
            'TotalCapitulos': self.totalCapitulos,
            'Url': url
            }
        
        return self.conteudo

    def __linksCapitulos(self):
        "Criar uma Dicionario {'Numero Do Capitulo': ['Link Da Imagem']}"

        dic = {}

        lista_cap = self.__soup.find_all('a', string=re.compile("Cap. "))
        self.totalCapitulos = len(lista_cap)

        for link in lista_cap:
            dic[link.text] = self.__linkImagens(link.get('href'))

        return dic
    
    def __linkImagens(self, url):
        "Recebe uma Url da pagana do capitilo é cria um lista de links das imagens"
        img_list =[]
        soup = self.__pagina_soup(url)
        lista_link = soup.find_all('img')

        for link_img in lista_link:
            img_list.append(link_img.get('src'))

        return img_list
    
    @staticmethod
    def __pagina_soup(url):
        tentativas = 1
        while tentativas <= 10:
            try:
                return BeautifulSoup(requests.get(url).content, 'html.parser')
            except:
                print(f"Tentativa de connectar {tentativas}")
                tentativas += 1
        print("Error Url com problema ou sem internet ...")
        exit()
