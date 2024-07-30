import math
from typing import List, Union


def root_square_solver(a: float, b: float, c: float) -> Union[List[float], None]:
    # Calcula o discriminante
    discriminante = b**2 - 4 * a * c

    if discriminante > 0:
        # Duas raízes reais
        raiz_1 = (-b + math.sqrt(discriminante)) / (2*a)
        raiz_2 = (-b - math.sqrt(discriminante)) / (2*a)
        return [raiz_1, raiz_2]
    
    elif discriminante == 0:
        # Uma raíz real
        raiz = -b / (2*a)
        return [raiz]

    else:
        # Nenhuma raiz real
        return None
