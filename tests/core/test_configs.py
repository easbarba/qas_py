from qas.core.configs import Configs
import pytest
from pathlib import Path

class FakeData:
    def __init__(self):
        self.qas_home = Path(__file__).parent.parent.joinpath('DATA')


configs = Configs(data=FakeData())

def test_filenames():
    files = ['empty_config.json', 'broken_link.json', 'misc.json', 'etc.json']

    assert files.sort() == configs.filenames().sort()
