from pathlib import Path

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Obtendo o diretório atual
ROOT_PATH: Path = Path(__file__).parent



# Lendo os dados
dataframe = pd.read_csv(ROOT_PATH / "data/census.csv")



# Exibe as primeiras linhas do 'dataframe' para inspecionar os dados
print(f"\nHead: {dataframe.head()}")



# Exibe a forma do 'dataframe' (número de linhas e colunas)
print(f"\nShape: {dataframe.shape}")



# Separando os dados em data(X) e target(y)
X = dataframe.iloc[:, 0:14].values # Previsores = colunas 'age' até 'native-country'
y = dataframe.iloc[:, 14].values # Alvo = coluna 'income'



# Convertendo as colunas categóricas em valores numéricos
label_encoder = LabelEncoder()
X[:, 1] = label_encoder.fit_transform(X[:, 1])    # Coluna 'workclass'
X[:, 3] = label_encoder.fit_transform(X[:, 3])    # Coluna 'education'
X[:, 5] = label_encoder.fit_transform(X[:, 5])    # Coluna 'marital-status'
X[:, 6] = label_encoder.fit_transform(X[:, 6])    # Coluna 'occupation'
X[:, 7] = label_encoder.fit_transform(X[:, 7])    # Coluna 'relationship'
X[:, 8] = label_encoder.fit_transform(X[:, 8])    # Coluna 'race'
X[:, 9] = label_encoder.fit_transform(X[:, 9])    # Coluna 'sex'
X[:, 13] = label_encoder.fit_transform(X[:, 13])  # Coluna 'native-country'
# Exibindo o primeiro registro das features (X) após a transformação
print(f"\nPrimeiro registro das features após transformação: {X[0]}")



# Normalizando os dados para que todas as características tenham a mesma escala
standard_scaler = StandardScaler()
X = standard_scaler.fit_transform(X)
print(f"\nPrimeiro registro das features após padronização {X[0]}")



# Dividindo o conjunto de dados em 80% de treinamento e 20% de teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)



# Criando e treinando o modelo de Logistic Regression
model_LR = LogisticRegression(max_iter=12000)
model_LR.fit(X_train, y_train)



# Predição no conjunto de teste
predictions = model_LR.predict(X_test)


 
# Avaliação do modelo
test_score = accuracy_score(y_test, predictions)
print(f"\nAcurácia do conjunto de teste: {test_score}")
