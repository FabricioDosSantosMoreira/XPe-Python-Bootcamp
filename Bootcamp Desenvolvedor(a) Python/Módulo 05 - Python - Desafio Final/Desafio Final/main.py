from pathlib import Path
from typing import List

import matplotlib.pyplot as plt
import pandas as pd

from models.api_model import api_predicted_salary
from models.my_model import my_predicted_salary


class Main():

    def __init__(self) -> None:

        self.ROOT_PATH: Path = Path(__file__).parent
        self.DATAFRAME = pd.read_csv(self.ROOT_PATH / "data/salary.csv")

    def run(self) -> None:
        api_predicted_values: List[float] = api_predicted_salary(self.DATAFRAME)
        my_predicted_values: List[float] = my_predicted_salary(self.DATAFRAME)

        print("\n\n", api_predicted_values)
        print("\n\n", my_predicted_values)

        if api_predicted_values is None:
            raise Exception("Erro na API!")

        # Criando um gráfico de barras para comparação
        x = range(len(api_predicted_values))  # Índices dos valores
        width = 0.35  # Largura das barras

        fig, ax = plt.subplots()

        bars1 = ax.bar(x, api_predicted_values, width, label="API Predicted Salary")
        bars2 = ax.bar([i + width for i in x], my_predicted_values, width, label="My Predicted Salary") 

        # Adicionando labels e título
        ax.set_xlabel("Index")
        ax.set_ylabel("Salary")
        ax.set_title("Comparison of Predicted Salaries")
        ax.set_xticks([i + width / 2 for i in x])
        ax.set_xticklabels([i for i in x])
        ax.legend()

        # Mostrar gráfico
        plt.show()


if __name__ == "__main__":
    app = Main()
    app.run()
