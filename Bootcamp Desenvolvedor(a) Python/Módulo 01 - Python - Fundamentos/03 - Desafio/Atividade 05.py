from typing import List, Optional, Tuple


def maior_impar(lista: List[int]) -> Optional[int]:
    maior_impar: Optional[int] = None

    for valor in lista:
        if valor % 2 != 0 and valor > 0:
            if maior_impar is None or valor > maior_impar:
                maior_impar = valor

    return maior_impar


def menor_impar(lista: List[int]) -> Optional[int]:
    menor_impar: Optional[int] = None

    for valor in lista:
        if valor % 2 != 0 and valor > 0:
            if menor_impar is None or valor < menor_impar:
                menor_impar = valor

    return menor_impar


def maior_e_menor_impar(lista: List[int]) -> Tuple[Optional[int], Optional[int]]:
    maior = maior_impar(lista)
    menor = menor_impar(lista)

    return (maior, menor)


lista: List[int] = [-1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 209]
maior_impar_na_lista, menor_impar_na_lista = maior_e_menor_impar(lista)

print("O maior impar é:", maior_impar_na_lista) 
print("O menor impar é:", menor_impar_na_lista) 
