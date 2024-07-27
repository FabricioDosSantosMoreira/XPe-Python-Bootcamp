import matplotlib.pyplot as plt
import numpy as np

# Dados
x = [-1., -0.77777778, -0.55555556, -0.33333333, -0.11111111, 
    0.11111111, 0.33333333, 0.55555556, 0.77777778, 1.]

y = [-1.13956201, -0.57177999, -0.21697033, 0.5425699, 0.49406657, 
     1.14972239, 1.64228553, 2.1749824, 2.64773614, 2.95684202]

x, y = np.array(x).reshape(-1, 1), np.array(y).reshape(-1, 1)

# Modelo
from sklearn.linear_model import LinearRegression

# Treinando o modelo: y = a*x + b, valores reais (a, b) = (2, 1)
reg = LinearRegression()
reg.fit(x, y)

# Coeficientes a, b estimados:
# Valores estimados usando o numpy diretamente
# a estimado no numpy: 2.05414951
# b estimado no numpy: 0.96798926

print('a estimado: ', reg.coef_.ravel()[0])
print('b estimado: ', reg.intercept_[0])

# Predição do modelo
y_pred = reg.predict(x)

# Score do modelo
score = reg.score(x, y)
print('\nscore: ', score) # Ver se os dados do modelo foi bom, quanto mais perto de 1 melhor

# Plot dos dados
plt.figure(figsize=(10,5)) 
plt.plot(x, y,"o", label='dados originais')
plt.plot(x, y_pred, label='regressão linear (R2: {:.4f})'.format(score)) 
plt.hlines(y = y.mean(), xmin= x.min(), xmax= x.max(), linestyles= 'dashed', label= 'Modelo de referência do $R^2$')
plt.legend() 
plt.xlabel("x") 
plt.ylabel("y") 
plt.title('Regressão linear no SciKit-Learn')
plt.grid()
plt.show() 

# Função para calculo do MSE
def mse(y_true, y_pred, is_ref = False):

    # MSE modelo
    if is_ref:
        mse = ((y_true - y_pred.mean())**2).mean()
    else:
        mse = ((y_true - y_pred)**2).mean()
    
    return mse

# Função para cálculo do coeficiente de determinação R2
def R2(mse_reg, mse_ref):
    return 1 - mse_reg/mse_ref

# Visualizando y e y_true
print('\ny_true: ', y.ravel())
print('y_pred: ', y_pred.ravel()) 

# Calculando o mse dos modelos
mse_reg = mse(y_true= y, y_pred= y_pred)
print('\nO MSE do modelo de regressão é: ', mse_reg)
mse_ref = mse(y_true= y, y_pred= y_pred, is_ref= True)
print('O MSE do modelo de referência é: ', mse_ref)

# Calculando o R2 Score
r2_score = R2(mse_reg= mse_reg, mse_ref= mse_ref)
print('\nCoeficiente R2 do modelo implementado (calculado): ', r2_score)

r2_score_sklearn = reg.score(x, y)
print('Coeficiente R2 do modelo implementado (SciKit-Learn): ', r2_score_sklearn)