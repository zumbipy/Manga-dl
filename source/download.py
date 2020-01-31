import os.path
import requests

from tqdm import tqdm


class Download:
    """ class responsible for donwload as images"""

    def image(self, url, path=''):
        """Donwload image"""

        *_, image_name = url.split("/")
        image = requests.get(url, stream=True)

        file_size = int(image.headers.get('content-length'))
        chunk_size = 1024  # 1 MB
        num_bars = int(file_size / chunk_size)

        if image.status_code == 200:
            with open(os.path.join(path, image_name), "wb") as f:
                for chuck in tqdm(image.iter_content(chunk_size=chunk_size), total=num_bars, unit='KB', desc=f'        Download da Imagem {image_name}'):
                    f.write(chuck)
        else:
            return f"Erro Download {url}"
