from typing import List

import matplotlib.pyplot as plt
import numpy as np

# Dados
x: List[int] = [-1., -0.77777778, -0.55555556, -0.33333333, -0.11111111, 
    0.11111111, 0.33333333, 0.55555556, 0.77777778, 1.]

y: List[int] = [-1.13956201, -0.57177999, -0.21697033, 0.5425699, 0.49406657, 
     1.14972239, 1.64228553, 2.1749824, 2.64773614, 2.95684202]


print(f"\nx:\n {x}")
print(f"\ny:\n {y}")


# Iremos estimar uma função linear(y = ax + b)
# Ou seja, devemos achar quais os valores de a e b que melhor representam o dados
# Os valores reais de (a, b) são (2, 1)


# Transformando para Numpy Array e vetor coluna
x, y = np.array(x).reshape(-1, 1), np.array(y).reshape(-1, 1)


# Adicionando bias(estimar o termo b)
X = np.hstack((x, np.ones(x.shape)))


# Estimando a e b
beta = np.linalg.pinv(X).dot(y)
print(f"a estimado: {beta[0][0]}")
print(f"b estimado: {beta[1][0]}")


# Plotando os dados usando o matplotlib
plt.figure(figsize=(10, 5)) # Define o tamanho da figura/janela

plt.plot(x, y, "o", label="Dados Originais") # Plot do tipo scatterplot

plt.plot(x, X.dot(beta), label="Regressão Linear") # Linha de regressão linear

plt.legend() # Expõe o label/legenda do gráfico

plt.xlabel("x") # Define o nome do eixo x

plt.ylabel("y") # Define o nome do eixo y

plt.title("Regressão Linear com Numpy") # Define o título do gráfico

plt.grid() # Define o grid

plt.show() # Mostra o gráfico
