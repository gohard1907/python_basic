# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 17:27:38 2023

@author: Jung
"""

import pandas as pd

df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']])
print(df)

df.index = ['학생1', '학생2']
df.columns = ['연령', '남녀', '소속']
print(df)

print(df.index)
print(df.columns)


df2 = df
print(df2)

df3 = df[:]
print(df3)

df2.drop('학생1', inplace = True)
print(df2)
print(df)
print(df3)

df = df3[:]
df3.drop('학생1', inplace = True)
print(df3)
print(df)


exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)

df.set_index('이름', inplace=True)
print(df)
print('\n')

a = df.loc['서준', '음악']
print(a)
b = df.iloc[0, 2]
print(b)
print('\n')

c = df.loc['서준', ['음악', '체육']]
print(c)
d = df.iloc[0, [2, 3]]
print(d)
e = df.loc['서준', '음악':'체육']
print(e)
f = df.iloc[0, 2:]
print(f)
print('\n')

g = df.loc[['서준', '우현'], ['음악', '체육']]
print(g)
h = df.iloc[[0, 1], [2, 3]]
print(h)
i = df.loc['서준':'우현', '음악':'체육']
print(i)
j = df.iloc[0:2, 2:]
print(j)


df.loc['영'] = 0
print(df)
df.loc['동규'] = [90, 80, 70, 60]
print(df)


exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)

df.set_index('이름', inplace=True)
print(df)


df.iloc[0][3] = 80
print(df)
print('\n')

df.iloc[0,3] = 1080
print(df)
print('\n')

df.loc['서준']['체육'] = 90
print(df)
print('\n')

df.loc['서준', '체육'] = 100
print(df)
print('\n')

df.loc['서준', ['음악', '체육']] = 50
print(df)
print('\n')

df.loc['서준', ['음악', '체육']] = 100, 50
print(df)


exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)
print('\n')

df = df.transpose()
print(df)
print('\n')

df = df.T
print(df)


ndf = df.set_index(['이름'])
print(ndf)
print(ndf.set_index(['음악']))
print(ndf.set_index(['수학', '음악']))


dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)
print('\n')

new_index = ['r0', 'r1', 'r2', 'r3', 'r4']
ndf = df.reindex(new_index)
print(ndf)
print('\n')

new_index = ['r0', 'r1', 'r2', 'r3', 'r4']
ndf2 = df.reindex(new_index, fill_value=0)
print(ndf2)

print(df.reset_index())
print(df)
print(df.sort_index(ascending = False))
print(df.sort_index(ascending = True))
print(df.sort_index())
print(df.sort_values(by = 'c1', ascending = False))


import numpy as np

student1 = pd.Series({'국어':np.nan, '영어':80, '수학':90})
print(student1)


import seaborn as sns

titanic = sns.load_dataset('titanic')
print(titanic)
print(titanic.info())

df = titanic.loc[:, ['age', 'fare']]
print(df)

add_df = df+10
print(add_df)
print(add_df - df)








