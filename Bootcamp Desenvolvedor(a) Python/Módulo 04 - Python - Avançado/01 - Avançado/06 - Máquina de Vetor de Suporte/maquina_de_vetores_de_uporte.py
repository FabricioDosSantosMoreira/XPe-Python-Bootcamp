from pathlib import Path

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

# Obtendo o diretório atual
ROOT_PATH: Path = Path(__file__).parent



# Lendo os dados
dataframe = pd.read_csv(ROOT_PATH / "data/social_network_ads.csv")



# Exibe as primeiras linhas do 'dataframe' para inspecionar os dados
print(f"\nHead: {dataframe.head()}")



# Exibe a forma do 'dataframe' (número de linhas e colunas)
print(f"\nShape: {dataframe.shape}")



# Separando os dados em data(X) e target(y)
X = dataframe[['Age', 'EstimatedSalary']] # Previsores = colunas 'Age' e 'EstimatedSalary'
y = dataframe['Purchased'] # Alvo = coluna 'Purchased'



# Normalizando os dados para que todas as características tenham a mesma escala
standard_scaler = StandardScaler()
X = standard_scaler.fit_transform(X)
print(f"\nPrimeiro registro das features após padronização {X[0]}")



# Dividindo o conjunto de dados em 80% de treinamento e 20% de teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)



# Criando e treinando o modelo de SVM com kernel 'rbf', semente aleatória 1 e parâmetro de regularização C=1.0
model_SVM = SVC(kernel='rbf', random_state=1, C=1.0)
model_SVM.fit(X_train, y_train.values.ravel())



# Predição no conjunto de teste
predictions = model_SVM.predict(X_test)


 
# Avaliação do modelo
test_score = accuracy_score(y_test, predictions)
print(f"\nAcurácia do conjunto de teste: {test_score}")
