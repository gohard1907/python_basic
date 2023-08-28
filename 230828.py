# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 14:16:39 2023

@author: Jung
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cctv = pd.read_csv('./CCTV_Seoul.csv', sep=',', skiprows = [1], encoding='cp949')
pop = pd.read_csv('./POP_Seoul.csv', sep=',', skiprows = [0, 2])

cctv_new = cctv[['구분', '총계']]
pop_new = pop[['동별(2)', '계 (명)']]

cctv_new = cctv_new.rename(columns = {'구분': 'gu', '총계':'cctv_total'})
pop_new = pop_new.rename(columns={'동별(2)': 'gu', '계 (명)':'pop_total'})

cctv_new['cctv_total'] = cctv_new['cctv_total'].str.replace(',', '').astype(int)
cctv_new['gu'] = cctv_new['gu'].str.replace(' ', '')

data = pd.merge(cctv_new, pop_new, on = 'gu')

print(data.head())


from sklearn.linear_model import LinearRegression

x = data.pop_total[:, np.newaxis]
y = data.cctv_total

model = LinearRegression()
model.fit(x, y)
print(model.coef_)
print(model.intercept_)

data['predict_lr'] = model.predict(x)
data['res'] = data.cctv_total - data.predict_lr # 잔차
print(data.head())

data_sort = data.sort_values(by = 'res', ascending = False)
data_sort = data_sort.reset_index(drop = True)
print(data_sort.head())


from matplotlib import font_manager
font_path = './NanumGothic.ttf'
fontprop = font_manager.FontProperties(fname = font_path, size = 15)

plt.figure(figsize=(8,8))
plt.scatter(data_sort.pop_total, data_sort.cctv_total, c = data_sort.res, s = 50) 
# c = 색깔의 범위, s = 동그라미 사이즈
plt.plot(data_sort.pop_total, data_sort.predict_lr, ls = '-', lw = 1, color = 'r')

for n in range(3):
    plt.text(data_sort.loc[n, 'pop_total']*1.02, data_sort.loc[n, 'cctv_total']*1.02, 
             data_sort.loc[n, 'gu'], fontsize = 10, fontproperties = fontprop) 
# plt.text(x위치, y위치, 텍스트문자)

for n in range(23, 25):
    plt.text(data_sort.loc[n, 'pop_total']*1.02, data_sort.loc[n, 'cctv_total']*1.02, 
             data_sort.loc[n, 'gu'], fontsize = 10, fontproperties = fontprop) 

plt.colorbar()
plt.grid()
plt.ylabel('CCTV 개수', fontproperties = fontprop)
plt.xlabel('인구 수', fontproperties = fontprop) 
plt.show()


df = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
                   'key2' : ['one', 'two', 'one', 'two', 'one'],
                   'data1' : [1,2,3,4,5],
                   'data2' : [10,20,30,40,50]})

grouped = df['data1'].groupby(df['key1'])
print(grouped.sum())
print(grouped.mean())
print(df['data1'].groupby(df['key2']).sum())

sums = df['data1'].groupby([df['key1'], df['key2']]).sum()
print(sums)

means = df['data2'].groupby([df['key1'], df['key2']]).mean()
print(means)

def grouping(data):
    sums = df['data1'].groupby([df['key1'], df['key2']]).sum()
    means = df['data1'].groupby([df['key1'], df['key2']]).mean()
    return sums, means

print(grouping(df))

def grouping2(data):
    sums = df.groupby(['key1', 'key2']).sum()
    sizes = df.groupby(['key1', 'key2']).size()
    means = df.groupby(['key1', 'key2']).mean()
    return sums, sizes, means

print(grouping2(df))


df.index = ['k', 'k', 'k', 'j', 'j']
grouped = df['data1'].groupby(df['key1'])
for i, j in grouped:
    print(i)
    print('-'*20)
    print(j)
    print('+'*20)

grouped = df.groupby(lambda x : x) # x에는 df의 인덱스 값이 자동으로 들어감
for i, j in grouped:
    print(i)
    print('-'*20)
    print(j)
    print('+'*20)


df = pd.DataFrame({'Animal': ['Falcon', 'Falcon',
                              'Parrot', 'Parrot'],
                   'Max_Speed': [380., 370., 24., 26.]})

speed_sum = df['Max_Speed'].groupby(df['Animal']).sum()
speed_mean = df['Max_Speed'].groupby(df['Animal']).mean()

print(speed_sum)
print(speed_mean)

arrays = [['Falcon', 'Falcon', 'Parrot', 'Parrot'],
          ['Captive', 'Wild', 'Captive', 'Wild']]
index = pd.MultiIndex.from_arrays(arrays, names=('Animal', 'Type'))
df = pd.DataFrame({'Max_Speed': [350., 390., 20., 30.]},
                  index=index)

print(df.groupby(level=0).sum())
print(df.groupby(level=1).sum())

gpd = df.Max_Speed.groupby(level = 0)
print(gpd.mean())
print(gpd.min())
print(df.groupby(level = 'Animal').mean())


list_s = [[1, 2, 3], [1, None, 4], [2, 1, 3], [1, 2, 2]]
df = pd.DataFrame(list_s, columns=["a", "b", "c"])

print(df.groupby(by=['b']).sum()) # NaN 제외
print(df.groupby(by=['b'], dropna=False).sum())


df = pd.DataFrame({'상품번호' : ['P1', 'P1', 'P2', 'P2'],
                   '수량' :     [2, 3, 5, 10]})

print(df.groupby(by=['상품번호']).sum())
print(df.groupby(by=['상품번호'], as_index=False).count())


df = pd.DataFrame({'고객번호' : ['C1', 'C2', 'C2', 'C2'],
                   '상품번호' : ['P1', 'P1', 'P2', 'P2'],
                   '수량' :     [2, 3, 5, 10]})

print(df.groupby(['고객번호', '상품번호'], as_index=False).sum())


df = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
                   'key2' : ['one', 'two', 'one', 'two', 'one'],
                   'data1' : [1,2,3,4,5],
                   'data2' : [10,20,30,40,50]})

for (k1, k2), group in df.groupby(['key1', 'key2']):
    print(k1, k2)
    print(group)
    print('===========')

g = list(df.groupby(['key1']))
print(g[0][1])

d_g = dict(g)
print(d_g)
print(d_g['b'])

print(df.groupby(['key1', 'key2'])['data2'].sum())


people = pd.DataFrame(np.random.randn(5, 5),
                      columns=['a', 'b', 'c', 'd', 'e'],
                      index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
people.iloc[2:3, [1, 2]] = np.nan # Add a few NA values

mapping = {'a': 'red', 'b': 'red', 'c': 'blue',
           'd': 'blue', 'e': 'red', 'f' : 'orange'}

by_column = people.groupby(mapping, axis = 1)
print(by_column.sum())

map_series = pd.Series(mapping)
print(people.groupby(map_series, axis=1).count())
print(people.groupby(len).sum())

key_list = ['one', 'one', 'one', 'two', 'two']
print(people.groupby([len, key_list]).min())
for i, j in people.groupby([len, key_list]):
    print(i)
    print(j)
    print('===========================')


columns = pd.MultiIndex.from_arrays([['US', 'US', 'US', 'JP', 'JP'],
                                    [1, 3, 5, 1, 3]],
                                    names=['cty', 'tenor'])
h_df = pd.DataFrame(np.random.randn(4, 5), columns=columns)

print(h_df.groupby(level = 'cty', axis = 1).count())



tips = pd.read_csv('./tips.csv')

gpd = tips.groupby(['day', 'smoker'])
for i, gr in gpd:
    print(i)

print(gpd['tip_pct'].agg('mean'))
print(gpd['tip_pct'].agg(['mean', 'std']))
print(gpd['tip_pct'].agg([('foo', 'mean'), ('bar', np.std)]))














