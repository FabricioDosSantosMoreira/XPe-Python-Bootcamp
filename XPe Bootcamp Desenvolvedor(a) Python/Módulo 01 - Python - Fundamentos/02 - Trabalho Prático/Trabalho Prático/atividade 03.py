from typing import List

inicio: int = 0; fim: int = 1000 
divisor: int = 3
multiplos: List[int] = []

# Verifica os múltiplos de 'divisor' entre 'inicio' até 'fim' - 1
for n in range(inicio, fim): 

    # Se o resto da divisão entre 'n' e 'divisor' é igual 0, adiciona aos 'multiplos'
    if n % divisor == 0:
        multiplos.append(n)
        
print(f"\nOs múltiplos de [{divisor}] entre [{inicio}, {fim}] são: {multiplos}", end=".")
