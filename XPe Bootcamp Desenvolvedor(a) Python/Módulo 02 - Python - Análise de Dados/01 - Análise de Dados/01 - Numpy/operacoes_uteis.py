import numpy as np

x = np.array([[1, 3 , 7], 
             [4, 11, 21], 
             [42, 8, 9]])

print(f"\nx:\n {x}")


# 'reshape()' transforma a matriz em um vetor coluna
print(f"\nMatriz para coluna (3 por 3 para 9 por 1):\n {x.reshape(9, 1)}")


# 'x.T' transpõe a matriz
print(f"\nMatriz transposta:\n {x.T}")


# 'np.sum()' soma em um determinado eixo(0 = linhas, 1 = colunas)
print(f"\nSoma de todos os elementos de x: {np.sum(x)}")
print(f"Soma de x ao longo do eixo 0: {np.sum(x, axis=0)}")
print(f"Soma de x ao longo do eixo 1: {np.sum(x, axis=1)}")


# 'np.mean()' média de um determinado eixo(0 = linhas, 1 = colunas)
print(f"\nMédia de todos os elementos de x: {np.mean(x)}") 
print(f"Média de x ao longo do eixo 0: {np.mean(x, axis=0)}")
print(f"Média de x ao longo do eixo 1: {np.mean(x, axis=1)}")


# 'np.median()' mediana de um determinado eixo(0 = linhas, 1 = colunas)
print(f"\nMediana de todos os elementos de x: {np.median(x)}") 
print(f"Mediana de x ao longo do eixo 0: {np.median(x, axis=0)}")
print(f"Mediana de x ao longo do eixo 1: {np.median(x, axis=1)}")


# 'np.where()' identificação dos indices onde uma condição é atendida, usado com indexação booleana 
condicao = x % 2 == 0 # Extrai números pares

eixo_x, eixo_y = np.where(condicao)

print("\nUsando np.where() para extrair os índices de uma condição")
print(f"Índice x (eixo 0): {eixo_x}")
print(f"Índice y (eixo 1): {eixo_y}")


# Indexação booleana e slicing: seleciona as linhas de x que possuem algum número par 
condicao = x % 2 == 0 # Extrai números pares

eixo_y = np.where(np.sum(condicao, axis=1))[0] # Se houver alguma condição True a soma será > 0

print(f"\nÍndice das linhas que possuem números pares: {eixo_y}")
print(f"Linhas que possuem números pares:\n {x[eixo_y, :]}")
