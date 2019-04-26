import pytest
from unionmangas import UnioMangas

def test_get():
    # TODO Criar teste unitario.
    pass

def test_linksCapitulos():
    # TODO Criar teste unitario.
    pass

def test_linkImagens():
    # TODO Criar teste unitario.
    pass

def test_pagina_soup():
    # TODO Criar teste unitario.
    pass

def test_conteudo_dic():
    conteudo_test = {
            #'Titulo': '',
            'LinksCapitulos': '',
            'TotalCapitulos': '',
            'Url': '' 
            }
    conteudo = UnioMangas().get('https://unionmangas.top/manga/tsurezure-children-manga&ot=4301122018')
    assert conteudo.keys() == conteudo_test.keys()