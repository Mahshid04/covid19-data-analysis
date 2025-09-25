import pandas as pd


df1_data = pd.read_csv('data/01_scraped_data.csv')
df_vac = pd.read_csv('data/vaccinations_global.csv')

df_lastest = df_vac.sort_values('date').groupby('country').tail(1)
df_lastest = df_lastest[["country", "date", "total_vaccinations"]]

country_dic = {
    'United States' : 'USA',
    'South Korea' : 'S. Korea',
    'United Kingdom' : 'UK',
    'United Arab Emirates' : 'UAE'
}

df_lastest['country'] = df_lastest['country'].replace(country_dic) #replacing the names of some countries 

df_new = pd.merge(df1_data, df_lastest, left_on='Country', right_on='country', how='inner')
df_new = df_new.drop(columns=['date','country'])

df_new = df_new.sort_values('Country')
df_new['column number'] = range(1, len(df_new) + 1) # new numbers for column
df_new = df_new.sort_values('column number')

df_new = df_new.fillna("0")
df_new.to_csv('data/02_merge_data.csv',index=False)