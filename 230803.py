# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 13:32:52 2023

@author: Jung
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.arange(6).reshape(3, 2),
                  index = range(0, 3), columns = ['A', 'B'])
print(df)

df.index = ['a', 'b', 'c']
print(df)

df.rename(index = {'a':'A'}, inplace = True)
print(df)

df.columns = ['a', 'b']
print(df)

df.rename(columns = {'a':'col_1', 'b':'val_2'}, inplace = True)
print(df)


import seaborn as sns

font_name = 'C:\\Users\\Jung\\Documents\\python_basic\\NanumGothic.ttf'

from matplotlib import font_manager

fontprop = font_manager.FontProperties(fname = font_name, size = 10)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(np.random.randn(1000).cumsum())
ticks = ax.set_xticks([0, 250, 500, 750, 1000])
labels = ax.set_xticklabels(['하나', '둘', '셋',' 넷', '다섯'],
                             rotation = 30)
plt.xticks(fontproperties = fontprop)
plt.show()


property_candidate = {'이재명':3217161, '윤석열':7745343, '심상정':1406297,
                      '안철수':197985542, '오준호':264067, '허경영':26401367, '이백윤':171800,
                      '옥은호':337062, '김동연':4053544, '김경재':2202623, '조원진':2058661,
                      '김재연':51807, '이경희':149907313, '김민찬':421648}
x = list(property_candidate.keys())
y = np.array(list(map(lambda x: x / 1000, property_candidate.values())))

plt.figure(figsize = (8, 8))
sns.barplot(x = x, y = y)
sns.set_theme(style = 'white', context = 'talk')
plt.xticks(fontproperties = fontprop, rotation = -90)
plt.show()


sns.set_theme(style="white", context="talk")
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True,figsize=(10,8))
fig.subplots_adjust(hspace=0.2)  # adjust space between axes

# plot the same data on both axes
ax1.bar(property_candidate.keys(), list(map(lambda x : x/1000, property_candidate.values())), color = ['yellow', 'cyan', 'pink', 'purple'], alpha = 0.5,
edgecolor = 'black', linewidth = 2.5)
ax2.bar(property_candidate.keys(), list(map(lambda x : x/1000, property_candidate.values())),color = ['yellow', 'cyan', 'pink', 'purple'], alpha = 0.5,
edgecolor = 'black', linewidth = 2.5)

# zoom-in / limit the view to different portions of the data
ax1.set_ylim(120000, 200000)  # outliers only
ax2.set_ylim(0, 30000)  # most of the data

# hide the spines between ax and ax2
ax1.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
#ax1.xaxis.tick_top()
ax1.tick_params(labeltop=False)  # don't put tick labels at the top
ax1.set_title('20 대 대선 후보자 재산 현황 (단위 : 백만원)', fontproperties = fontprop, pad=20)
#ax1.set_ylabel('단위 : 백만원',labelpad=20, fontproperties = fontprop)
ax2.xaxis.tick_bottom()
ax2.set_xticklabels(property_candidate.keys(),fontproperties = fontprop,rotation = 270)

#Y축 양쪽에 빗금 넣기
d = .5  # proportion of vertical to horizontal extent of the slanted line
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle="none", color='k', mec='k', mew=1, clip_on=False)
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)
plt.show()




df = pd.DataFrame(np.arange(6).reshape(3, 2),
                  index = range(0, 3), columns = ['A', 'B'])
print(df)

df_ext = df.reindex(range(5), columns = ['B', 'C', 'A'])
print(df_ext)

df_ext.drop(1, inplace = True)
print(df_ext)

df_ext.drop('C', axis = 'columns', inplace = True)
print(df_ext)

df_ext.drop(3, inplace = True)
print(df_ext)

df = pd.Series([10, 20, 30, 40, 50], index = ['a', 'b', 'c', 'd', 'e'])
print(df[1])
print(df[0:3])
print(df['a':'c'])

df['c':'d'] = 0
print(df)

df = pd.DataFrame(np.arange(3*4).reshape(3, 4), 
                  index = ['A', 'B', 'C'], columns = ['aa', 'bb', 'cc', 'dd'])
print(df)

print(df['aa'])
print(df[['aa','cc','dd']])
print(df[:2])
print(df['A':'B'])
print(df<4)
print(df[df['aa']<=4])

df[df<4]=0
print(df)

print(df.loc[:, 'aa'])
print(df.loc['A':'B', ['aa','cc']])
print(df.iloc[:2, [0, 2]])
print(df.iloc[1, 2])
print(df.iloc[:3, [0]])


pds = pd.Series([10, 20, 30])
#pds[-1] #에러 발생

pds2 = pd.Series([10, 20, 30], index = ['a', 'b', 'c'])
print(pds2[-1])

pds1 = pd.Series(range(5), index = ['a', 'b', 'c', 'd', 'e'])
pds2 = pd.Series(range(1, 10, 2), index = ['a', 'b', 'f', 'g', 'h'])
print(pds1 + pds2)

df1 =  pd.DataFrame(np.arange(3*3).reshape(3,3), 
                  index = ['a', 'b', 'c'], columns = ['가', '나', '다'])
print(df1)

df1.columns = ['AA', 'BB', 'CC']
print(df1)

df2 =  pd.DataFrame(np.arange(4*3).reshape(4,3), 
                  index = ['a', 'b', 'c', 'd'], columns = ['AA', 'BB', 'CC'])
print(df1 + df2)

df3 =  pd.DataFrame(np.arange(12).reshape(3, 4), 
                  index = list('ABC'), columns = list('abcd'))
print(df3)

pds1 = df3.iloc[0]
print(pds1)
print(df3 + pds1)

pds1 = pd.Series([10, 100, 1000, 10000], index = list('abcd'))
print(pds1)
print(df3 + pds1)


url = 'https://raw.githubusercontent.com/Datamanim/pandas/main/lol.csv'
df = pd.read_csv(url, sep = '\t')
print(df)
print(df.info())
print(df.shape)

df_index_list = list(df.index)
print(df_index_list)
print(df.iloc[:, 5])
print(df.iloc[2, 3])


df1 = pd.DataFrame(np.random.randn(12).reshape(3, 4),
                   columns = list('abcd'), index = list('ABC'))
fx = lambda x : x.max() - x.min()
print(df1.apply(fx))
print(df1.max(axis=1)) #column 방향 연산
print(df1.max(axis=0)) #row 방향 연산

print(df1.a.max(), df1['a'].max(), df1.max()['a'])

fm = lambda x: '{:.2f}'.format(x) #소수점 둘째자리에서 반올림
print(df1.applymap(fm))


frame = pd.DataFrame(np.arange(9).reshape(3, 3), index = list('abc'),
                     columns = ['Ohio', 'Texas', 'California'])
print(frame)

states = ['Texas', 'Utah', 'California']
print(frame.reindex(columns = states))
print(frame.drop(['Ohio', 'California'], axis=1))
print(frame.drop(['a', 'b'], axis=0))

data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data.sum(axis=0))
print(data.sum(axis=1))
print(data.mean(axis=1))
print(data.div(10, axis=0))
print(data.div(data.sum(axis=1), axis=0) * 100)


df = pd.DataFrame(np.arange(12).reshape(3,4),
                  columns = list('bcda'), index = list('DBA'))
print(df)
print(df.sort_index())
print(df.sort_index(axis=1))

df2 = df.sort_index(axis=1, ascending=False)
print(df2)

print(df2.sort_values(by='D', axis=1))
print(df2.sort_values(by='c', ascending=False))

df = pd.DataFrame({'a':[-2, -3, -5, 1], 'b':[20, -29, -40, 20]})
print(df.sort_values(by='a'))


pds = pd.Series(np.arange(5), index=list('abcda'))
print(pds['a'])
print(pds['b'])
print(pds.index.is_unique)

pds1 = pd.Series(['a', 'b', 'c','d','a', 'b', 'c','d', 'e', 'f', 'b'])
print(pds1.unique())
print(pds1.value_counts())
print(pds1.value_counts(ascending=True))
print(pds1.value_counts(sort=False))
print(pds1.isin(['a', 'b']))

mask = pds1.isin(['a', 'b'])
print(pds1[mask])

df = pd.read_csv('C:\\Users\\Jung\\Documents\\python_basic\\example_data\\ex1.csv')
print(df)
print(pd.read_table('C:\\Users\\Jung\\Documents\\python_basic\\example_data\\ex1.csv', sep=','))

print(pd.read_csv('./example_data/ex2.csv', header=None))
df = pd.read_csv('./example_data/ex2.csv', names=['a','b','c','d','ma'])
print(df)

names_=['a','b','c','d','ma']
df = pd.read_csv('./example_data/ex2.csv', names = names_, index_col='ma')
print(df)

df = pd.read_table('./example_data/ex3.txt', sep='\s+') # +: 최대한 많이 구분하라
print(df)
print(df.info())
print(df.describe())

df = pd.read_csv('./example_data/ex4.csv', skiprows=[0, 2, 3])
print(df)

df = pd.read_csv('./example_data/ex5.csv', index_col=0)
print(df)










