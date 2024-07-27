import numpy as np

x = np.array([
            [1, 3 , 7], 
            [4, 11, 21], 
            [42, 8, 9]
            ])

print(f"\nx:\n {x}")



# Indexação booleana em Numpy Arrays
print("\nIndexação booleana em Numpy Arrays:\n")

k = 10; condicao = x > k # Extraindo números maiores que 'k'

print(f"\nCondição (x > {k}):\n {condicao}")
print(f"Elementos maiores que {k}: {x[condicao]}")
print(f"Números de elementos maiores que {k}: {len(x[condicao])}")


condicao = x % 2 == 0 # Extraindo números pares

print(f"\nCondição (x % 2 == 0):\n {condicao}")
print(f"Elementos pares: {x[condicao]}")
print(f"Números de elementos pares: {len(x[condicao])}")
