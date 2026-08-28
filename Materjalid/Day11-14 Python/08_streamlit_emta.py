"""
python -m streamlit run streamlit_emta.py
"""

import streamlit as st
import pandas as pd
import duckdb

import matplotlib.pyplot as plt
import seaborn as sns

st.write("# Etteevõtluse statistika maakondade lõikes")

data = pd.read_csv("emta_data.csv")


col1, col2 = st.columns(2)

with col1:
    aasta = st.selectbox("Aasta", options=sorted(data["aasta"].unique(), reverse=True))

with col2:
    kvartal = st.selectbox(
        "Kvartal",
        options=duckdb.sql(f"SELECT DISTINCT kvartal FROM data WHERE aasta = {aasta} ORDER BY kvartal DESC")
    )


count_by_county = duckdb.sql(f"""
    SELECT
        maakond,
        count(DISTINCT registrikood) AS ettevotete_arv
    FROM data
    WHERE aasta = {aasta} AND kvartal = {kvartal}
    GROUP BY maakond
    HAVING maakond NOT NULL
    ORDER BY ettevotete_arv DESC
""").df()

st.write("## Ettevõtete arv maakondade lõikes")

st.bar_chart(count_by_county, y="ettevotete_arv", x="maakond", sort=False)

fig = plt.figure(figsize=(10, 4))
sns.barplot(count_by_county, x="ettevotete_arv", y="maakond")
st.pyplot(fig)

maakond: str = st.selectbox("Maakond", options=data["maakond"].unique())


st.write(duckdb.sql(f"""
    SELECT
        kov,
        count(DISTINCT registrikood) AS ettevotete_arv,
        round(avg(kaive) / 3)::int AS keskmine_kuine_kaive,
        round(avg(kaive))::int AS keskmine_kvartaalne_kaive
    FROM data
    WHERE aasta = {aasta} AND kvartal = {kvartal} AND maakond = '{maakond}'
    GROUP BY kov
    ORDER BY keskmine_kuine_kaive DESC
""").df())
