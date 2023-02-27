from .data import Data

class Configs:
    def __init__(self, data: object = Data()):
        self.data = data

    def filenames(self) -> dict:
        return [str(x.name) for x in self.data.qas_home.iterdir()]
