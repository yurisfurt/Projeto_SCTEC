from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

BASE = Path(__file__).resolve().parent
GRAFICOS = BASE / "graficos"
GRAFICOS.mkdir(exist_ok=True)
sns.set_theme(style="whitegrid")

df_dep = pd.read_csv(BASE / "query_01.csv")
df_reg = pd.read_csv(BASE / "query_02.csv")

print("Banco de dados departamentos:")
print(df_dep.head())
print("Banco de dados regiões:")
print(df_reg.head())

departamento = df_dep.groupby("DEPARTMENT_NAME")["SALARY"].mean().sort_values(ascending=False)
cargo = df_dep.groupby("JOB_TITLE")["SALARY"].max().sort_values(ascending=False).head(10)
city = df_reg.groupby("CITY")["SALARY"].mean().sort_values()

print(f"Salário médio por departamento: {departamento}")
print("")
print(f"Maiores salários por cargo: {cargo}")
print("")
print(f"Média de salário por cidade: {city}")

ax = departamento.plot(kind="bar", figsize=(10, 6), color="steelblue", edgecolor="black")
ax.set_title("Salário médio por departamento")
ax.set_xlabel("Departamento")
ax.set_ylabel("Salário médio (USD)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(GRAFICOS / "media_salario_por_departamento.png")
plt.close()
print("Gráfico salvo: graficos/media_salario_por_departamento.png")

ax = city.plot(kind="barh", figsize=(10, 6), color="seagreen", edgecolor="black")
ax.set_title("Média de salário por cidade")
ax.set_xlabel("Salário (USD)")
ax.set_ylabel("Cidade")
plt.tight_layout()
plt.savefig(GRAFICOS / "media_salario_por_cidade.png")
plt.close()
print("Gráfico salvo: graficos/media_salario_por_cidade.png")