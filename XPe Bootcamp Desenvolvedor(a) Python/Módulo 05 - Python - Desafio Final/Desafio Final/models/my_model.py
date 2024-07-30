from typing import List

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


def my_predicted_salary(dataframe: pd.DataFrame) -> List[float]:

    # Separando os dados em variáveis independentes(X) e dependentes(y)
    X = dataframe[["YearsExperience"]]
    y = dataframe["Salary"]

    # Dividindo os dados em conjuntos de treinamento e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Criando um modelo de regressão linear
    linear_model = LinearRegression()

    # Ajustando o modelo aos dados de treinamento
    linear_model.fit(X_train, y_train)

    # Fazendo previsões com o conjunto de teste
    y_pred = linear_model.predict(X_test)

    # Avaliando o desempenho do modelo
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("\nInformações do meu modelo:")
    print(f"MSE (Erro Quadrático Médio): {mse}")
    print(f"R-squared (R²): {r2}")

    # Previsão de todo o dataframe
    predicted_salary = linear_model.predict(X)
    return [round(value, 2) for value in predicted_salary]
