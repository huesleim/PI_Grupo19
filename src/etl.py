import pandas as pd

# 1. Carregar o dataset
df = pd.read_csv("data/global_air_quality_deforestation_dataset.csv")

# 2. Transformações
# Transformar nomes das colunas em caixa baixa
df.columns = df.columns.str.lower()

# Remover duplicatas
df = df.drop_duplicates()

# Remover valores nulos
df = df.dropna()

# 3. Criar novas colunas (exemplos extras para enriquecer o trabalho)
df["vehicles_per_density"] = df["vehicles_increase_%"] / df["population_density_per_sqkm"]
df["green_space_per_capita"] = df["green_space_ratio_%"] / df["population_density_per_sqkm"]

# 4. Salvar dataset tratado
df.to_csv("data/cleaned_dataset.csv", index=False)

print("Transformações concluídas! Arquivo salvo em data/cleaned_dataset.csv")
print(df.columns)
