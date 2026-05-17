import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar dataset
df = pd.read_csv("data/cleaned_dataset.csv")

st.title("🌍 Dashboard - Qualidade do Ar e Meio Ambiente")

# Filtros principais
anos = sorted(df["year"].unique())
cidades = sorted(df["city"].unique())

col1, col2 = st.columns(2)
with col1:
    ano_selecionado = st.selectbox("Selecione o ano:", anos)
with col2:
    cidade_selecionada = st.selectbox("Selecione a cidade:", cidades)

df_filtrado = df[(df["year"] == ano_selecionado) & (df["city"] == cidade_selecionada)]


# Declaração de variáveis para os gráficos
cidades_brasileiras = df[df["country"] == "Brazil"]["city"].unique()

ano_df = df[df["year"] == ano_selecionado]
cidade_df = df[df["city"] == cidade_selecionada]

aqi_por_cidade = ano_df.groupby("city")["aqi"].mean().reset_index()
aqi_por_cidade = aqi_por_cidade[(aqi_por_cidade["city"].isin(cidades_brasileiras)) |
(aqi_por_cidade["city"] == cidade_selecionada)]

aqi_por_ano = cidade_df.groupby("year")["aqi"].mean().reset_index()

espaços_verdes_por_ano = cidade_df.groupby("year")["green_space_ratio_%"].mean().reset_index()
investimento_por_ano = cidade_df.groupby("year")["env_budget_million_usd"].mean().reset_index()


# Criar abas/páginas
aba = st.tabs(["📊 Visão Geral", "🌱 Poluentes", "📈 Evolução"])

# Aba 1 - Visão Geral
with aba[0]:
    st.subheader("⚙️Conteúdo da base de dados")
    st.write(df_filtrado.dtypes)

    st.subheader("📊 Dados filtrados")
    st.write(df_filtrado.head())

    st.subheader("📈 Estatísticas descritivas")
    st.write(df_filtrado.describe())

# Aba 2 - Poluentes
with aba[1]:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader(f"Média do AQI por cidade - Ano {ano_selecionado}")
        fig, ax = plt.subplots()


        ax.bar(
            aqi_por_cidade["city"],
            aqi_por_cidade["aqi"],
            color="skyblue"
        )

        ax.set_ylabel("AQI médio")
        st.pyplot(fig)

    with col2:
        st.subheader(f"Relação entre PM2.5 e PM10 - {cidade_selecionada}, {ano_selecionado}")
        fig, ax = plt.subplots()
        df_filtrado.plot(kind="scatter", x="pm2.5", y="pm10", ax=ax, color="green")
        st.pyplot(fig)

    st.subheader(f"📉 Distribuição do AQI - {cidade_selecionada}, {ano_selecionado}")
    fig, ax = plt.subplots()
    df_filtrado["aqi"].plot(kind="hist", bins=20, ax=ax, color="orange", edgecolor="black")
    ax.set_xlabel("AQI")
    st.pyplot(fig)

# Aba 3 - Evolução
with aba[2]:


    # Evolução do AQI ao longo dos anos
    st.subheader(f"📈 Evolução do AQI ao longo dos anos - {cidade_selecionada}")
    fig, ax = plt.subplots()
    ax.plot(
        aqi_por_ano["year"], 
        aqi_por_ano["aqi"], 
        label="AQI", 
        color="red", 
        marker="o"
    )
    ax.set_ylabel("AQI médio")
    ax.set_xlabel("Ano")
    st.pyplot(fig)

    # Relação entre espaços verdes e AQI ao longo dos anos
    st.subheader( f"📉 Relação entre espaços verdes e AQI ao longo dos anos - {cidade_selecionada}")
    fig, ax1 = plt.subplots(figsize=(10, 5))

    # Espaços verdes
    ax1.plot(
    espaços_verdes_por_ano["year"],
    espaços_verdes_por_ano["green_space_ratio_%"],
    color="green",
    marker="o",
    label="Espaços Verdes (%)"
    )

    ax1.set_xlabel("Ano")
    ax1.set_ylabel("Espaços Verdes (%)", color="green")
    ax1.tick_params(axis="y", labelcolor="green")

    # AQI
    ax2 = ax1.twinx()

    ax2.plot(
        aqi_por_ano["year"],
        aqi_por_ano["aqi"],
        color="red",
        marker="o",
        label="AQI"
    )

    ax2.set_ylabel("AQI", color="red")
    ax2.tick_params(axis="y", labelcolor="red")

    st.pyplot(fig)

    # Relação entre investimento governamental em sustentabilidade e AQI ao longo dos anos
    st.subheader( f"📉 Relação entre investimento público e AQI ao longo dos anos - {cidade_selecionada}")
    fig, ax1 = plt.subplots()

    # Investimento governamental
    ax1.plot(
    investimento_por_ano["year"],
    investimento_por_ano["env_budget_million_usd"],
    color="green",
    label="Investimento público em políticas ambientais (USD)"
    )

    ax1.set_xlabel("Ano")
    ax1.set_ylabel("Investimento público em políticas ambientais (USD)", color="green")
    ax1.tick_params(axis="y", labelcolor="green")

    # AQI
    ax2 = ax1.twinx()

    ax2.plot(
        aqi_por_ano["year"],
        aqi_por_ano["aqi"],
        color="red",
        marker="o",
        label="AQI"
    )

    ax2.set_ylabel("AQI", color="red")
    ax2.tick_params(axis="y", labelcolor="red")

    st.pyplot(fig)
