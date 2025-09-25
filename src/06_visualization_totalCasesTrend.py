import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates



df = pd.read_csv('data/05_cases_deaths.csv')

df['date_date'] = pd.to_datetime(df['date_date'], errors='coerce')
df = df.dropna(subset=['date_date'])

df['total_cases_million'] = df['total_cases'] / 1_000_000


plt.figure(figsize=(12,7))

sns.lineplot(x="date_date", y="total_cases_million", hue="country", data=df)

plt.gca().xaxis.set_major_locator(mdates.YearLocator())   
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))  

plt.title("COVID-19 Total Cases Trend (US, Iran, Germany, China)")
plt.ylabel("Total Cases (millions)")
plt.xlabel("Year")


plt.savefig("outputs/TotalCasesTrend.png")

plt.show()

