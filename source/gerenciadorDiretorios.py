import os.path


class Diretorio(object):
    """Criar os diretorios e os Organizar"""

    @staticmethod
    def criar(nomeDaPasta, local):
        criarPasta = os.path.join(local, nomeDaPasta)
        os.makedirs(criarPasta, exist_ok=True)
