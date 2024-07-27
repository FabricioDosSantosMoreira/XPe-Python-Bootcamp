import pandas as pd
import os

from pathlib import Path
from handlers.interface_handler import InterfaceHandler
from interface.interface import Interface





class Main():

    def __init__(self) -> None:
        self.is_running: bool = True

        self.on_init()


    def on_init(self) -> None:
        self.interface_handler = InterfaceHandler(self)
        self.interface = Interface(self)

        self.ROOT_PATH: Path = Path(__file__).parent
        self.CSV_PATH: Path = self.ROOT_PATH / "data/bike-sharing.csv"

        self.CSV_NAME: str = os.path.basename(self.CSV_PATH)

        self.df: pd.DataFrame = pd.read_csv(self.CSV_PATH).set_index('datetime')

    
    def run(self) -> None:
        while self.is_running:

            self.interface.menu()


    def quit(self) -> None:
        self.is_running = False
        quit()


if __name__ == "__main__":
    app = Main()
    app.run()
