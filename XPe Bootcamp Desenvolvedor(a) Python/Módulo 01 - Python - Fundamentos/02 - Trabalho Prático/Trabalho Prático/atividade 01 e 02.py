from typing import List

inicio: int = 100; fim: int = 500 
multiplos: List[int] = []

# Verifica os múltiplos de 2, 5 e 7 entre 'inicio' até 'fim' + 1
for n in range(inicio, fim + 1): 

    # Se o resto da divisão entre 'n' e 2, 5 ou 7 é igual 0, adiciona aos 'multiplos'
    if n % 2 == 0 or n % 5 == 0 or n % 7 == 0: 
        multiplos.append(n)

print(f"\nOs múltiplos de [2, 5 e 7] entre [{inicio}, {fim}] são: {multiplos}", end=".")
