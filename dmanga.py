
import sys
from downloadmanga import DownloadManga
from unionmangas import UnioMangas


if __name__ == "__main__":

    while True:
        url = input("Digite a URL(Link) do capitulo do manga: ")
        if 'https://unionmangas.top/' in url:
            break
        else:
            print("URL invalida. ")
            exit()

    baixaConteudo = DownloadManga(UnioMangas().get(url))
    baixaConteudo.criarPastaTitulo()
    baixaConteudo.criarPastaCapitulo()
    baixaConteudo.downConteudo()
