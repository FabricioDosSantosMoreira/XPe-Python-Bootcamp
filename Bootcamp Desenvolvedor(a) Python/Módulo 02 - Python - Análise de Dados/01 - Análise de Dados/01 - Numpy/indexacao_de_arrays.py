import numpy as np

x =  np.linspace(start=10, stop=100, num=10)

print(f"\nx:\n {x}")
print(f"\nx.shape: {x.shape}")

# Indexação de Numpy Arrays
print("\nIndexação de Numpy Arrays:\n")

print(f"Primeiro elemento: x[0] = {x[0]}")
print(f"Segundo elemento: x[1] = {x[1]}")
print(f"Último elemento: x[9] = {x[9]}")
print(f"Último elemento: x[-1] = {x[-1]}")
print (f"Os dois primeiro elementos: x[0:2] = {x[0:2]}") # Do 0 até 2 - 1 (exclusivo)
print (f"Os dois primeiro elementos: x[:2] = {x[:2]}") # Do 0 até 1 (exclusivo)
print (f"OS dois ultimos elementos: x[-2:] = {x[-2:]}") # Do -1 até -2 

# Reshape de x para 2 linhas e 5 colunas
x = x.reshape(2, 5) 
print(f"\nIndexação após reshape de x:\n")

print(f"x:\n {x}")
print(f"\nx.shape: {x.shape}\n")

print(f"Primeira linha, segunda coluna: {x[0, 1]}")
print(f"Segunda linha, penultima coluna: {x[1, -2]}")
print(f"Última linha, ultima coluna: {x[1, 4]}")
print(f"Última linha, ultima coluna: {x[-1, -1]}")
