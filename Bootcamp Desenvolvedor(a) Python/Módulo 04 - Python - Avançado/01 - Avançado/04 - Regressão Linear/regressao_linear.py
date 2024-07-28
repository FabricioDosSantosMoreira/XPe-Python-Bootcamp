import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Altura de uma pessoa em metros
X = np.array([[160], [175], [176], [179], [180], [186], [189], [190], [198], [200]])
# Peso de uma pessoa em quilos
y = np.array([[50], [56], [60], [67], [89], [100], [87], [97], [75], [89]])



# Criando e treinando o modelo de Linear Regression
model_LR = LinearRegression()
model_LR.fit(X, y)



# Prevendo o peso para uma pessoa com altura de 190 cm
previsao = model_LR.predict(np.array([[190]]))
print(f"\nPeso previsto para uma pessoa com altura de 190cm: {previsao[0][0]}Kg")



# Prevendo diversos pesos
pesos = np.array([[160], [175], [176], [179], [180], [186], [189], [190], [198], [200]])
previsoes = model_LR.predict(pesos)



# Erro Absoluto Médio (MAE)
mae = mean_absolute_error(y, previsoes)
print(f"\nErro Absoluto Médio (MAE): {mae}")



# Erro Quadrático Médio (MSE)
mse = mean_squared_error(y, previsoes)
print(f"\nErro Quadrático Médio (MSE): {mse}")



# Plotando os dados reais e a linha de regressão
plt.scatter(X, y, color='blue', label='Dados reais')
plt.plot(X, previsoes, color='red', label='Linha de regressão')
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.title('Regressão Linear: Altura vs Peso')
plt.legend()
plt.show()
