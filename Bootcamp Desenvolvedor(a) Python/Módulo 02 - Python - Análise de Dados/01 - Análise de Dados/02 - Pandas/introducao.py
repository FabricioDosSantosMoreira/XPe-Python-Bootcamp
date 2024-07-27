from pathlib import Path
import pandas as pd

ROOT_PATH = Path(__file__).parent

# Leitura de dados CSV
print("\nArquivo CSV:\n")

dataframe = pd.read_csv(ROOT_PATH / "temperature.csv")
print(f"\n{dataframe}")


 
# Leitura de dados Excel

# Leitura do arquivo todo
excel_file = pd.ExcelFile(ROOT_PATH / "temperature.xlsx")



# Leitura da primeira aba (Sheet1)
print("\nPrimeira aba do arquivo Excel:")
dataFrame = pd.read_excel(excel_file, sheet_name='Sheet1')
print(dataFrame)



# Visualizando as primeiras n linhas
n = 2
print ("\nPrimeiras linhas:")
print(dataFrame.head(n))



# Visualizando as últimas n linhas
n = 2
print ("\nÚltimas linhas:")
print(dataFrame.tail(n))



# Tipo dos dados
print("\nTipo dos dados(dtypes):")
print(dataFrame.dtypes)



# Estatísticas básicas
print("\nEstatísticas básicas:") 
print(dataFrame.describe())



# dataframe info
print("\ndataframe info:") 
print(dataFrame.info())



# Nomes das colunas 
print("\nNomes das colunas") 
print(dataFrame.columns)



# Renomear os nomes das colunas
dataFrame.columns = ['coluna1', 'coluna2', 'coluna3']
print("\nRenomeando as colunas:") 
print(dataFrame.columns)
