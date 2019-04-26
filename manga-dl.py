
import sys
from downloadmanga import DownloadManga
from unionmangas import UnioMangas


def siteAceito(url, dic_url):
    for url_aceitos in dic_url.values():
        if url.startswith(url_aceitos):
            return True
    else:
        return False

dic_url = {
    'Union Mangas':'https://unionmangas.top/'
}

if __name__ == "__main__":
    url = input("Digite o Link do site do manga: ")
    if siteAceito(url, dic_url):
        baixaConteudo = DownloadManga(UnioMangas().get(url))
        baixaConteudo.criarPastaTitulo()
        baixaConteudo.criarPastaCapitulo()
        baixaConteudo.downConteudo()
    else:
        print(f"Site {url} não tem suporte.")
