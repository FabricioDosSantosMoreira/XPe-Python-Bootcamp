from typing import List
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

# Criando uma malha
xx, yy = np.meshgrid(np.linspace(-3, 3, 500), np.linspace(-3, 3, 500))



# Gerando dados
np.random.seed(0)
X = np.random.randn(300, 2)
Y = np.logical_xor(X[:, 0] > 0, X[:, 1] > 0)



# Treinando o modelo
clf = svm.NuSVC(gamma='auto')
clf.fit(X, Y)



# Obtendo a função de decisão para cada ponto na malha
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
# Ajusta a forma dos resultados para corresponder à malha original.
Z = Z.reshape(xx.shape)



# Plota a fronteira de decisão e os pontos de dados
plt.contourf(xx, yy, Z, levels=np.linspace(Z.min(), 0, 7), cmap=plt.cm.PuOr, alpha=0.8)
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired, edgecolors='k')
# Adiciona rótulos e exibe o gráfico
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Fronteira de Decisão do NuSVC')
plt.show()
