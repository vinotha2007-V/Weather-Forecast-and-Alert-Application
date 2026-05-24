import streamlit as st
import pandas as pd

st.title("Weather Forecast Dashboard")

data = pd.read_csv("data/weather_history.csv")

st.line_chart(data["Temperature"])
st.dataframe(data)
