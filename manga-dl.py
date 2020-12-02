import os

from source.download import Download
from source.manage import Manage
from source.unionleitor import UnionLeitor
from source.neoxscans import NeoxScans
from source import is_valido_url

versao = "Versão: 4.0.1"

print(f"""
+-----------------------------------------------------------+                     
|     __  __         Manga Download.               _   _    |                     
|    |  \/  |  __ _   _ _    __ _   __ _   ___   __| | | |  |                    
|    | |\/| | / _` | | ' \  / _` | / _` | |___| / _` | | |  |                   
|    |_|  |_| \__,_| |_||_| \__, | \__,_|       \__,_| |_|  |                 
|                            |___/         Versão: 4.0.2    |  
+-----------------------------------------------------------+  
Pasta Atual: {os.path.basename(os.path.abspath(''))}
"""
)

url_manga = input("Digite a URL da Pagina do Manga:\x1b[38;5;4m").replace(" ", "")  # Remove os espaços.
print("\x1b[0m", end="")  # Remove a cor do link do comando acima

if is_valido_url(url_manga):
    print("Iniciando Analise do conteudo.")

    if "https://neoxscans.com/" in url_manga:
        down = NeoxScans(url_manga)
        print("neoxscans")
    elif "unionleitor.top" in url_manga:
        down = UnionLeitor(url_manga)
        print("unionleitor")
    else:
        down = UnionLeitor(url_manga)
        print("UnionMnaga")

    
    title_folder = down.content["Title"]
    chapters_folder = list(down.content["Chapters"].keys())
    chapters_folder.sort()

    Manage().create_folder(title_folder)
    print(f"Criando pasta {title_folder}...")

    for folder in chapters_folder:
        base_dir = os.path.join(title_folder, folder)
        Manage().create_folder(base_dir)
        print(f"    Criando pasta {folder}...")

        for url in down.content["Chapters"][folder]:
            Download().image(url, base_dir)

else:

    print("link invalido!!!")
