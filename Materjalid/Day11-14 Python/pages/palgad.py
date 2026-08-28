import streamlit as st

import pandas as pd
import duckdb


"# Palgad tööstusharude lõikes"

data = pd.read_csv("emta_data.csv")

TAX_PERCENTAGE = 0.338

salary_stats = duckdb.sql(f"""
    SELECT
        tegevusala,
        avg(toojoumaksud / {TAX_PERCENTAGE} / tootajate_arv / 3) AS keskmine_palk
    FROM data
    WHERE aasta = 2026 AND kvartal = 1 AND tegevusala IS NOT NULL
    GROUP BY tegevusala
    ORDER BY keskmine_palk DESC
""").df()

st.write(salary_stats)
""
""
""
st.bar_chart(salary_stats, x="tegevusala", y="keskmine_palk", sort=False, horizontal=True)