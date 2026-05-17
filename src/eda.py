import pandas as pd
df = pd.read_csv("data/cleaned_dataset.csv")
print(df.head())
# Estatísticas descritivas
print(df.describe())

# Informações gerais sobre colunas e tipos de dados
print(df.info())
import matplotlib.pyplot as plt

# Média do AQI por cidade
df.groupby("city")["aqi"].mean().plot(kind="bar", figsize=(8,5))
plt.title("Média do AQI por cidade")
plt.xlabel("Cidade")
plt.ylabel("AQI médio")
plt.show()
df.plot(kind="scatter", x="pm2.5", y="pm10", figsize=(6,6))
plt.title("Relação entre PM2.5 e PM10")
plt.show()
import pandas as pd
import matplotlib.pyplot as plt   # <-- só essa importação nova

df = pd.read_csv("data/cleaned_dataset.csv")
print(df.head())
print(df.describe())
print(df.info())

# -----------------------------
# Gráficos básicos
# -----------------------------

# Gráfico de colunas: média do AQI por cidade
df.groupby("city")["aqi"].mean().plot(kind="bar", figsize=(8,5))
plt.title("Média do AQI por cidade")
plt.xlabel("Cidade")
plt.ylabel("AQI médio")
plt.show()

# Gráfico de dispersão: PM2.5 vs PM10
df.plot(kind="scatter", x="pm2.5", y="pm10", figsize=(6,6))
plt.title("Relação entre PM2.5 e PM10")
plt.show()

# Histograma: distribuição do AQI
df["aqi"].plot(kind="hist", bins=20, figsize=(8,5))
plt.title("Distribuição do AQI")
plt.xlabel("AQI")
plt.show()

# Gráfico de linha: evolução do AQI ao longo dos anos
df.groupby("year")["aqi"].mean().plot(kind="line", marker="o", figsize=(8,5))
plt.title("Evolução do AQI ao longo dos anos")
plt.xlabel("Ano")
plt.ylabel("AQI médio")
plt.show()
python src/eda.py
pip install matplotlib
python src/eda.py

