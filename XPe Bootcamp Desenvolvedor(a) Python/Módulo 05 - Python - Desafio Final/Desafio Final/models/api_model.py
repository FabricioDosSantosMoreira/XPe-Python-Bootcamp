import json
from pathlib import Path
from typing import Dict, List, Union

import pandas as pd
import requests

# Endpoint da API com o modelo de Machine Learning
url: str = "https://as5jmctylk.execute-api.us-east-1.amazonaws.com/default/demo_forecast"


def api_predicted_salary(dataframe: pd.DataFrame) -> Union[List[float], None]:

    years_experience: pd.Series = dataframe["YearsExperience"]

    data: Dict[str, float] = {}
    for i in years_experience.index:
        # NOTE: A API recebe um json que contém str e float
        # Neste caso, a chave será o id e o valor será years_experience[i]
        data[i] = years_experience[i]

    # NOTE: Retorna um json contendo chave valor
    # A chave é uma string representando o nome
    # O Valor é a previsão do 'Salary' baseado em 'YearsExperience'
    response = requests.post(url=url, data=json.dumps(data))

    if response.status_code == 200:
        predicted_salary: Dict[str, float] = response.json()

        # Retorna uma lista contendo os salários previstos
        return list(predicted_salary.values())

    else:
        return None
