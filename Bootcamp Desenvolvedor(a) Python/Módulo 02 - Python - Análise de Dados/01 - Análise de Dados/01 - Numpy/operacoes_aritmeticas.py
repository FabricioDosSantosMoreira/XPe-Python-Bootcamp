import numpy as np

x = np.ones((2,2))
y = np.eye(2)

print(f"\nx:\n {x}")
print(f"\ny:\n {y}")



# Soma em Numpy Arrays
print("\nSoma em Numpy Arrays:\n")

print(f"Soma de dois arrays: {x + y}")
print(f"Soma com inteiro: {x + 2}") # Broadcasting (soma 2 em todos os elementos de x)



# Subtração em Numpy Arrays
print("\nSubtração em Numpy Arrays:\n")

print(f"Subtração de dois arrays: {x - y}")
print(f"Subtração com inteiro: {x - 2}") # Broadcasting (subtrai 2 em todos os elementos de x)



# Multiplicação em Numpy Arrays
print("\nMultiplicação em Numpy Arrays:\n")

print(f"Multiplicação de dois arrays: {x * y}")
print(f"Multiplicação com inteiro: {x * 2}") # Broadcasting (multiplica 2 em todos os elementos de x)



# Divisão em Numpy Arrays
print("\nDivisão em Numpy Arrays:\n")

print(f"Divisão de dois arrays: {x / y}")
print(f"Divisão com inteiro: {x / 2}") # Broadcasting (divide 2 em todos os elementos de x)
