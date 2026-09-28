import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import statsmodels.api as sm
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Laadi Iris andmestik
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target, name='species')

# Standardiseeri tunnused (parandab logit mudeli konvergentsi)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled = pd.DataFrame(X_scaled, columns=X.columns)

# Jaga treening- ja testimisandmestikuks
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.3, random_state=42, stratify=y
)

# Lisa konstant (intercept)
X_train_const = sm.add_constant(X_train)
X_test_const = sm.add_constant(X_test)

# Ehita multinomiaalse logistilise regressiooni mudel
model = sm.MNLogit(y_train, X_train_const)
results = model.fit(disp=False)

# Näita mudeli kokkuvõtet
print("=" * 70)
print("MUDELI KOKKUVÕTE")
print("=" * 70)
print(results.summary())

# Prognoosid treiningandmestikul
y_pred_train = results.predict(X_train_const)
y_pred_train_class = y_pred_train.idxmax(axis=1)

# Prognoosid testimisandmestikul
y_pred_test = results.predict(X_test_const)
y_pred_test_class = y_pred_test.idxmax(axis=1)

# Täpsused
train_accuracy = accuracy_score(y_train, y_pred_train_class)
test_accuracy = accuracy_score(y_test, y_pred_test_class)

print("\n" + "=" * 70)
print("MUDELI JÕUDLUSkõUD")
print("=" * 70)
print(f"Treeningandmestiku täpsus: {train_accuracy:.4f}")
print(f"Testimisandmestiku täpsus: {test_accuracy:.4f}")

print("\n" + "=" * 70)
print("KLASSIFIKATSIOONIARUANNE (TESTANDMESTIK)")
print("=" * 70)
species_names = iris.target_names
print(classification_report(y_test, y_pred_test_class, target_names=species_names))

# Segamaatriks
cm = confusion_matrix(y_test, y_pred_test_class)
print("\n" + "=" * 70)
print("SEGAMAATRIKS")
print("=" * 70)
print(cm)

# Visualiseeri segamaatriksi
plt.figure(figsize=(8, 6))
sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=species_names,
    yticklabels=species_names,
    cbar_kws={'label': 'Count'}
)
plt.title("Segamaatriks: Iris'i liikide ennustamine")
plt.ylabel('Tegelik liik')
plt.xlabel('Ennustatud liik')
plt.tight_layout()
plt.savefig('/home/claude/confusion_matrix.png', dpi=300, bbox_inches='tight')
print("\nSegamaatriks salvestatud: /home/claude/confusion_matrix.png")

# Näita mõne näitega ennustuste tõenäosusi
print("\n" + "=" * 70)
print("NÄITED: ENNUSTUSTE TÕENÄOSUSED")
print("=" * 70)
for idx in range(min(5, len(y_test))):
    print(f"\nNäide {idx + 1}:")
    print(f"  Tegelik liik: {species_names[y_test.iloc[idx]]}")
    print(f"  Ennustatud liik: {species_names[y_pred_test_class.iloc[idx]]}")
    print(f"  Tõenäosused:")
    for class_idx, species in enumerate(species_names):
        prob = y_pred_test[class_idx].iloc[idx]
        print(f"    {species}: {prob:.4f}")
