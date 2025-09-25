import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("data/01_scraped_data.csv")

df = df[["TotalCases", "TotalDeaths", "TotalRecovered", "Population"]]
df = df.dropna(subset=["TotalCases", "TotalDeaths", "TotalRecovered", "Population"])

plt.figure(figsize=(12,7))

corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")


plt.title("Correlation Heatmap of COVID-19 Metrics")
plt.savefig("outputs/correlationHeatmap.png")


plt.show()

