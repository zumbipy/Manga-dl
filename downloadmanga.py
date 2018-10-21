import os
import os.path
import requests

class DownloadManga(object):
    "Esta class é responsavel por gerenciar as pastas e baixa as imagens"

    def __init__(self, dicionario_conteudo):
        self.dic_conteudo = dicionario_conteudo
        self.pasta_principal = dicionario_conteudo['Titulo'].replace(" ", "_")
    
    def criar_dir_principal(self):
        if self.verificar_dir_existe(self.pasta_principal):
            return f'Pasta {self.pasta_principal} já foi criada.'
        else:
            os.mkdir(self.pasta_principal)
            return f'Pasta {self.pasta_principal} foi criada.'

    
    def criar_pasta_cap(self):
        os.chdir(self.pasta_principal)  # Entra na pasta.

        lista_chaves = list(self.dic_conteudo['LinksCapitulos'].keys())
        lista_chaves.sort()

        for pasta in lista_chaves:
            link = self.dic_conteudo['LinksCapitulos'][pasta]
            if self.verificar_dir_existe(pasta):
                print(f'pasta {pasta} já existe')
            else:
                os.mkdir(pasta)
                os.chdir(pasta)
                for img in link:
                    self.download_img(img)
                os.chdir('..')
                

    def verificar_dir_existe(self, Nome_pasta):
        lista_pasta = os.listdir()
        if Nome_pasta in lista_pasta:
            return True
        else: 
            return False
    
    
    def download_img(self, url):
        *_ , nome = url.split("/")
        imagem = requests.get(url)
        if imagem.status_code == 200:
            with open(nome, 'wb') as f:
                f.write(imagem.content)
            
