from Dmanga import DownloadManga

url = 'http://unionmangas.site/manga/world-trigger'
site = DownloadManga(url)

print(site)
links = site.list_link
links.reverse()

for l in links:
    print(l)
