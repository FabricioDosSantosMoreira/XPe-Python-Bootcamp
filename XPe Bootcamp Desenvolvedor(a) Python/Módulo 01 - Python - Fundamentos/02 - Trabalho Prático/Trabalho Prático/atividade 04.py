nome: str = "Fabrício dos Santos Moreira"; cidade: str = "Florianópolis"; cpf: str = "123.456.789-00"


# Transformando cada caracter para letras maiúsculas em cada variável
print(f"\nNOME = [{nome.upper()}], CIDADE = [{cidade.upper()}], CPF = [{cpf.upper()}]")


# Transformando cada caracter para letras minúsculas em cada variável
print(f"\nNOME = [{nome.lower()}], CIDADE = [{cidade.lower()}], CPF = [{cpf.lower()}]")


# Procurando o índice da primeira ocorrência de caracteres em cada variável
print(f"\nNOME = [{nome.find("í")}], CIDADE = [{cidade.find("ó")}], CPF = [{cpf.find(".")}]")


# Obtendo o número de caracteres em cada variável
print(f"\nNOME = [{len(nome)}], CIDADE = [{len(cidade)}], CPF = [{len(cpf)}]")


# Mudando cada '.' e '-' do 'cpf' por espaços vazios
print(f"\nCPF = [{cpf.replace('.', '').replace('-', '')}]")
