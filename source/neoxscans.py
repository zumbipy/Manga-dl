from requests_html import HTMLSession
from bs4 import BeautifulSoup


class Neoxscans(object):
    # Uma Classe que recebe um link e retorna um Dicionario.
    # {
    #     'titulo': 'Nome do Manga Completo',
    #     'imgDaCapa': 'Url da Imagem da capa',
    #     'capitulos': {
    #         'cap01':['Links das Imagens do Capitlo'],
    #         'cap02':['Links das Imagens do Capitlo'],
    #         ....,
    #         'cap100':['Links das Imagens do Capitlo'],
    #     'url': 'link Completo da Pagina do Manga'
    #     }

    # }

    def __init__(self, urlPagina):
        self.content = BeautifulSoup(urlPagina, "html.parser")
        self.dictConteudo = {}

        self.titulo = self.title()

    def __str__(self):
        return str(self.dictConteudo)

    def title(self):
        extairTitulo = self.content.h1.getText().strip()

        titulo = {"titulo": extairTitulo}
        self.dictConteudo.update(titulo)

    def imgDaCapa(self, HtmlContent):
        pass

    def listCap():
        pass

    def get(self, url):
        pass


with open("./source/neoxscrans.html") as f:
    html = f.read()

neox = Neoxscans(html)
print(neox)
