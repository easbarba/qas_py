from pathlib import Path

class Data:
    """Main data information"""

    def __init__(self):
        self.qas_home = Path.home().joinpath(".config", "qas")
