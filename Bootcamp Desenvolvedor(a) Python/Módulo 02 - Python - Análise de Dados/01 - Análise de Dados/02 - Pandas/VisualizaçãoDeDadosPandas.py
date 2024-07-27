import pandas as pd

print ('Arquivo CSV')
df = pd.read_csv("temperature.csv")

df = df.set_index('date') # Setando o índice como datas
print(df, '\n')

# Plot de linhas
#df.plot(style=('-o'), linewidth=2.5, color= '#eb4000', figsize=(10,5), grid=True); # O ; retira uns códigos malucos
# Style define o tipo de traçado
# Linewidth define o tamanho da linha
# Figsize define o tamanho do gráfico
# Grid= True adiciona os grids
# Color define a cor da linha (color='red ou color='#eb4034')


# Plot de barras
#df['classification'].value_counts().plot.bar(figsize=(10,5), rot=0); 

# Também pode ser:
#df.plot(kind=('bar'), figsize=(10,5), rot= 0);

# rot é a rotação dos label do eixo x

# Plot de pizza(pie)
df['classification'].value_counts().plot.pie(autopct='%1.1f%%', shadow= True, figsize= (10,7))