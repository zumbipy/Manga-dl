import os.path
import requests


class Download:
    """ class responsible for donwload as images"""

    def image(self, url, path=''):
        """Donwload image"""

        *_, image_name = url.split("/")
        image = requests.get(url, stream=True)

        if image.status_code == 200:
            with open(os.path.join(path, image_name), "wb") as f:
                for chuck in image.iter_content(1024):
                    f.write(chuck)
        else:
            return f"Erro Download {url}"
