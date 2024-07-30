from typing import Dict, List

import numpy as np
import pandas as pd

# Atividade 01
print("\nAtividade 01:")
Z = np.zeros((4, ))
print(f"Z: {Z}")


# Atividade 02
print("\nAtividade 02:")
Z = np.zeros((4, ))
Z[1] = 1.
print(f"Z: {Z}")


# Atividade 03
print("\nAtividade 03:")
Z = np.zeros((4, ))
Z[1:] = 1.
print(f"Z: {Z}")


# Atividade 04
print("\nAtividade 04:")
Z = np.zeros((4, ))
Z[0:3] = 1.
print(f"Z: {Z}")


# Atividade 05
print("\nAtividade 05:")
X = np.ones((2,2)) + 1
print(f"X:\n {X}")


# Atividade 06
print("\nAtividade 06:")
X = np.array([[1, 2], [3, 4]])
Y = X[0, :]
Y[1] = 10
print(f"X:\n {X}")


# Atividade 07
print("\nAtividade 07:")
X = np.array([[1, 3], [11, 10]])
print(np.mean(X[X > np.pi]))


# Atividade 08
print("\nAtividade 08:")
data: Dict[str, List] = {
    'animal': 
        ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'], 
    'age': 
        [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3], 
    'visits': 
        [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 
    'priority': 
        ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels: List[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

dataframe = pd.DataFrame(data=data, index=labels)

print(f"\nDataFrame:\n {dataframe}")
