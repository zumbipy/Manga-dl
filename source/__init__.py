from source.neoxscans import NeoxScans
from source.unionleitor import UnionLeitor

dict_url = {
    "Union Manga": "unionmangas.top",
    "Union Leitor": "unionleitor.top",
    "Neoxscans": "neoxscans.com"
}


def is_valido_url(url):
    for link in dict_url.values():
        name_site = url.split('/')
        if len(name_site) < 3:
            return False
        if name_site[2] == link:
            return True

