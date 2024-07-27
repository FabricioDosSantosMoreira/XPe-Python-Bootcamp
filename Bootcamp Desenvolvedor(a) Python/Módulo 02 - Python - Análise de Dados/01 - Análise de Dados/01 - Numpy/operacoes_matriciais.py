import numpy as np

x = np.ones((2,2))
y = np.eye(2)

print(f"\nx:\n {x}")
print(f"\ny:\n {y}")



# Multiplicação matricial em Numpy Arrays
print("\nMultiplicação matricial em Numpy Arrays:\n")

print(f"Multiplicação matricial (np.dot()): \n{np.dot(x,y)}\n")

print(f"Multiplicação matricial (x @ y): \n{x @ y}\n")

print(f"Multiplicação matricial (x.dot(y)): \n{x.dot(y)}\n")
