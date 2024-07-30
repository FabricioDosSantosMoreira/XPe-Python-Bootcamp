from pathlib import Path

import pandas as pd

ROOT_PATH: Path = Path(__file__).parent

dataframe = pd.read_csv(ROOT_PATH / "temperature.csv")
dataframe['date'] = pd.to_datetime(dataframe['date']) # Transformando 'dataframe['date']' para datetime
dataframe = dataframe.set_index('date') # Setando o índice

print("\nArquivo CSV:")
print(f"\n{dataframe}")
print(f"\n{dataframe.dtypes}")


condicao = dataframe['temperatura'] >= 25 # Seleção de exemplos acima de 25 graus
print(f"\nDataframe com temperatura >= 25:\n{dataframe[condicao]}")


print(f"\nDataframe com entradas até março de 2020:\n")
print(dataframe[dataframe.index <= '2020-03-01'])


print(f"\nDataframe com entradas até março de 2020 e slice na coluna ['classification']:\n")
print(dataframe.loc[dataframe.index <= '2020-03-01', ['classification']])
