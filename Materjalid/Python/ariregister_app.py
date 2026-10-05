import streamlit as st
import seaborn
import duckdb
import pandas as pd


data = pd.read_csv("äri.csv")

"# Mis toimub Eesti äri maastikul?"

st.dataframe(data.head(10))