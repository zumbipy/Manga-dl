from downloadmanga import DownloadManga
from unionmangas import UnioMangas

url = 'http://unionmangas.site/manga/no-doubt-in-us'

manga_pagina = UnioMangas(url)

dic_conteudo = manga_pagina()

programa = DownloadManga(dic_conteudo)
programa.criar_dir_principal()
programa.criar_pasta_cap()
