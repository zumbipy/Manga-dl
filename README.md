# Manga Download - manga-dl
## Descrição:

> Programa via cli para download de capitulos de mangas.  
> O programa valida o link é depois criar uma pasta com Titulo do manga e dentro da criar uma pasta para cada capitulo e por fim baixa as imagens.


**Depedencias:**

    pip install bs4 requests tqdm

Ou

    poetry install

> Exercutando o Programa:  
> Vá ate a pasta do programa e rode o arquivo manga-dl.py  


```bash
python manga-dl.py 
+-----------------------------------------------------------+
|     __  __         Manga Downloand.               _   _   |
|    |  \/  |  __ _   _ _    __ _   __ _   ___   __| | | |  |
|    | |\/| | / _` | | ' \  / _` | / _` | |___| / _` | | |  |
|    |_|  |_| \__,_| |_||_| \__, | \__,_|       \__,_| |_|  |
|                            |___/         Versão: 4.0      |
+-----------------------------------------------------------+
Pasta Atual: Manga-dl
```

> Agora coloca a Url(link) da pagina onde esta todos os capitulos do manda.

```bash
Digite a URL da Pagina do Manga: https://unionleitor.top/perfil-manga/yakedo-shoujo 
```

```bash

Link Valido.
 Iniciando Analise do conteudo.
Criando pasta Yakedo Shoujo...
    Criando pasta Cap. 01...
        Download da Imagem banner_scan.png: 222KB [00:00, 754.81KB/s]     
        Download da Imagem banner_forum.png: 516KB [00:00, 936.72KB/s]    
        ....
        Download da Imagem 033.jpg: 1034KB [00:00, 1082.97KB/s]           
    Criando pasta Cap. 02...
        Download da Imagem banner_scan.png: 222KB [00:00, 1306.71KB/s]    
        Download da Imagem banner_forum.png: 516KB [00:00, 1165.18KB/s]   
        Download da Imagem 01.jpg: 488KB [00:00, 1101.92KB/s]             
        Download da Imagem 02.jpg: 464KB [00:00, 1144.70KB/s]             
        Download da Imagem 03.jpg: 638KB [00:00, 932.44KB/s]              
        ....            
        Download da Imagem 39.jpg: 1034KB [00:00, 1111.11KB/s]            
    Criando pasta Cap. 03...
        ...

```
> **Sites  Valido:**  
> https://unionleitor.top/