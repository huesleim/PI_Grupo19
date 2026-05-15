import pandas as pd
import streamlit as st

df = pd.read_csv("data/banco_limpo.csv")

def classify_aqi(aqi):

    if aqi <= 50:
        return "Good"

    elif aqi <= 100:
        return "Moderate"

    elif aqi <= 150:
        return "Unhealthy for Sensitive Groups"

    elif aqi <= 200:
        return "Unhealthy"

    elif aqi <= 300:
        return "Very Unhealthy"

    else:
        return "Hazardous"

df["AQI_Quality"] = df["aqi"].apply(classify_aqi)

years = sorted(df["year"].unique())

selected_years = [
    years[0],
    years[len(years) // 2],
    years[-1]
]

st.title("Green Space vs AQI")

for year in selected_years:

    st.subheader(f"Ano: {year}")

    year_df = df[df["year"] == year]

    year_df = (
        year_df.groupby("country")
        .agg({
            "green_space_ratio_%": "mean",
            "aqi": "mean"
        })
        .reset_index()
    )

    year_df["AQI_Quality"] = year_df["aqi"].apply(classify_aqi)

    st.scatter_chart(
        data=year_df,
        x="green_space_ratio_%",
        y="aqi",
        color="AQI_Quality"
    )