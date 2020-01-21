# Manga Download - manga-dl

### Descrição:

Programa via cli para download de capitulos de mangas.
O programa valida o link é depois criar uma pasta com Titulo do manga e dentro da
criar uma pasta para cada capitulo e por fim baixa as imagens.

Depedencias:
> pip install bs4  
> pip install requests
> 
Ou
> pipenv install

Exercutando o Programa:
```
>>> python manga-dl.py
>>> 
>>> +-----------------------------------------------------------+
>>> |     __  __         Downloand de Mangas.           _   _   |
>>> |    |  \/  |  __ _   _ _    __ _   __ _   ___   __| | | |  |
>>> |    | |\/| | / _` | | ' \  / _` | / _` | |___| / _` | | |  |
>>> |    |_|  |_| \__,_| |_||_| \__, | \__,_|       \__,_| |_|  |
>>> |                            |___/         Versão: 3.0 beta |
>>> +-----------------------------------------------------------+
>>> Pasta Atual: Dmanga
>>> 
>>> Digite a URL da Pagina do Manga: https://unionmangas.top/manga/level-up
>>> URL é valido...
>>> 
>>> Começando o processo...
>>> Analisando link isso pode demorar alguns minutos.
>>> Pasta Level_Up foi criada.
>>> Pasta Cap. 01 foi criada.
>>> Iniciando Donwload...
>>>     Cap. 01
>>>         banner_scan.png concluido.
>>>         00.jpg concluido.
>>>         01.jpg concluido.
>>>         ....
>>>         29.jpg concluido.
>>>         30.jpg concluido.
>>> Download Completo
>>> 
```

## Sites Suportados:
|           Site          | Status |
| :---------------------- | :----: |
| https://unionleitor.top/ |   ok   |
