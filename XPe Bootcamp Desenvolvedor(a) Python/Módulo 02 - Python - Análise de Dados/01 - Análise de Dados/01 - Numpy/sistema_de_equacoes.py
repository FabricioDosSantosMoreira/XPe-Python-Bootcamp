import numpy as np

# Solução de um sistema de equações:
#   1a + 2b = 7
#   3a - 2b = -11
#   Solução analítica: (a, b) = (-1, 4)


# Matricialmente, este problema tem a seguinte forma:
# Ax = C, onde:
#   x = [a,b]
#   A = [[1, 2], [3, -2]]
#   C = [7, -11]
# Mas Ax = C, pode ser x = A^(-1) * C


# Sistema de equações:
#    A   *  x  =     Ax    =   C
# [1  2] * [a] = [ 1a  2b] = [ 7 ]
# [3 -2] * [b] = [ 3a -2b] = [-11]
# x = inverso(A) @ ou .dot(multiplicado por) C

# Definição do problema:
A = np.array([[1, 2], [3, -2]])
C = np.array([[7], [-11]])

print(f"\nA:\n {A}")
print(f"\nC:\n {C}")


# NOTE: Solução 1
x = np.dot(np.linalg.inv(A), C) # Multiplica o inverso de A por C 

# NOTE Solução 2
x = np.linalg.inv(A) @ C # Multiplica o inverso de A por C 


print("\nSolução do sistema de equação:")
print(f"(a, b) = {x.ravel()}") 
