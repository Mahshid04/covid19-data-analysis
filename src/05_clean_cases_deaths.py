import pandas as pd


df = pd.read_csv('data/05_cases_deaths.csv')
df = df[["country", "date", "total_cases"]]
df = df.dropna(subset=["country", "date", "total_cases"])


df['date_date'] = pd.to_datetime(df['date'])
df['year'] = df['date_date'].dt.year

df = df[df['country'].isin(["United States","Iran","Germany","China"])]

df.to_csv('data/05_cases_deaths.csv',index=False)

