from pathlib import Path

import pandas as pd

ROOT_PATH: Path= Path(__file__).parent

dataframe = pd.read_csv(ROOT_PATH / "temperature.csv")
dataframe = dataframe.set_index('date') # Setando o índice como 'date'

print("\nArquivo CSV:")
print(f"\n{dataframe}")



# 'groupby()' agrupa valores únicos de uma ou mais colunas e a média delas
print(f"\nMédia de cada classification:")
print(dataframe.groupby(by='classification').mean()) # É possível usar .sum .max, etc



# 'drop()' remove uma coluna específica
dataframe_dropped = dataframe.drop('temperatura', axis=1)
print(f"\nRemovendo a coluna temperatura:\n{dataframe_dropped}")



# 'copy()' copia o dataframe(evita compartilhamento de memória) 
# OBS: Sem o 'copy()', operações inplace em 'dataframe_copy' também altera 'dataframe'
dataframe_copy = dataframe.copy()



# Argumento inplace
# O argumento inplace aplica a tranformação no próprio objeto
# inplace=False (retorna uma cópia do objeto com a transformação)
# inplace=True (aplica a transformação no próprio objeto)

dataframe_copy.drop('temperatura', axis=1, inplace=False) # Sem o inplace, dataframe_copy continua o mesmo
print("\ndataframe_copy:") 
# OBS: a mudança só seria visível se atribuisse uma variável. 
# Ex: dummy = dataframe_copy.drop('temperatura', axis=1, inplace=False)
# print(dummy)
print(dataframe_copy) 

dataframe_copy.drop('temperatura', axis=1, inplace=True) # Com o inplace, dataframe_copy é alterado
print("\ndataframe_copy:")
print(dataframe_copy)
