dict_url = {
    "Union Manga": "unionmangas.top",
    "Union Leitor": "unionleitor.top",
    
}


def is_valido_url(url):
    for link in dict_url.values():
        name_site = url.split('/')
        if len(name_site) < 3:
            return False
        if name_site[2] == link:
            return True
