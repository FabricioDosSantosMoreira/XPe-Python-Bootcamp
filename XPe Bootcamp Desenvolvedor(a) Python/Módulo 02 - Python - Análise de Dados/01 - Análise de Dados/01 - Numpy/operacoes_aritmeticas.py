import numpy as np

x = np.ones((2, 2))
y = np.ones((2, 2)) + np.ones((2, 2))

print(f"\nx:\n {x}")
print(f"\ny:\n {y}")


# Soma em Numpy Arrays
print(f"\nSoma de dois arrays:\n {x + y}")
print(f"\nSoma com inteiro:\n {x + 2}") # Broadcasting (soma 2 em todos os elementos de x)


# Subtração em Numpy Arrays
print(f"\nSubtração de dois arrays:\n {x - y}")
print(f"\nSubtração com inteiro:\n {x - 2}") # Broadcasting (subtrai 2 em todos os elementos de x)


# Multiplicação em Numpy Arrays
print(f"\nMultiplicação de dois arrays:\n {x * y}")
print(f"\nMultiplicação com inteiro:\n {x * 2}") # Broadcasting (multiplica 2 em todos os elementos de x)


# Divisão em Numpy Arrays
print(f"\nDivisão de dois arrays:\n {x / y}")
print(f"\nDivisão com inteiro:\n {x / 2}") # Broadcasting (divide 2 em todos os elementos de x)
