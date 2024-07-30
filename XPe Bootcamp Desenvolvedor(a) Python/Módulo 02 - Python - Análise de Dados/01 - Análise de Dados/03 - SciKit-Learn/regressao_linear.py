from typing import List

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

X: List[float] = [
    -1., -0.77777778, -0.55555556, -0.33333333, -0.11111111, 
    0.11111111, 0.33333333, 0.55555556, 0.77777778, 1.
    ]

y: List[float] = [
    -1.13956201, -0.57177999, -0.21697033, 0.5425699, 0.49406657, 
     1.14972239, 1.64228553, 2.1749824, 2.64773614, 2.95684202
    ]

X: np.ndarray = np.array(X).reshape(-1, 1)
y: np.ndarray = np.array(y).reshape(-1, 1)


# Modelo classificador de regressão linear(y = a*x + b, valores reais (a, b) = (2, 1))
reg = LinearRegression()
reg.fit(X, y) # Treinando o modelo

print(f"a estimado: {reg.coef_.ravel()[0]}")
print(f"b estimado: {reg.intercept_[0]}")


# Predição do modelo
y_pred: np.ndarray = reg.predict(X)


# Score do modelo
score: float = reg.score(X, y)
print(f"\nScore: {score}") # OBS: Quanto mais perto de 1 melhor


# Plot dos dados
plt.figure(figsize=(10,5)) 
plt.plot(X, y, "o", label="Dados Originais")
plt.plot(X, y_pred, label=f"Regressão Linear (R2: {score:.2f})")
plt.hlines(y=y.mean(), xmin=X.min(), xmax=X.max(), linestyles="dashed", label="Modelo de Referência do $R^2$")
plt.legend() 
plt.xlabel("x") 
plt.ylabel("y") 
plt.title('Regressão linear no SciKit-Learn')
plt.grid()
plt.show() 


def get_mse(y_true, y_pred, is_ref: bool = False) -> float:
    mse: float = None

    # Calcula o erro quadrático médio
    if is_ref:
        mse = ((y_true - y_pred.mean())**2).mean()
    else:
        mse = ((y_true - y_pred)**2).mean()
    
    return mse


# Visualizando y e y_true
print(f"\ny_true:\n {y.ravel()}")
print(f"\ny_pred:\n {y_pred.ravel()}")


# Calculando o MSE dos modelos
mse_reg: float = get_mse(y_true=y, y_pred=y_pred)
mse_ref: float = get_mse(y_true=y, y_pred=y_pred, is_ref=True)

print(f"\nO MSE do modelo de regressão é: {mse_reg}")
print(f"\nO MSE do modelo de referência é: {mse_ref}")


# Calculando o Score R2
r2_score_sklearn = reg.score(X, y)
print(f"\nCoeficiente R2 do modelo implementado: {r2_score_sklearn}")
