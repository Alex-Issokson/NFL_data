#NFL Stats


# Import scraping modules
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Import data manipulation modules
import pandas as pd
import numpy as np
# Import data visualization modules
import matplotlib as mpl
import matplotlib.pyplot as plt

pip install seaborn

import seaborn as sns

url1 = 'https://www.pro-football-reference.com/years/2021/fantasy.htm'
html1 = urlopen(url1)
stats_page = BeautifulSoup(html1)

# Collect table headers
column_headers = stats_page.findAll('tr')[1]
column_headers = [i.getText() for i in column_headers.findAll('th')]

print(column_headers)

# Collect table rows
rows = stats_page.findAll('tr')[1:]
# Get stats from each row
player_stats = []
for i in range(len(rows)):
  player_stats.append([col.getText() for col in rows[i].findAll('td')])

print(player_stats[1])

# Create DataFrame from our scraped data
data = pd.DataFrame(player_stats, columns=column_headers[1:])

data.head()

data.columns

new_columns = data.columns.values
new_columns[8] = 'Passing_Yds'
new_columns[12] = 'Rushing_Yds'
new_columns[17] = 'Receiving_Yds'
new_columns[-10] = 'Total_TD'
data.columns = new_columns

data['Receiving_Yds'] = pd.to_numeric(data['Receiving_Yds'])
data['Tgt'] = pd.to_numeric(data['Tgt'])
data['FantPt'] = pd.to_numeric(data['FantPt'])
data['Rec'] = pd.to_numeric(data['Rec'])
data['Total_TD'] = pd.to_numeric(data['Total_TD'])

categories = ['Receiving_Yds', 'Tgt', 'FantPt', 'Rec']

WR = data.loc[data['FantPos'] == 'WR']

WR.head()

data_radar = WR[['Player', 'Tm'] + categories]
data_radar.head() 

data_radar.dtypes

sns.scatterplot(x = 'Receiving_Yds', y = 'Tgt', data = WR)

RB = data.loc[data['FantPos'] == 'RB']

data_radar2 = RB[['Player', 'Tm'] + categories]
data_radar2.head() 

data_radar2.dtypes

sns.regplot(x = 'Rec', y = 'FantPt', data = RB[:40])

data["Fantasy_Points"] = 0
