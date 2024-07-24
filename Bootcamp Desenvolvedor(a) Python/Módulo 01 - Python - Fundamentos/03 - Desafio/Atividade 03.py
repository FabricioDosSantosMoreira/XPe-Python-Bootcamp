from math import pi
from typing import Optional 

def area_circulo(r: float, pi: Optional[float] = pi):

    area: float = pi * (r**2)
    return area

raio = 8



print("A área do circulo é:", area_circulo(raio), "cm^2") 
print("A área do circulo é:", area_circulo(raio, 3.141592), "cm^2") 
