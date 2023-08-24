# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 11:22:54 2023

@author: Jung
"""

import pandas as pd
import seaborn as sns
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures


iris = sns.load_dataset('iris')
print(iris)
print(type(iris))

fig = plt.figure(figsize=(6, 4))
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')
ax.axis('equal')

# Draw features matrix
ax.vlines(range(6), ymin=0, ymax=9, lw=1)
ax.hlines(range(10), xmin=0, xmax=5, lw=1)
font_prop = dict(size=12, family='monospace')
ax.text(-1, -1, "Feature Matrix ($X$)", size=14)
ax.text(0.1, -0.3, r'n_features $\longrightarrow$', **font_prop)
ax.text(-0.1, 0.1, r'$\longleftarrow$ n_samples', rotation=90,
        va='top', ha='right', **font_prop)

# Draw labels vector
ax.vlines(range(8, 10), ymin=0, ymax=9, lw=1)
ax.hlines(range(10), xmin=8, xmax=9, lw=1)
ax.text(7, -1, "Target Vector ($y$)", size=14)
ax.text(7.9, 0.1, r'$\longleftarrow$ n_samples', rotation=90,
        va='top', ha='right', **font_prop)

ax.set_ylim(10, -2)

fig.savefig('05.02-samples-features.png')
plt.show()


fruits = ['apple', 'orange', 'apple', 'apple']*2
df = pd.DataFrame(fruits)

cat_ddf = df[0].astype('category')
print(cat_ddf)
print(cat_ddf.cat.codes)
print(cat_ddf.cat.categories)


x = [{'city':'seoul', 'temp':10.0}, {'city':'Dubai', 'temp':33.5}, {'city':'LA', 'temp':20.0}]
vec = DictVectorizer(sparse = False) # 인스턴스 오브젝트 = 클래스(sparse = False)
print(vec.fit_transform(x))
print(vec)

vec_sparse_true = DictVectorizer(sparse = True)
print(vec_sparse_true)

x_sparse = vec_sparse_true.fit_transform(x)
print(x_sparse) # 1이 있는 것만 압축해서 저장한다
print(x_sparse.toarray())

D = [{'foo':1, 'bar':2}, {'foo':3, 'baz':1}]
V = DictVectorizer(sparse = False)
print(V.fit_transform(D))
print(V.get_feature_names_out())

D = [{'foo':1, 'bar':2}, {'foo':3, 'baz':1}]
vec = DictVectorizer()
x = vec.fit_transform(D)
print(x)


text=['떴다 떴다 비행기 날아라 날아라',
      '높이 높이 날아라 우리 비행기',
      '내가 만든 비행기 날아라 날아라',
      '멀리 멀리 날아라 우리 비행기']

vec2 = CountVectorizer()
tex = vec2.fit_transform(text)
print(vec2.get_feature_names_out())

df = pd.DataFrame(tex.toarray(), columns = vec2.get_feature_names_out())
print(df)

tfidf = TfidfVectorizer()
x2 = tfidf.fit_transform(text)
print(x2)
df = pd.DataFrame(x2.toarray(), columns = tfidf.get_feature_names_out())
print(df)


x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 3, 1, 4, 8])
plt.plot(x, y, 'o')
plt.show()

poly = PolynomialFeatures(degree = 3, include_bias = True)
x1 = poly.fit_transform(x[:, np.newaxis])
print(x1)

print(poly.get_feature_names_out())
print(x[:, np.newaxis])


data = pd.Series(np.random.randn(9), index = [['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],
                                              [1, 2, 3, 1, 3, 1, 2, 2, 3]])
print(data)
print(data.index)
print(data['b'])
print(data['b':'c'])
print(data.loc[['b', 'c']])
print(data.loc[:, 2])
print(data.unstack())
print(data.unstack().stack())


frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
                     index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                     columns=[['Ohio', 'Ohio', 'Colorado'],
                              ['Green', 'Red', 'Green']])

print(frame)

frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
print(frame)
print(frame['Ohio'])
print(frame.swaplevel('key1', 'key2'))
print(frame.sort_index(level=1))
print(frame.sort_index(level=0))
print(frame.sum(level='key2'))
print(frame.sum(level='color', axis=1))


df1 = pd.DataFrame({'key':['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1':range(7)})

df2 = pd.DataFrame({'key':['a', 'b', 'd'],
                    'data2':range(3)})
print(df1)
print(df2)

print(pd.merge(df1, df2))
print(pd.merge(df1, df2, on='key'))


df3 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})
df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'],
                    'data2': range(3)})

print(df3)
print(df4)

print(pd.merge(df3, df4, left_on = 'lkey', right_on = 'rkey'))
print(pd.merge(df1, df2, how = 'outer'))
print(pd.merge(df1, df2))
      

df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                    'data1': range(6)})
df2 = pd.DataFrame({'key': ['a', 'b', 'a', 'b', 'd'],
                    'data2': range(5)})

print(df1)
print(df2)

print(pd.merge(df1, df2, on='key', how = 'left') )
print(pd.merge(df1, df2, how = 'inner'))


left = pd.DataFrame({'key1': ['foo', 'foo', 'bar'],
                     'key2': ['one', 'two', 'one'],
                     'lval': [1, 2, 3]})
right = pd.DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
                      'key2': ['one', 'one', 'one', 'two'],
                      'rval': [4, 5, 6, 7]})

print(left)
print(right)

print(pd.merge(left, right, on=['key1','key2'], how = 'outer'))
print(pd.merge(left, right, on='key1'))
print(pd.merge(left, right, on='key1', suffixes=('_left', '_right')))


left1 = pd.DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],
                      'value': range(6)})
right1 = pd.DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])

print(left1)
print(right1)

print(pd.merge(left1, right1, left_on='key', right_index=True))
print(pd.merge(left1, right1, left_on='key', right_index=True, how = 'outer'))


lefth = pd.DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio',
                               'Nevada', 'Nevada'],
                      'key2': [2000, 2001, 2002, 2001, 2002],
                      'data': np.arange(5.)})
righth = pd.DataFrame(np.arange(12).reshape((6, 2)),
                      index=[['Nevada', 'Nevada', 'Ohio', 'Ohio',
                              'Ohio', 'Ohio'],
                             [2001, 2000, 2000, 2000, 2001, 2002]],
                      columns=['event1', 'event2'])

print(lefth)
print(righth)

print(pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True))
print(pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True, how = 'outer'))


left2 = pd.DataFrame([[1., 2.], [3., 4.], [5., 6.]],
                     index=['a', 'c', 'e'],
                     columns=['Ohio', 'Nevada'])
right2 = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],
                      index=['b', 'c', 'd', 'e'],
                      columns=['Missouri', 'Alabama'])

print(left2)
print(right2)

print(left2.join(right2, how='outer'))


arr = np.arange(12).reshape(3, 4)
print(np.concatenate([arr, arr], axis=1))


s1 = pd.Series([0, 1], index=['a', 'b'])
s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = pd.Series([5, 6], index=['f', 'g'])

print(s1)
print(s2)
print(s3)

print(pd.concat([s1, s2, s3]))
print(pd.concat([s1, s2, s3], axis=1))

s4 = pd.concat([s1, s3])
print(pd.concat([s1, s4], axis=1))
print(pd.concat([s1, s4], axis=1, join='inner'))

result = pd.concat([s1, s1, s3], keys=['one', 'two', 'three'])
print(result)
print(result.unstack())
print(pd.concat([s1, s1, s3], keys=['one', 'two', 'three'], axis=1))
