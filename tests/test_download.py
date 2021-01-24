import os.path
from source.download import Download


def test_downlad_image():
    Download().image('https://uploads.toptal.io/blog/image/252/toptal-blog-image-1389090346415.png', '/home/zumbipy/Projetos/Manga-dl/tests')
    assert 'toptal-blog-image-1389090346415.png' in os.listdir('/home/zumbipy/Projetos/Manga-dl/tests')
    os.remove('/home/zumbipy/Projetos/Manga-dl/tests/toptal-blog-image-1389090346415.png')
    