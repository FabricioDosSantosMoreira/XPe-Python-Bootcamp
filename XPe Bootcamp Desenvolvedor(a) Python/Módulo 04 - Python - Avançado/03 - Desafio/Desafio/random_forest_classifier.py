from pathlib import Path

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

ROOT_PATH: Path = Path(__file__).parent

# Lendo os dados
dataframe = pd.read_csv(ROOT_PATH / "data/census.csv")


# Separando os dados em data(X) e target(y)
X = dataframe.drop("income", axis=1)  
y = dataframe["income"] # Alvo = income 


# Selecionando apenas as colunas categóricas e precisam ser codificadas
categorical_columns = [
    'workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country'
]


# Convertendo as variáveis categóricas em valores numéricos
label_encoder = LabelEncoder()
for col in categorical_columns:
    X[col] = label_encoder.fit_transform(X[col])


# Normalizando os dados para que todas as características tenham a mesma escala
standardScaler = StandardScaler()
X_scaled = standardScaler.fit_transform(X)


# Dividindo os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)


# Criando e treinando o modelo de Random Forest Classifier
model_RFC = RandomForestClassifier(n_estimators=100, criterion='entropy', random_state=42)
model_RFC.fit(X_train, y_train)


# Predição no conjunto de teste
predict = model_RFC.predict(X_test)


# Avaliação do modelo
test_score = accuracy_score(y_test, predict)
print(f"\nAcurácia do conjunto de teste: {test_score}")
