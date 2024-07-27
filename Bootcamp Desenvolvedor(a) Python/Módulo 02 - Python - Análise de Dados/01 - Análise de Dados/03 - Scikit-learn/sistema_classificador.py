from pathlib import Path
import pandas as pd

ROOT_PATH = Path(__file__).parent

dataframe = pd.read_csv(ROOT_PATH / "temperature.csv")

x, y = dataframe[['temperatura']].values, dataframe[['classification']].values

print(f"\nx:\n {x}")
print(f"\ny:\n {y}")



# Conversão de y para valores númericos
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y.ravel())
print(f"\ny convertido:\n {y}")



# Modelo
from sklearn.linear_model import LogisticRegression

# Classificador
clf = LogisticRegression()
clf.fit(x, y)



# Gerando 100 valores de temperatura linearmente espaçados entre 0 e 45 
import numpy as np
x_test = np.linspace(start=0., stop= 45., num=100).reshape(-1, 1)

# Predição desses valores
y_pred = clf.predict(x_test)

# Conversão de y_pred para os valores originais
y_pred = le.inverse_transform(y_pred)



def classificar_temperaturas():
    continuar: bool = True

    while continuar:
        temperatura = input("\nInsira a temperatura que deseja classificar: ")

        temperatura = np.array(float(temperatura)).reshape(-1,1)

        temperatura_classificada = clf.predict(temperatura)
        temperatura_classificada = le.inverse_transform(temperatura_classificada)

        print(f"\nA classificação da temperatura {temperatura.ravel()[0]} é: {temperatura_classificada[0]}")

        ask = input('Nova classificação? (y/n): ') == 'y' 



classificar_temperaturas()