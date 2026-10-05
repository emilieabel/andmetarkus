import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import duckdb
import shap
import pandas as pd

"# Pingviini äpp"

penguins = sns.load_dataset("penguins")

col1, col2, col3 = st.columns(3)

with col1:
    flipper_length = st.slider("Tiiva pikkus", penguins["flipper_length_mm"].min(), penguins["flipper_length_mm"].max())

with col2:
    bill_length = st.slider("Noka pikkus",penguins["bill_length_mm"].min(), penguins["bill_length_mm"].max())

with col3:
    bill_depth = st.slider("Noka sügavus", penguins["bill_depth_mm"].min(), penguins["bill_depth_mm"].max())


# Viskame välja puuduvate väärtustega read

complete_penguins = penguins.dropna()

# Treenime random forest mudeli, mille sisesnid on tiiva pikkus, noka pikkus ja noka sügavus ning väljund on linnukese kaal


from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor()

model.fit(complete_penguins[["flipper_length_mm", "bill_length_mm", "bill_depth_mm"]], complete_penguins["body_mass_g"])


# Genereerime antud mudelist kasutaja ette antud andmete põhjal ennustuse

user_input = pd.DataFrame(
    [[flipper_length, bill_length, bill_depth]],
    columns=["flipper_length_mm", "bill_length_mm", "bill_depth_mm"],
)

prediction = round(model.predict(user_input)[0])

# Näitame ennustuse kasutajale välja

st.write(f"Selle pingviini hinnanguline kaal on {prediction}g")

# Boonus: SHAP graafik, mis selgitab, kuidas see ennustus sündis

fig = plt.figure(figsize=(10, 4))
ax=sns.kdeplot(complete_penguins, x="body_mass_g")
ax.axvline(x=prediction, color='red', linewidth=2)
st.pyplot(fig)

"## Aga miks mudel nii ennustas?"

explainer = shap.TreeExplainer(model)
shap_values = explainer(user_input)

shap_fig = plt.figure()
shap.plots.waterfall(
    shap_values[0],
    show=False
)
st.pyplot(shap_fig)