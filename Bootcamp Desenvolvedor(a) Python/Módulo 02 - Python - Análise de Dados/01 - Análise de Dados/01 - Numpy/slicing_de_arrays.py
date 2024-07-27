import numpy as np

x =  np.linspace(start=10, stop=100, num=10).reshape(2, 5)

print(f"\nx:\n {x}")
print(f"\nx.shape: {x.shape}")



# Slicing de Numpy Arrays(SubArrays)
print("\nSlicing de Numpy Arrays:\n")

print(f"Primeira linha inteira: {x[0, :]}")
print(f"Primeira linha, segunda a quarta coluna: {x[0, 1:4]}")
# OBS: [:, [-1]] preserva as dimensões, se fosse [:, -1] coloca tudo em linha 
print(f"Penúltima coluna inteira:\n {x[:, [-1]]}") 



# NOTE: Compartilhamento de memória em SubArrays
print("\nExemplo de array com compartilhamento de memória:\n")

array_original = np.array([1, 2, 3, 4, 5])

print(f"\nArray original antes: {array_original}")

# Criando um SubArray do array original
array_compartilhado = array_original[:3]
print(f"SubArray do Array original: {array_compartilhado}")

array_compartilhado[0] = 192 # Alterar o valor de 'array_compartilhado[0]' altera 'array_original[0]' também!
print(f"Array original depois: {array_original}")



# Resolvendo o compartilhamento de memória em SubArrays:
print("\nExemplo de array sem compartilhamento de memória:\n")

array_original = np.array([1, 2, 3, 4, 5])


print(f"Array original antes: {array_original}")

# # Usando 'copy()' para criar uma cópia independente
array_compartilhado = array_original[:3].copy()
print(f"SubArray do Array original: {array_compartilhado}")

array_compartilhado[0] = 192 # Agora alterar o valor de 'array_compartilhado[0]' não altera 'array_original[0]'
print(f"Array original depois: {array_original}")
