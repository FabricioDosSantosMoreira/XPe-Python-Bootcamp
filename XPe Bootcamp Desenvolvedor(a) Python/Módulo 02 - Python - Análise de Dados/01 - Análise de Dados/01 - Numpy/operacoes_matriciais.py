import numpy as np

x = np.ones((2,2))
y = np.eye(2)

print(f"\nx:\n {x}")
print(f"\ny:\n {y}")


# Multiplicação matricial em Numpy Arrays
print(f"\nMultiplicação matricial (np.dot()):\n {np.dot(x,y)}")
print(f"\nMultiplicação matricial (x @ y):\n {x @ y}")
print(f"\nMultiplicação matricial (x.dot(y)):\n {x.dot(y)}")
