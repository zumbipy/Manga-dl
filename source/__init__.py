dict_url = {
    "Unionleitor": "unionleitor.top",
    "Neoxscan": "neoxscan.com",
}


def is_valido_url(url):
    for link in dict_url.values():
        name_site = url.split('/')
        if len(name_site) < 3:
            return False
        if name_site[2] == link:
            return True
