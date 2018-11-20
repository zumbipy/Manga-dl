from downloadmanga import DownloadManga
from unionmangas import UnioMangas


if __name__ == "__main__":
    url = 'http://unionmangas.top/manga/charlotte-the-4-koma-seshun-o-kakenukero&ot=1542683993'

    baixaComteudo = DownloadManga(UnioMangas().get(url))
    baixaComteudo.criarPastaTitulo()
    baixaComteudo.criarPastaCapitulo()
