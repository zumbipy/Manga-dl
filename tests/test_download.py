import pytest
import os.path
import sys

sys.path.append("/home/zumbipy/Projetos/manga-dl/source")

from download import Download


def test_image():
    down = Download()
    down.image(
        "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
    )
    assert "googlelogo_color_272x92dp.png" in os.listdir(".")
    os.remove("googlelogo_color_272x92dp.png")
