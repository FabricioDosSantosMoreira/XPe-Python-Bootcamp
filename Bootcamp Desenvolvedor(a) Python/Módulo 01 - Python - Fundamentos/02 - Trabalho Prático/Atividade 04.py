nome = "Fabrício dos Santos Moreira"; cidade = "Florianópolis"; cpf = "123.456.789-00"


# Transformando cada caracter das variáveis em letras maiúsculas
print(f"\nNOME = [{nome.upper()}], CIDADE = [{cidade.upper()}], CPF = [{cpf.upper()}]")


# Transformando cada caracter das variáveis em letras minúsculas
print(f"\nNOME = [{nome.lower()}], CIDADE = [{cidade.lower()}], CPF = [{cpf.lower()}]")


# Procurando pelo caracter "í e ó" em cada variável e retornando a posição
# OBS: 'cpf' retorna '-1' porque não existe uma substring "í"
print(f"\nNOME = [{nome.find("í")}], CIDADE = [{cidade.find("ó")}], CPF = [{cpf.find("í")}]")


# Retornando o número de caracteres de cada variável
print(f"\nNOME = [{len(nome)}], CIDADE = [{len(cidade)}], CPF = [{len(cpf)}]")


# Mudando cada '.' e '-' do 'cpf' por espaços vazios
print(f"\nCPF = [{cpf.replace('.', '').replace('-', '')}]")
