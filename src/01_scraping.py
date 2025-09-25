from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd

service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get('https://www.worldometers.info/coronavirus/#countries')

table = driver.find_element(By.ID, "main_table_countries_today")
rows = table.find_elements(By.TAG_NAME, "tr")

dataSet = []

for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    if len(cells) >= 8:
        row = {
            "column number": cells[0].text,
            "Country": cells[1].text.replace(',',''),
            "TotalCases": cells[2].text.replace(',',''),
            "TotalDeaths": cells[3].text.replace(',',''),
            "TotalRecovered": cells[4].text.replace(',',''),
            "Tot Cases/1M pop": cells[5].text.replace(',',''),
            "Deaths/1M pop": cells[6].text.replace(',',''),
            "Population": cells[7].text.replace(',','')
        } 
        if cells[0].text:
           dataSet.append(row)
    else:
        continue
     
df = pd.DataFrame(dataSet)
df = df.fillna('N/A')
df = df.replace('', 'N/A')
print(df)
df.to_csv('data/01_scraped_data.csv',index=False)
