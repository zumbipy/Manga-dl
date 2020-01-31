import os.path


class Manage:
    """create a folder with your chosen name and location"""

    def create_folder(self, name, base_path=""):
        folder = os.path.join(base_path, name)
        os.makedirs(folder, exist_ok=True)
