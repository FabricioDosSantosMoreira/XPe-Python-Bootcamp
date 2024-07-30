from pathlib import Path
from typing import List

import matplotlib.pyplot as plt
import pandas as pd
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

# Obtendo o diretório atual
ROOT_PATH: Path = Path(__file__).parent


# Lendo os dados
dataframe = pd.read_csv(ROOT_PATH / "data/risco_credito.csv")


# Exibindo as primeiras linhas do 'dataframe' para inspecionar os dados
print(f"\nHead: {dataframe.head()}")


# Exibindo a forma do 'dataframe' (número de linhas e colunas)
print(f"\nShape: {dataframe.shape}")


# Separando os dados em data(X) e target(y)
X = dataframe.iloc[:, 0:4].values # Previsores = colunas 'historia' até 'renda'
y = dataframe.iloc[:, -1].values # Alvo = coluna 'risco'


# Convertendo as colunas categóricas em valores numéricos
label_encoder = LabelEncoder()
X[:, 0] = label_encoder.fit_transform(X[:, 0]) # Coluna 'historia'
X[:, 1] = label_encoder.fit_transform(X[:, 1]) # Coluna 'divida'
X[:, 2] = label_encoder.fit_transform(X[:, 2]) # Coluna 'garantias'
X[:, 3] = label_encoder.fit_transform(X[:, 3]) # Coluna 'renda'

# Exibindo o primeiro registro das features (X) após a transformação
print(f"\nPrimeiro registro das features após transformação: {X[0]}")


# Criando e treinando o modelo de Decision Tree Classifier
model_DTC = DecisionTreeClassifier(criterion='entropy')
model_DTC.fit(X, y)


# Exibindo a importância das características (features) na classificação
print(f"\nImportância de cada feature: {model_DTC.feature_importances_}")


# Exibindo as classes previstas pela árvore de decisão
print(f"\nClasses previstas: {model_DTC.classes_}")


# Definindo as variáveis de previsão
previsores: List[str] = ['historia', 'divida', 'garantias', 'renda']


# Criando uma figura e um eixo para plotar a árvore de decisão
figura, eixos = plt.subplots(nrows=1, ncols=1, figsize=(10, 10))


# Plotando a árvore de decisão com características e classes
tree.plot_tree(model_DTC, feature_names=previsores, class_names=model_DTC.classes_, filled=True)
plt.show()



# Previsão de exemplo com a árvore treinada
predictions = model_DTC.predict([[0, 0, 1, 2]])
print(f"\nPrevisão de exemplo: {predictions}")
