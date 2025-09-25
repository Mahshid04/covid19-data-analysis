import pycountry
import pandas as pd

df = pd.read_csv("data/01_scraped_data.csv")

corrections = {
             'S. Korea' : 'Korea, Republic of',
             'UK' : 'United Kingdom',
             'Russia': 'Russian Federation',
             'Turkey' : 'Türkiye',
             'DPRK' : "Korea, Democratic Peoples's Republic of",
             'UAE' : 'United Arab Emirates',
             'CAR' : 'Central African Republic',
             'Vatican City' : 'Holy See (Vatican City State)'

}

df["Country"] = df["Country"].replace(corrections)

def get_iso3(pre_name):
     try:
         return pycountry.countries.lookup(pre_name).alpha_3
     except:
         return None


df["ISO3"] = df["Country"].apply(get_iso3)

df = df.dropna(subset=['ISO3'])

df.to_csv("data/08_with_iso.csv", index=False)


