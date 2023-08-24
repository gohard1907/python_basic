# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 18:17:18 2023

@author: Jung
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy import nan as NA


def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.dot(x, w) + b
    if tmp < 0:
        return 0
    else:
        return 1

print(AND(0, 0))
print(AND(0, 1))
print(AND(1, 0))
print(AND(1, 1))

def NAND(x1, x2): # Not AND
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.dot(x, w) + b
    if tmp < 0:
        return 0
    else:
        return 1

print(NAND(0, 0))
print(NAND(0, 1))
print(NAND(1, 0))
print(NAND(1, 1))

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.dot(x, w) + b
    if tmp < 0:
        return 0
    else:
        return 1

print(OR(0, 0))
print(OR(0, 1))
print(OR(1, 0))
print(OR(1, 1))

def XOR(x1, x2): # 다르면 참, 같으면 거짓
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

print(XOR(0, 0))
print(XOR(0, 1))
print(XOR(1, 0))
print(XOR(1, 1))


x = np.arange(-5, 5, 0.1)
y = x > 0
print(y)
print(y.astype(int))

def step_func(x):
    y = x > 0
    y = y.astype(int)
    return y

plt.plot(x, step_func(x))
plt.show()

def sigmoid(x):
    return 1/(1+np.exp(-x))

plt.plot(x, sigmoid(x))
plt.show()

y1 = sigmoid(x)
y2 = step_func(x)

plt.plot(x, y1, label = 'sigmoid')
plt.plot(x, y2, linestyle = '--', label = 'step_function')
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-0.1, 1.1)
plt.show()

def relu(x):
    return np.maximum(0, x) # x = -10 -> 0, x = 10 -> 10

plt.plot(x, relu(x))
plt.show()

x1 = np.linspace(-1, 2, 20)
x2 = -x1 + 0.5
plt.plot(x1, x2)
plt.show()

plt.figure(figsize=(8,6))
plt.plot(x1, x2)
plt.show()

plt.axvline(x=0,color='k')
plt.axhline(y=0,color='k')
plt.scatter([0],[0],marker='o',color='r')
plt.scatter([1,0,1],[0,1,1],marker='^',color='r')
plt.xlabel("x1") # x축 이름
plt.ylabel("x2") # y축 이름
plt.fill_between(x1,x2,-2, alpha=0.5) # y값에서 y축의 -3 까지의 값들에 대해 색깔칠해준다.
plt.grid()
plt.show()

x1 = np.arange(-1, 3, 0.1)
x2 = -x1 + 0.5
plt.axvline(x=0, color = 'b')  # draw x =0 axes
plt.axhline(y=0, color = 'b')   # draw y =0 axes
plt.xlabel("X1") # x축 이름
plt.ylabel("X2") # y축 이름

plt.scatter([0,1],[0,1],marker='o',color='r', s=120)
plt.scatter([1,0],[0,1],marker='^',color='r', s=120)
plt.xlim(-1,2)
plt.ylim(-1,2)
plt.show()



string_data = pd.Series(['a', 'b', np.nan, 'c'])
print(string_data)
print(pd.isnull(string_data))

string_data[0] = None
print(string_data)
print(pd.isnull(string_data))

data = pd.Series([1, NA, 3.5, NA, 7])
print(data)
print(data.dropna())

data = pd.DataFrame([[1, 6.5, 3], [1, NA, NA], [NA, NA, NA], [NA, 6.5, 3]])
print(data)
print(data.dropna())
print(data.dropna(how='all'))

data[4] = NA
print(data)
print(data.dropna(how='all', axis = 1))

df = pd.DataFrame(np.random.randn(7,3))
print(df)

df.iloc[:4, 1] = NA
df.iloc[:2, 2] = NA
print(df)
print(df.dropna())
print(df.dropna(thresh=2)) # NaN이 두 개인 행만 지움
print(df.dropna(thresh=4, axis = 1))
print(df.fillna(0.7))
print(df.fillna({1:0.5, 2:0.0}))

df = pd.DataFrame(np.random.randn(6, 3))
df.iloc[2:, 1] = NA
df.iloc[4:, 2] = NA
print(df)
print(df.fillna(method='ffill'))
print(df.fillna(method='ffill', limit=2))
print(df.fillna(df.mean())) # 해당 열의 평균값으로 채움

data = pd.DataFrame({'k1':['one', 'two']*3 + ['two'], 'k2':[1, 1, 2, 3, 3, 4, 4]})
print(data)
print(data.duplicated())
print(data.drop_duplicates())

data['v1'] = range(7)
print(data)
print(data.drop_duplicates(['k1']))
print(data.drop_duplicates(['k1', 'k2']))
print(data.drop_duplicates(['k1', 'k2'], keep = 'last'))


data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon',
                              'Pastrami', 'corned beef', 'Bacon',
                              'pastrami', 'honey ham', 'nova lox'],
                     'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})

meat_to_animal = {
  'bacon': 'pig',
  'pulled pork': 'pig',
  'pastrami': 'cow',
  'corned beef': 'cow',
  'honey ham': 'pig',
  'nova lox': 'salmon'
}

lowercased = data['food'].str.lower()
print(lowercased)
lowercased.map(meat_to_animal)
data['animal'] = lowercased.map(meat_to_animal)
print(data)

def match_animal(my_df, my_dict):
    lowercased = my_df.iloc[:, 0].str.lower()
    lowercased.map(my_dict)
    my_df['animal'] = lowercased.map(my_dict)
    return my_df

print(match_animal(data, meat_to_animal))


data = pd.Series([1., -999., 2., -999., -1000., 3.])
print(data)
print(data.replace(-999., np.nan))
print(data.replace([-999., -1000.], np.nan))
print(data.replace([-999., -1000.], [np.nan, 0]))
print(data.replace({-999.:np.nan, -1000.:0}))

data = pd.DataFrame(np.arange(12).reshape((3, 4)), index = ['Ohio', 'Colorado', 'New York'],
                    columns = ['one', 'two', 'three', 'four'])

print(data)

tf = lambda x : x[:4].upper()
print(data.index.map(tf))
data.index = data.index.map(tf)
print(data)
print(data.rename(index = str.title, columns = str.upper))
print(data.rename(index = {'OHIO':'INDIANA'}, columns = {'three':'peekaboo'}))


ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]

print(pd.cut(ages, bins))

cats = pd.cut(ages, bins)
print(type(cats))


fruits = ['apple', 'orange', 'apple', 'apple']*2
df = pd.DataFrame(fruits)
print(df)

cat_df = df[0].astype('category')
print(cat_df)
print(cat_df.cat.categories)
print(cat_df.cat.codes)

print(cats)
print(pd.value_counts(cats))
print(pd.cut(ages, bins, right = False)) # 오른쪽 값 포함 x, 왼쪽 값 포함 o

group_names = ['Youth', 'YouthAdult', 'MiddleAged', 'Senior']
print(pd.cut(ages, bins, labels = group_names))


data = np.random.rand(5)
print(data)
print(pd.cut(data, 4, precision = 2))

data = np.random.randn(1000)
cats = pd.qcut(data, 4) # 범주에 들어있는 데이터 개수가 동일하도록 나눠주는 것
print(cats)
print(pd.value_counts(cats))

data = pd.DataFrame(np.random.randn(1000, 4))
print(data)
print(data.describe())

col = data[2]
print(col)
print(col[np.abs(col)>3])
print(data[(np.abs(data)>3).any(axis=1)])

print(np.sign(data)) # 값이 음수면 -1.0, 양수면 1.0
print((np.sign(data)*3))

data[np.abs(data)>3] = np.sign(data)*3
print(data.describe())

df = pd.DataFrame({'key':['b', 'b', 'a', 'c', 'a', 'b'], 'data1':range(6)})
print(df)
print(pd.get_dummies(df['key']))

dummies = pd.get_dummies(df['key'], prefix = 'key')
print(dummies)
df_dummies = df[['data1']].join(dummies)
print(df_dummies)


df = pd.read_table('./movies.dat', 
                   sep = '::', header = None, 
                   names = ['movie_id', 'title', 'genres'])

print(df)
print(df.info())

genres = df['genres'].str.get_dummies()
genres.columns = 'Genre_' + genres.columns
# genres = genres.add_prefix('Genre_')
df_dummies = df.join(genres)
print(df_dummies)

def get_file(file_path):
    df = pd.read_table(file_path, 
                       sep = '::', header = None, 
                       names = ['movie_id', 'title', 'genres'])
    return df

def get_dummies(df):
    genres = df['genres'].str.get_dummies()
    genres = genres.add_prefix('Genre_')
    df_dummies = df.join(genres)
    print(df_dummies)


df = get_file('./movies.dat')
get_dummies(df)














