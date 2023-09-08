# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 13:30:21 2023

@author: Jung
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from bs4 import BeautifulSoup
import requests
import re

url = 'https://en.wikipedia.org/wiki/List_of_American_exchange-traded_funds'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'lxml')
rows = soup.select('div > ul > li')

etfs = {}
for row in rows:
    try:
        etf_name = re.findall('^(.*) \(', row.text)
        etf_market = re.findall('NYSE Arca|Nasdaq', row.text)
        if len(etf_market) == 0:
            row1 = row.text.replace(u'\xa0', u' ')
            etf_market = re.findall('NYSE Arca|Nasdaq', row1)
        etf_ticker = re.findall('([A-Z]{2,4})\)', row.text)
        print(etf_ticker, etf_name, etf_market)

        if (len(etf_ticker) > 0) & (len(etf_market) > 0) & (len(etf_name) > 0):
            etfs[etf_ticker[0]] = [etf_market[0], etf_name[0]]

    except:
        pass
    
print(etfs)
print('\n')

df = pd.DataFrame(etfs)
print(df)


df = pd.read_csv('./auto-mpg.csv', header = None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

print(df.head())
print('\n')
print(df.tail())

print(df.shape)
print(df.info())
print(df.dtypes)

print(df.describe())
print('\n')
print(df.describe(include='all'))
print(df.count())

unique_values = df['origin'].value_counts()
print(unique_values)
print('\n')
print(type(unique_values))

#numeric_columns = df.select_dtypes(include=['float64', 'int64'])
#column_means = numeric_columns.mean()
#print(column_means)

print(df['mpg'].mean())
print(df.mpg.mean())
print('\n')
print(df[['mpg', 'weight']].mean())

print(df['mpg'].median())
print(df['mpg'].max())
print(df['mpg'].min())
print(df['mpg'].std())
print(df[['mpg', 'weight']].corr())


df = pd.read_excel('./남북한발전전력량.xlsx', engine = 'openpyxl')
df_ns = df.iloc[[0, 5], 3:]
df_ns.index = ['South', 'North']
df_ns.columns = df_ns.columns.map(int)

print(df_ns.head())
print('\n')
df_ns.plot()

tdf_ns = df_ns.T
print(tdf_ns.head())
print('\n')
tdf_ns.plot()

tdf_ns.plot(kind = 'bar')

tdf_ns.astype('float').plot(kind='hist')


df = pd.read_csv('./auto-mpg.csv', header = None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

df.plot(x = 'weight', y = 'mpg', kind = 'scatter')

df[['mpg', 'cylinders']].plot(kind = 'box')



df = pd.read_csv('./KR_youtube_trending_data.csv')
print(df.head())

print(df.channelId.value_counts().head(10))
print(df.channelId.value_counts().head(10).index)
print(df[df.channelId.isin(df.channelId.value_counts().head(10).index)])
print(df[df.channelId.isin(df.channelId.value_counts().head(10).index)].channelTitle.unique())
print(df.loc[df.likes<df.dislikes].channelTitle.unique())



import seaborn as sns

df = sns.load_dataset('titanic')

nan_deck = df['deck'].value_counts(dropna=False)
print(nan_deck)

print(df.head().isnull())
print(df.head().notnull())
print(df.head().isnull().sum(axis=0))

missing_df = df.isnull()
for col in missing_df.columns:
    missing_count = missing_df[col].value_counts()

    try:
        print(col, ':', missing_count[True])
    except:
        print(col, ':', 0)

df_thresh = df.dropna(axis = 1, thresh = 500)
print(df_thresh.columns)

df_age = df.dropna(subset=['age'], how = 'any', axis = 0)
print(len(df_age))

print(df['age'].head(10))
mean_age = df['age'].mean()
df['age'].fillna(mean_age, inplace = True)
print(df['age'].head(10))

print(df['embark_town'][825:831])
most_freq = df['embark_town'].value_counts(dropna=True).idxmax()
df['embark_town'].fillna(most_freq, inplace=True)
print(df['embark_town'][825:831])


idx = ['row1', 'row2', 'row3']
col = ['col1', 'col2', 'col3']
data = [[1, 2, 300], [100, 5, 6], [7, 300, np.nan]]

df_ = pd.DataFrame(data, idx, col)
print(df_)
print(df_.idxmax())


df = pd.DataFrame({'c1':['a', 'a', 'b', 'a', 'b'],
                   'c2':[1, 1, 1, 2, 2],
                   'c3':[1, 1, 2, 2, 2]})
df_dup = df.duplicated()

print(df)
print('\n')
print(df_dup)

col_dup = df['c2'].duplicated()
print(col_dup)

df2 = df.drop_duplicates()
print(df2)

df3 = df.drop_duplicates(subset = ['c2', 'c3'])
print(df3)


df = pd.read_csv('./auto-mpg.csv', header = None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

print(df.head(3))
print('\n')

mpg_to_kpl = 1.60934/3.78541

df['kpl'] = df['mpg']*mpg_to_kpl
print(df.head(3))
print('\n')

df['kpl'] = df['kpl'].round(2)
print(df.head(3))


print(df.dtypes)
print(df['horsepower'].unique())

df['horsepower'].replace('?', np.nan, inplace=True)
df.dropna(subset=['horsepower'], axis = 0, inplace = True)
df['horsepower'] = df['horsepower'].astype('float')
print(df.dtypes)

print(df['origin'].unique())
df['origin'].replace({1:'USA', 2:'EU', 3:'JPN'}, inplace = True)
print(df['origin'].unique())
print(df['origin'].dtypes)

df['origin'] = df['origin'].astype('category')
print(df['origin'].dtypes)

df['origin'] = df['origin'].astype('str')
print(df['origin'].dtypes)

print(df['model year'].sample(3))
df['model year'] = df['model year'].astype('category')
print(df['model year'].sample(3))


count, bin_dividers = np.histogram(df['horsepower'], bins=3)
print(bin_dividers)

bin_names = ['저출력', '보통출력', '고출력']

df['hp_bin'] = pd.cut(x = df['horsepower'],
                      bins = bin_dividers,
                      labels = bin_names,
                      include_lowest = True)

print(df[['horsepower', 'hp_bin']].head(15))


