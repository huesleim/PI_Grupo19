import pandas as pd

df = pd.read_csv("../data/global_air_quality_deforestation_dataset.csv")

# Tratamento de dados 
df.columns = df.columns.str.lower() # Deixa os nomes das colunas em minúsculo
df = df.drop_duplicates() # Remove linhas duplicadas
df = df.dropna() # Remove linhas com valores nulos (caso houvessem) 

# Exportação de dados limpos em um novo CSV
df.to_csv("../data/banco_limpo.csv", index=False)
