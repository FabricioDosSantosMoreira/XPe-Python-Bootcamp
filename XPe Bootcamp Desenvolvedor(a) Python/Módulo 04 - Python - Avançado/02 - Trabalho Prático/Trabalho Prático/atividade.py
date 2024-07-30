from io import StringIO
from typing import List

import pandas as pd
import requests
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler

DATA_URL: str = "http://lib.stat.cmu.edu/datasets/boston"


def read_data(url: str) -> pd.DataFrame:

    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"\nOcorreu um erro ao obter os dados!")

    lines: List[str] = response.text.splitlines()
    lines = lines[22:] # Pular as primeiras 22 linhas de cabeçalho

    combined_lines: List[str] = []
    current_line: str = ""
    for line in lines:
        current_line += " " + line.strip()

        if len(current_line.split()) == 14:
            combined_lines.append(current_line)
            current_line = ""

    data = "\n".join(combined_lines)
    columns = [
        "CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT", "MEDV"
    ]

    df: pd.DataFrame = pd.read_csv(
        StringIO(data), delim_whitespace=True, header=None, names=columns
    )
    return df


# Lendo os dados
df = read_data(DATA_URL)


# Separando os dados em data e target
data = df.drop(columns=["MEDV"])
target = df["MEDV"]


# Dividindo os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=42)


# Normalização dos dados
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# Criando e treinando o classificador de redes neurais MLP (Multi-Layer Perceptron)
model_MLP = MLPRegressor(
    max_iter=1000,
    tol=0.000010,
    verbose=True,
    hidden_layer_sizes=(15, 5),
    random_state=42,
)
model_MLP.fit(X_train, y_train)


# Predição no conjunto de teste
predict = model_MLP.predict(X_test)


# Avaliação do modelo
train_score = model_MLP.score(X_train, y_train)
test_score = model_MLP.score(X_test, y_test)

mse = mean_squared_error(y_test, predict)
r2 = r2_score(y_test, predict)

print(f"\nAcurácia do conjunto de treinamento: {train_score}")
print(f"\nAcurácia do conjunto de teste: {test_score}")
print(f"\nMean Squared Error: {mse}")
print(f"\nR²: {r2}")
