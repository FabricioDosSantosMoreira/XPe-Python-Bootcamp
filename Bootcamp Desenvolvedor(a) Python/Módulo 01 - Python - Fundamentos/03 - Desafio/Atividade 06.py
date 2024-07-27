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


especialistas: Dict[str, Set[DiasDaSemana]] = {
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


disponibilidade = disp_dois_especialistas(especialistas["cardiologista"], especialistas["ortopedista"])
print(f"\nDisponibilidade no mesmo dia para cardiologista e ortopedista: {disponibilidade}")



disponibilidade = disp_dois_especialistas(especialistas["neurologista"], especialistas["ortopedista"])
print(f"\nDisponibilidade no mesmo dia para neurologista e ortopedista: {disponibilidade}")



disponibilidade = disp_tres_especialistas(especialistas["cardiologista"], especialistas["ortopedista"], especialistas["psiquiatra"])
print(f"\nDisponibilidade no mesmo dia para cardiologista, ortopedista e psiquiatra: {disponibilidade}")



disponibilidade = disp_tres_especialistas(especialistas["cardiologista"], especialistas["psiquiatra"], especialistas["dermatologista"])
print(f"\nDisponibilidade no mesmo dia para cardiologista, psiquiatra e dermatologista: {disponibilidade}")
