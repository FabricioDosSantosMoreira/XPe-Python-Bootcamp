import math
from typing import Optional


def area_circulo(r: float, pi: Optional[float] = math.pi) -> float:
    area: float = pi * (r**2)

    return area

raio: int = 8

print(f"\nA área do circulo é: {round(area_circulo(raio), 5)} cm^2") 
print(f"\nA área do circulo é: {round(area_circulo(raio, 3.141592), 5)} cm^2") 
