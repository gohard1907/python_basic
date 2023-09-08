# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 17:35:44 2023

@author: Jung
"""

import pandas as pd
import numpy as np

seafood = pd.read_excel('./통합 식품영양성분DB_수산물_20230831.xlsx', engine = 'openpyxl')
product = pd.read_excel('./통합 식품영양성분DB_농축산물_20230831.xlsx', engine = 'openpyxl')

seafood = seafood.iloc[:, list(range(14, 57))]
seafood.replace('-', np.nan, inplace=True)
seafood = seafood.astype(float)

s_list = seafood.sum().sort_values(ascending = False).head(10)
s_list = s_list.index.tolist()
#print(s_list)

product = product[['식품명'] + s_list]

for i in product.columns[1:]:
    product[i] = product[i].apply(lambda x: x.strip('()') if x.startswith('(') else x)
    product[i] = product[i].replace(['Tr', '-', 'tr'], '0')
    
product.iloc[:, 1:] = product.iloc[:, 1:].astype(float)
#print(product.info())

for i,j in enumerate(product.columns[1:], start=1):
    print(f'수산물 Top {i} 영양소 : {j}')
    top10_idx = product.sort_values(j, ascending=False).index[:3]
    top10 = product.iloc[top10_idx, 0].values
    print('-'*20)
    print('대체 농축산물')
    for k in top10:
        print(f'- {k}')
    print('='*30)
    
    
file_path = './read_csv_sample.csv'

df1 = pd.read_csv(file_path)
print(df1)
print('\n')

df2 = pd.read_csv(file_path, header=None)
print(df2)
print('\n')

df3 = pd.read_csv(file_path, index_col=None)
print(df3)
print('\n')

df4 = pd.read_csv(file_path, index_col='c0')
print(df4)


df1 = pd.read_excel('./남북한발전전력량.xlsx', engine = 'openpyxl')
df2 = pd.read_excel('./남북한발전전력량.xlsx', engine = 'openpyxl', header = None)
# header = None 옵션, sheet_name = 0

print(df1)
print('\n')
print(df2)


url = './sample.html'

tables = pd.read_html(url)

print(len(tables))
print('\n')

for i in range(len(tables)):
    print('tables[%s]' % i)
    print(tables[i])
    print('\n')

df = tables[1]

df.set_index(['name'], inplace=True)
print(df)