from downloadmanga import DownloadManga

import os


def test_verificarDirTitulo():
    assert DownloadManga.verificarDirTitulo("Pasta") == False

def test_criarPastaTitulo():
    DownloadManga.pastaTitulo = "teste1"
    DownloadManga.criarPastaTitulo(DownloadManga)
    assert DownloadManga.pastaTitulo in os.listdir()
    os.system(f"rmdir {DownloadManga.pastaTitulo}")
