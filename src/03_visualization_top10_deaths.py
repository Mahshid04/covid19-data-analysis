import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('data/02_merge_data.csv').sort_values('TotalDeaths',ascending=False).head(10)
df = df.dropna(subset=['TotalDeaths'])


plt.style.use("fivethirtyeight")
plt.figure(figsize=(12,7))
plt.subplots_adjust(bottom=0.15) 

sns.barplot(x='Country', y='TotalDeaths', alpha = 0.8, data=df)


plt.title("Top 10 Countries with Highest COVID-19 Deaths")
plt.xlabel("Country")
plt.ylabel("Total Deaths")
plt.xticks(rotation = 15)
plt.savefig("outputs/Top10_deaths.png")
plt.show()
