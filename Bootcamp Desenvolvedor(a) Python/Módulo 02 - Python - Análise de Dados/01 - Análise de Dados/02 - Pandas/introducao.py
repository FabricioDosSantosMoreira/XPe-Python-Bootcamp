from pathlib import Path
import pandas as pd

ROOT_PATH = Path(__file__).parent

# Leitura de dados CSV
dataframe = pd.read_csv(ROOT_PATH / "temperature.csv")

print("\nArquivo CSV:")
print(f"\n{dataframe}")


 
# Leitura de dados Excel
excel_file = pd.ExcelFile(ROOT_PATH / "temperature.xlsx") # Leitura do arquivo todo

dataframe = pd.read_excel(excel_file, sheet_name='Sheet1') # Leitura da primeira aba (Sheet1)

print("\nPrimeira aba do arquivo Excel:")
print(dataframe)



# Visualizando as primeiras n linhas
n = 2
print ("\nPrimeiras linhas:")
print(dataframe.head(n))



# Visualizando as últimas n linhas
n = 2
print ("\nÚltimas linhas:")
print(dataframe.tail(n))



# Tipo dos dados
print("\nTipo dos dados(dtypes):")
print(dataframe.dtypes)



# Estatísticas básicas
print("\nEstatísticas básicas:") 
print(dataframe.describe())



# dataframe info
print("\ndataframe info:") 
print(dataframe.info())



# Nomes das colunas 
print("\nNomes das colunas") 
print(dataframe.columns)



# Renomear os nomes das colunas
dataframe.columns = ['coluna1', 'coluna2', 'coluna3']
print("\nRenomeando as colunas:") 
print(dataframe.columns)
