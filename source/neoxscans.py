from requests_html import HTMLSession


class Neoxscans(object):

    def __init__(self, url):
        self.url = url
        self.conteudoDaPagina = self.get()
        self.conteudo = {'url': self.url,
                         'titulo': self.conteudoDaPagina.find('.post-title h1')[0].text,
                         'capitulos': {},
                         }
        self.capitulos()


    def __str__(self):
        return str(self.conteudo)

    def get(self):
        sessao = HTMLSession()
        try:
            requeste = sessao.get(self.url)
            if requeste.ok:
                requeste.html.render(sleep=5)

            else:
                print("Link Invalido")
                return False
        except:
            print("Erro com A pagina!!!")
        return requeste.html

    def capitulos(self):
        listaElemntos = self.conteudoDaPagina.find('.wp-manga-chapter  a')
        for elem in listaElemntos:
            url = list(elem.links)[0]
            self.conteudo['capitulos'].update({elem.text : self.linksImagens(url)})

    @staticmethod
    def linksImagens(url):
        listaUrl = []
        sessao = HTMLSession()
        try:
            requeste = sessao.get(url)
            if requeste.ok:
                listaDeElemetos = requeste.html.find('.wp-manga-chapter-img')
                for elem in listaDeElemetos:
                    listaUrl.append(elem.attrs.get('data-src', False).lstrip())
            else:
                print("Link Do Capilo Invalido")
                return False
        except:
            print("Erro com A pagina do Capitulo!!!")
        return listaUrl
        
        


a = Neoxscans('https://neoxscans.com/manga/doctors-rebirth/')


