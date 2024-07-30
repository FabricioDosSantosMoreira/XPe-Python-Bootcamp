from pathlib import Path

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

# Obtendo o diretório atual
ROOT_PATH: Path = Path(__file__).parent


# Lendo os dados
dataframe = pd.read_csv(ROOT_PATH / "data/credit_data.csv")


# Exibindo as primeiras linhas do 'dataframe' para inspecionar os dados
print(f"\nHead: {dataframe.head()}")


# Exibindo a forma do 'dataframe' (número de linhas e colunas)
print(f"\nShape: {dataframe.shape}")


# Removendo as linhas com valores ausentes
dataframe.dropna(inplace=True)


# Separando os dados em data(X) e target(y)
X = dataframe[['income', 'age', 'loan']] # Previsores = colunas 'income', 'age' e 'loan'
y = dataframe['default'] # Alvo = coluna 'default'


# Normalizando os dados para que todas as características tenham a mesma escala
standard_scaler = StandardScaler()
X = standard_scaler.fit_transform(X)
print(f"\nPrimeiro registro das features após padronização {X[0]}")


# Dividindo o conjunto de dados em 80% de treinamento e 20% de teste
X_train, X_test, y_train, y_test  = train_test_split(X, y, test_size=0.25, random_state=0)


# Exibindo as formas dos conjuntos de treinamento e teste
print(f"\nShape X_train: {X_train.shape}")
print(f"\nShape X_test: {X_test.shape}")
print(f"\nShape y_train: {y_train.shape}")
print(f"\nShape y_test: {y_test.shape}")


# Criando e treinando o modelo de MLP (Multi-Layer Perceptron)
MLP_model = MLPClassifier(max_iter=1000, tol=0.00001, verbose=True, hidden_layer_sizes=(15, 5), early_stopping=True, n_iter_no_change=10)
MLP_model.fit(X_train, y_train)


# Predição no conjunto de teste
predictions = MLP_model.predict(X_test)


# Avaliação do modelo
test_score = accuracy_score(y_test, predictions)
print(f"\nAcurácia do conjunto de teste: {test_score}")
