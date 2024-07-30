from typing import List

import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Idade dos indivíduos
idades: List[int] = [21, 23, 27, 32, 34, 41, 50, 53, 57, 59, 38, 46, 48, 48, 60]

# Salário dos indivíduos
salarios: List[int] = [1000, 1100, 1250, 1700, 1500, 1980, 2500, 3500, 2200, 4100, 3900, 5100, 5500, 7000, 6500]


# Combinando as listas de idades e salários em um único array bidimensional
dados_salario = np.array([idades, salarios]).T


# Normalizando os dados entre a idade e o salário
standard_scaler = StandardScaler()
dados_normalizados = standard_scaler.fit_transform(dados_salario)


# Criando um modelo de K-Means com 3 clusters
kmeans = KMeans(n_clusters=3, random_state=0)


# Treinando o modelo K-Means com os dados normalizados
kmeans.fit(dados_normalizados)


# Obtendo os centróides dos clusters normalizados
centroides_normalizados = kmeans.cluster_centers_


# Desnormalizando os centróides para a escala original
centroides = standard_scaler.inverse_transform(centroides_normalizados)


# Indicando a qual cluster cada indivíduo pertence
rotulos = kmeans.labels_


# Criando um gráfico de dispersão para visualizar os dados com cores indicando os clusters
grafico1 = px.scatter(x=dados_normalizados[:, 0], y=dados_normalizados[:, 1], color=rotulos,
                      labels={'x': 'Idade (normalizada)', 'y': 'Salário (normalizado)'},
                      title='Clusterização de Idade e Salário (Dados Normalizados)')


# Criando um gráfico de dispersão para mostrar os centróides dos clusters como marcadores
grafico2 = px.scatter(x=centroides_normalizados[:, 0], y=centroides_normalizados[:, 1], 
                      size=[10, 10, 10], symbol=[0, 1, 2], 
                      labels={'x': 'Idade (normalizada)', 'y': 'Salário (normalizado)'},
                      title='Centroides dos Clusters (Dados Normalizados)')


# Criando um gráfico composto combinando os dados dos gráficos 1 e 2
grafico_combinado = go.Figure(data=grafico1.data + grafico2.data)


# Adicionando títulos e rótulos ao gráfico composto
grafico_combinado.update_layout(title='Clusterização K-Means: Idade vs Salário',
                                xaxis_title='Idade (normalizada)',
                                yaxis_title='Salário (normalizado)')


# Mostrando o gráfico composto
grafico_combinado.show()


# Exibindo os centróides desnormalizados
print(f"\nCentroides desnormalizados:\n{centroides}")
