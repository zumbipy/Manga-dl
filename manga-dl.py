import os

from source.download import Download
from source.manage import Manage
from source.unionleitor import UnionLeitor
from source import is_valido_url

versao = "Versão: 4.0.1"

print(f"""
\x1b[38;5;197m+-----------------------------------------------------------+                    \x1b[0m 
\x1b[38;5;198m|     __  __         Manga Downloand.               _   _   |                    \x1b[0m 
\x1b[38;5;199m|    |  \\/  |  __ _   _ _    __ _   __ _   ___   __| | | |  |                   \x1b[0m 
\x1b[38;5;200m|    | |\\/| | / _` | | ' \\  / _` | / _` | |___| / _` | | |  |                  \x1b[0m 
\x1b[38;5;201m|    |_|  |_| \\__,_| |_||_| \\__, | \\__,_|       \\__,_| |_|  |                \x1b[0m 
\x1b[38;5;202m|                            |___/        \x1b[38;5;7m {versao} \x1b[0m \x1b[38;5;203m  | \x1b[0m 
\x1b[38;5;203m+-----------------------------------------------------------+                    \x1b[0m 
Pasta Atual:\x1b[38;5;3m {os.path.basename(os.path.abspath(''))}\x1b[0m
"""
)

url_manga = input("Digite a URL da Pagina do Manga:\x1b[38;5;4m").replace(
    " ", ""
)  # Remove os espaços.
print("\x1b[0m", end="")  # Remove a cor do link do comando acima

if is_valido_url(url_manga):
    print("Link Valido.\n Iniciando Analise do conteudo.")
    down = UnionLeitor(url_manga)

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

    print("\x1b[38;5;9mlink invalido!!! \x1b[0m")
