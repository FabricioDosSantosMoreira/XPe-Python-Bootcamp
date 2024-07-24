nomes: list[str] = ['Maria', 'Julieta', 'Fernando', 'Cristiano', 'Julieta', 'Maria', 'Fernando', 'Cláudio'] 
qtd_letras: dict[str] = {}

for nome in nomes:
    qtd_letras[nome] = len(nome) 

for key, value in qtd_letras.items():
    print(f"{key} contém {value} letra(s)")



qtd_letras: dict[str] = {nome: len(nome) for nome in nomes} 

for key, value in qtd_letras.items():
    print(f"{key} contém {value} letra(s)")
