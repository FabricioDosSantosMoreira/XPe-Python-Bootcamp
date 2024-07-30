numero: str = "1234567890987654321"
soma: int = 0 

for caractere in numero:
    # Transforma o caracter em int
    valor = int(caractere) 
    # Adiciona o 'valor' na 'soma'
    soma += valor 

print(f"\nO resultado da soma é: {soma}")
    