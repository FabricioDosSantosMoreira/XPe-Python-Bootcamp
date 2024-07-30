from enum import Enum
from typing import Dict, List, Set, Union


class DiasDaSemana(Enum):
    SEGUNDA = 1
    TERCA = 2
    QUARTA = 3
    QUINTA = 4
    SEXTA = 5
    SABADO = 6
    DOMINGO = 7


ESPECIALISTAS: Dict[str, Set[DiasDaSemana]] = {
    "cardiologista": {DiasDaSemana.TERCA, DiasDaSemana.QUARTA},
    "ortopedista": {DiasDaSemana.TERCA, DiasDaSemana.QUINTA},
    "dermatologista": {DiasDaSemana.SEGUNDA, DiasDaSemana.QUARTA, DiasDaSemana.SEXTA},
    "neurologista": {DiasDaSemana.TERCA, DiasDaSemana.QUINTA, DiasDaSemana.SEXTA},
    "psiquiatra": {DiasDaSemana.SEGUNDA, DiasDaSemana.QUARTA, DiasDaSemana.SEXTA},
}


def disp_dois_especialistas(
        especialista01: Set[DiasDaSemana], 
        especialista02: Set[DiasDaSemana]
    ) -> Union[List[DiasDaSemana], List[str]]:   

    dias_comuns: Set[DiasDaSemana] = especialista01.intersection(especialista02)

    dias_disponiveis: List[str] = []
    for dia in dias_comuns:
        dias_disponiveis.append(dia.name)

    if dias_disponiveis:
        return dias_disponiveis

    return ["NENHUM DIA DISPONÍVEL"]


def disp_tres_especialistas(
        especialista01: Set[DiasDaSemana], 
        especialista02: Set[DiasDaSemana], 
        especialista03: Set[DiasDaSemana]
    ) -> Union[List[DiasDaSemana], List[str]]:

    dias_comuns: Set[DiasDaSemana] = especialista01.intersection(especialista02, especialista03)

    dias_disponiveis: List[str] = []
    for dia in dias_comuns:
        dias_disponiveis.append(dia.name)

    if dias_disponiveis:
        return dias_disponiveis
    
    return ["NENHUM DIA DISPONÍVEL"]


busca = ["cardiologista", "ortopedista"]
disp = disp_dois_especialistas(
    ESPECIALISTAS.get(busca[0]), 
    ESPECIALISTAS.get(busca[1])
)
print(f"\nDisponibilidade no mesmo dia para {busca}: {disp}")


busca = ["neurologista", "ortopedista"]
disp = disp_dois_especialistas(
    ESPECIALISTAS.get(busca[0]), 
    ESPECIALISTAS.get(busca[1])
)
print(f"\nDisponibilidade no mesmo dia para {busca}: {disp}")



busca = ["cardiologista", "ortopedista", "psiquiatra"]
disp = disp_tres_especialistas(
    ESPECIALISTAS.get(busca[0]),
    ESPECIALISTAS.get(busca[1]), 
    ESPECIALISTAS.get(busca[2])
)
print(f"\nDisponibilidade no mesmo dia para {busca}: {disp}")



busca = ["cardiologista", "psiquiatra", "dermatologista"]
disp = disp_tres_especialistas(
    ESPECIALISTAS.get(busca[0]),
    ESPECIALISTAS.get(busca[1]), 
    ESPECIALISTAS.get(busca[2])
)
print(f"\nDisponibilidade no mesmo dia para {busca}: {disp}")
