from pathlib import Path
import pandas as pd

ROOT_PATH = Path(__file__).parent

print("\nArquivo CSV:\n")

dataframe = pd.read_csv(ROOT_PATH / "temperature.csv")
print(f"\n{dataframe}")



# Indexação
print("\nIndexação:\n")

# Seleção de uma coluna 
print("\nSeleção de uma coluna:")

print(dataframe['temperatura'])



# Seleção de múltiplas colunas 
print("\nSeleção de múltiplas colunas:")

print(dataframe[['temperatura', 'date']])



# Seleção de linhas de uma coluna por índice
print("\nSeleção de linhas de uma colunas:")

print(dataframe.iloc[:, 1]) # [1] = 'temperatura'



# Seleção de linhas de uma coluna por nome
print("\nSeleção de linhas de uma colunas:")

print(dataframe.loc[:, 'classification']) 



# Seleção de linhas de múltiplas colunas por índice
print("\nSeleção de linhas de múltiplas colunas:")

print(dataframe.iloc[:, 1:3])


# Seleção de linhas de múltiplas colunas por nome
print("\nSeleção de linhas de múltiplas colunas:")

print(dataframe.loc[:, ['temperatura', 'classification']])
