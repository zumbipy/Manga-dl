import os
import os.path
import requests

class DownloadManga(object):
    "Esta class é responsavel por gerenciar as pastas e baixa as imagens"

    def __init__(self, dicionario_conteudo):
        self.pastaTitulo = dicionario_conteudo['Titulo'].replace(" ", "_")
        self.conteudo = dicionario_conteudo
        self.titulo = self.conteudo.get("Titulo", None)
        self.totalCapitulos = self.conteudo.get('TotalCapitulos', None)
        self.url = self.conteudo.get('Url', None)
        self.linksCapitulos = self.conteudo['LinksCapitulos']
    
    def criarPastaTitulo(self):
        "Criar a pasta raiz com Titulo do manga."

        if self.verificarDirTitulo(self.pastaTitulo):
            return f'Pasta {self.pastaTitulo} já existe.'
        else:
            os.mkdir(self.pastaTitulo)
            return f'Pasta {self.pastaTitulo} foi criada.'

    
    def criarPastaCapitulo(self):
        "Criar as pastas dos capitulos dos mangas."

        os.chdir(self.pastaTitulo)  # Entra na pasta.

        lista_chaves = list(self.conteudo['LinksCapitulos'].keys())
        lista_chaves.sort()

        for pasta in lista_chaves:
            link = self.conteudo['LinksCapitulos'][pasta]
            if self.verificarDirTitulo(pasta):
                print(f'pasta {pasta} já existe')
            else:
                os.mkdir(pasta)
                os.chdir(pasta)
                for img in link:
                    self.downloadImagem(img)
                os.chdir('..')
                
    @staticmethod
    def verificarDirTitulo(nomePasta):
        "Verifica se pasta principal do downloand existe."
        
        listaPasta = os.listdir()
        if nomePasta in listaPasta:
            return True
        else: 
            return False
    
    @staticmethod
    def downloadImagem(url):
        "Recebe o link do capitulo e baixa as imagens. "
        *_ , nome = url.split("/")
        imagem = requests.get(url)
        if imagem.status_code == 200:
            with open(nome, 'wb') as f:
                f.write(imagem.content)
            
