# 한국은행 


import pandas as pd
import json
from pandas import json_normalize
import requests


url0 = "http://ecos.bok.or.kr/api/StatisticSearch/idkey/json/kr/1/300/010Y002/MM/201101/202202/AAAA11"

response = requests.get(url0).text



df_json = json.loads(response)

df_row = df_json['StatisticSearch']['row']
df_row

df = json_normalize(df_row)

df.head()

df.info()


df.to_excel('money.xlsx', index=False)

df['DATA_VALUE'] = pd.to_numeric(df['DATA_VALUE'])

df['TIME']

pd.to_datetime(df['TIME'], format='%Y%m')

df['TIME'] = pd.to_datetime(df['TIME'], format='%Y%m')

df.info()

df_master = df[['DATA_VALUE','TIME']]

df_master.info()

# lag operation
df_master['diff'] = (df_master['DATA_VALUE'] - df_master['DATA_VALUE'].shift())
df_master

import matplotlib.pyplot as plt
import seaborn as sns


fig, ax1 = plt.subplots(figsize=(10,6))

# axis 1
ax1.set_title('high powered money')
ax1.set_xlabel('date')
ax1.set_ylabel('HP money')
ax1 = sns.lineplot(x = 'TIME', y = 'diff', data = df_master, alpha = 0.4)
ax1.axhline(0.0)


# axis 2
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Difference')
ax2 = sns.(x = 'TIME', y = 'DATA_VALUE', data = df_master)
ax2.tick_params(axis = 'y')

plt.show()
