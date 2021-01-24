import os.path


class Diretorio(object):
    """Criar os diretorios e os Organizar"""

    @staticmethod
    def criar(nomeDaPasta, local):
        criarPasta = os.path.join(os.path.abspath(local), nomeDaPasta)
        os.makedirs(criarPasta, exist_ok=True)


Diretorio.criar('rogerio', '/mnt/BAF4F744F4F70185/Projetos/Manga-dl/')