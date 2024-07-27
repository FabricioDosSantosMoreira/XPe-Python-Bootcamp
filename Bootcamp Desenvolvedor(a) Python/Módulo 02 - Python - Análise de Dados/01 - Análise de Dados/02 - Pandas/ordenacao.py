from pathlib import Path

import pandas as pd

ROOT_PATH: Path = Path(__file__).parent

dataframe = pd.read_csv(ROOT_PATH / "temperature.csv")
dataframe = dataframe.set_index('date')

print("\nArquivo CSV:")
print(f"\n{dataframe}")



print("\nOrdenação:\n")

# Ordenação crescente por uma coluna 
print("\nColuna temperatura ordenada de forma crescente:")
print(dataframe.sort_values(by='temperatura'))



# Ordenação crescente por uma coluna 
print("\nColuna classification ordenada de forma crescente:")
print(dataframe.sort_values(by='classification')) # Como é 'classification' é string, ordena de forma alfabética



# Ordenação crescente por múltiplas colunas 
print("\nColunas temperatura e classification ordenadas de forma crescente:")
print(dataframe.sort_values(by=['temperatura', 'classification']))



# Ordenação decrescente por uma coluna
print("\nColuna temperatura ordenada de forma decrescente:")
print(dataframe.sort_values(by='temperatura', ascending=False))



# Ordenação crescente pelo índice
print("\nOrdenação crescente pelo índice(date):")
print(dataframe.sort_index()) # ordena em forma cronológica
