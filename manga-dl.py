import os

from source.download import Download
from source.manage import Manage
from source.unionleitor import UnionLeitor


print(
    f"""
+-----------------------------------------------------------+
|     __  __         Manga Downloand.               _   _   |
|    |  \/  |  __ _   _ _    __ _   __ _   ___   __| | | |  |
|    | |\/| | / _` | | ' \  / _` | / _` | |___| / _` | | |  |
|    |_|  |_| \__,_| |_||_| \__, | \__,_|       \__,_| |_|  |
|                            |___/         Versão: 4.0      |
+-----------------------------------------------------------+
Pasta Atual: {os.path.basename(os.path.abspath(''))}
"""
)

url_manga = input("Digite a URL da Pagina do Manga: ").replace(' ','')  # Remove os espaços.

if url_manga.startswith('https://unionleitor.top/'):
    print("Link Valido Iniciando Analise do conteudo.")
    down = UnionLeitor(url_manga)

    title_folder = down.content['Title']
    chapters_folder = list(down.content['Chapters'].keys())
    chapters_folder.sort()

    Manage().create_folder(title_folder)
    print(f"Criando pasta {title_folder}...")

    for folder in chapters_folder:
        base_dir = os.path.join(title_folder, folder)
        Manage().create_folder(base_dir)
        print(f"    Criando pasta {folder}...")

        for url in down.content['Chapters'][folder]:
            Download().image(url, base_dir)
            print(f"        Download da Imagem {url.split('/')[-1]}" , end='')
            print('\b'*60, end='', flush=True)
