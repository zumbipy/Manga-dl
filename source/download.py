import os.path
import requests


class Download:
    """ Classe Responsável por Baixa As Imagens"""

    def __init__(self, url, localDeSalva, nomeDoAquivo=''):
        self.url = url
        self.nomeDoAquivo = url.split(
            '/')[-1] if (nomeDoAquivo == '') else nomeDoAquivo
        self.localDeSalva = os.path.join(localDeSalva, self.nomeDoAquivo)

    def ver(self):
        print(
            f'Link Da Imagem: {self.url} \nNome do Arquivo: {self.nomeDoAquivo} \nSalva em: {self.localDeSalva}')

    def salva(self):

        resposta = requests.get(self.url, stream=True)
        if not resposta.ok:
            print("Ocorreu um erro, status:", resposta.status_code)
            return False
        else:
            with open(self.localDeSalva, 'wb') as imagem:
                for dado in resposta.iter_content(1024):
                    if not dado:
                        break

                    imagem.write(dado)

        return True
