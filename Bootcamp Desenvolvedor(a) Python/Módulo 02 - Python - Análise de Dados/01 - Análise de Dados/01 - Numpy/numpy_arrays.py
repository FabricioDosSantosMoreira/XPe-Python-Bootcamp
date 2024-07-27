import numpy as np

# Criação de um array unidimencional
print("\nCriando um Numpy Array unidimencional:\n")

l1 = [1, 2, 3]
x1 = np.array(l1, dtype=int) # Dtype determina o tipo dos dados nos arrays

print(f"x1:\n {x1}")
print(f"Shape de x1: {x1.shape}")
print(f"Tipo de x1: {type(x1)}")



# Criação de um array bidimencional, OBS: listas aninhadas[[],[]]
print("\nCriando um Numpy Array bidimencional:\n")

l2 = [[1, 2], [3, 4]]
x2 = np.array(l2, dtype=int)

print(f"x2:\n {x2}")
print(f"Shape de x2: {x2.shape}")
print(f"Tipo de x2: {type(x2)}")



# Criação de um array com apenas 0's
print("\nCriando um Numpy Array somente de 0's:\n")

dimensoes = (2, 2) # Linhas, colunas
x3 = np.zeros(dimensoes, dtype=int)

print(f"x3:\n {x3}")
print(f"Shape de x3: {x3.shape}")
print(f"Tipo de x3: {type(x3)}")



# Criação de um array com apenas 1's
print("\nCriando um Numpy Array somente de 1's:\n")

dimensoes = (3, 2) # Linhas, Colunas
x4 = np.ones(dimensoes)

print(f"x4:\n {x4}")
print(f"Shape de x4: {x4.shape}")
print(f"Tipo de x4: {type(x4)}")



# Criação de Arrays linearmente espaçados (a distância entre os elementos é a mesma)
print("\nCriando um Numpy Array linearmente espaçado:\n")

# Criaçao de valores dentro de um intervalo 
x_min, x_max = 5, 15 # Valores uniformes entre 5 e 15
arary_linear = np.linspace(start=x_min, stop=x_max, num=6)

print(f"Array linear: {arary_linear}")
print(f"Shape do array linear: {arary_linear.shape}")



# Criação de uma matriz identidade (eye)
print("\nCriando uma matriz identidade:\n")

dimensao = 4
matriz_identidade = np.eye(dimensao)

print(f"Matriz identidade:\n {matriz_identidade}")
# OBS: # As matrizes identidades serão quadradas ([2,2], [3,3]...)
print(f"Shape da matriz identidade: {matriz_identidade.shape}")



# Criação de um array com valores aleatórios 
print("\nCriando um Numpy Array com valores aleatórios")

array_aleatorio = np.random.random(size=(2, 7))

print(f"Array aleatório:\n {array_aleatorio}")
print(f"shape do array aleatório: {array_aleatorio.shape}") 
