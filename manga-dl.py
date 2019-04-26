
import sys
import os.path
from downloadmanga import DownloadManga
from unionmangas import UnioMangas

print(f"""
+-----------------------------------------------------------+
|     __  __         Downloand de Mangas.           _   _   |
|    |  \/  |  __ _   _ _    __ _   __ _   ___   __| | | |  |
|    | |\/| | / _` | | ' \  / _` | / _` | |___| / _` | | |  |
|    |_|  |_| \__,_| |_||_| \__, | \__,_|       \__,_| |_|  |
|                            |___/         Versão: 3.0 beta |
+-----------------------------------------------------------+
Pasta Atual: {os.path.basename(os.path.abspath(''))}
""")

url_manga = input("Digite a URL da Pagina do Manga: ").replace(' ','')  # Remove os espaços.

# Verifica se a Url é aceita pelo programa.
if DownloadManga.url_valido(url_manga):
    print(f"URL é valido...")
    print("\nComeçando o processo...")
else:
    print("URL invalida!!!")
    sys.exit()  # Para o programa se a url for invalida.

conteudo = UnioMangas().get(url_manga)  # Analiza a Url e retorna um dicionario com todo o conteudo.
