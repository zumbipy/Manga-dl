import pytest
import os.path
import sys

sys.path.append("/home/zumbipy/Projetos/manga-dl/source")

from manage import Manage


def test_create_folder():
    Manage().create_folder("tmp", ".")
    assert "tmp" in os.listdir(".")
    os.removedirs("tmp")
