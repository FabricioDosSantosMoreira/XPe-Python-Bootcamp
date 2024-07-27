import numpy as np

x = np.array([[1, 2], [3, 4]])
y = np.array([1.5, 3.5])

print(f"\nx:\n {x}")
print(f"\ny:\n {y}")



# Comparação booleana: Element Wise ou elemento por elemento
print("\nComparação booleana em Numpy Arrays:\n")

print(f"\nComparação (x > 2):\n {x > 2}")

print(f"\nComparação (x < 2):\n { x < 2}") 

print(f"\nComparação (x == 2):\n {x == 2}")  

print(f"\nComparação (x > y):\n {x > y}")

print(f"\nComparação (x < y):\n {x < y}")

print(f"\nComparação (x == y):\n {x == y}")
