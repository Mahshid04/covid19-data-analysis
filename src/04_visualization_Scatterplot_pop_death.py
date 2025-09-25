import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('data/02_merge_data.csv')
df = df.dropna(subset=['TotalDeaths'])
df.Population= df.Population.astype(int)

plt.figure(figsize=(12,7),dpi=100)

sns.scatterplot(x ='Population', y ='TotalDeaths',s=50, data=df)

plt.xscale("log")
plt.yscale("log")

plt.title("Scatterplot of Population vs Total Deaths")
plt.xlabel("Population")
plt.ylabel("Total Deaths")
plt.savefig("outputs/Scatterplot_pop_death.png")
plt.show()
