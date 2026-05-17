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

# Criar abas/páginas
aba = st.tabs(["📊 Visão Geral", "🌱 Poluentes", "📈 Evolução"])

# Aba 1 - Visão Geral
with aba[0]:
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
        df[df["year"] == ano_selecionado].groupby("city")["aqi"].mean().plot(kind="bar", ax=ax, color="skyblue")
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
    st.subheader(f"📈 Evolução do AQI ao longo dos anos - {cidade_selecionada}")
    fig, ax = plt.subplots()
    df[df["city"] == cidade_selecionada].groupby("year")["aqi"].mean().plot(kind="line", marker="o", ax=ax, color="red")
    ax.set_ylabel("AQI médio")
    st.pyplot(fig)