from typing import Dict, List

NOMES: List[str] = [
    "Maria", "Julieta", "Fernando", "Cristiano", 
] 


# NOTE: Método 1
qtd_letras: Dict[str, int] = {}

for nome in NOMES:
    qtd_letras[nome] = len(nome) 

for key, value in qtd_letras.items():
    print(f"\nO nome ['{key}'] contém {value} letra(s)")


# NOTE: Método 2
qtd_letras: dict[str] = {nome: len(nome) for nome in NOMES} 

for key, value in qtd_letras.items():
    print(f"\nO nome ['{key}'] contém {value} letra(s)")
