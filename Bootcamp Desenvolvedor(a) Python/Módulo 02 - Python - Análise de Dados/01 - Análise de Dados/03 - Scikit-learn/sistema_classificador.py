from pathlib import Path
from typing import List

import numpy as np
import pandas as pd

ROOT_PATH: Path = Path(__file__).parent

dataframe = pd.read_csv(ROOT_PATH / "temperature.csv")

x = dataframe[['temperatura']].values
y = dataframe[['classification']].values

print(f"\nx:\n {x}")
print(f"\ny:\n {y}")



# Conversão de y para valores númericos
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y.ravel())



# Modelo classificador
from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()
clf.fit(x, y)



# Gerando 100 valores de temperatura linearmente espaçados entre 0 e 45 
x_test = np.linspace(start=0, stop= 45, num=100).reshape(-1, 1)

# Predição dos valores 'x_test'
y_pred = clf.predict(x_test)

# Conversão de 'y_pred' para os valores originais
y_pred = label_encoder.inverse_transform(y_pred)



# Prevendo alguns valores de temperatura
temperaturas: List[float] = [
    10, 24.2, 15.5, 8.5, 1.1, 32, 40.5, 12.2, 24.9
]

temperaturas = np.array(temperaturas).reshape(-1, 1)

previsao_temperaturas = clf.predict(temperaturas)
previsao_temperaturas = label_encoder.inverse_transform(previsao_temperaturas)


for i, temp in enumerate(previsao_temperaturas):
    print(f"\nA classificação de {temperaturas[i]}ºC é: {temp}")
