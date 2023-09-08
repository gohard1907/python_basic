# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 13:01:20 2023

@author: Jung
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('./auto-mpg.csv', header = None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

df['horsepower'].replace('?', np.nan, inplace=True)
df.dropna(subset=['horsepower'], axis = 0, inplace = True)
df['horsepower'] = df['horsepower'].astype('float')

count, bin_dividers = np.histogram(df['horsepower'], bins=3)
print(bin_dividers)

bin_names = ['저출력', '보통출력', '고출력']

df['hp_bin'] = pd.cut(x = df['horsepower'],
                      bins = bin_dividers,
                      labels = bin_names,
                      include_lowest = True)

print(df[['horsepower', 'hp_bin']].head(15))

df['hp_bin'] = pd.cut(df['horsepower'], 3, labels=bin_names)
print(df[['horsepower', 'hp_bin']].head(15))

horsepower_dummies = pd.get_dummies(df['hp_bin'])
print(horsepower_dummies.head(15))


from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()
onehot_encoder = preprocessing.OneHotEncoder()

onehot_labeled = label_encoder.fit_transform(df['hp_bin'].head(15)) # 범주형 데이터에 번호 부여
print(onehot_labeled)
print(type(onehot_labeled))

onehot_reshaped = onehot_labeled.reshape(len(onehot_labeled), 1)
print(onehot_reshaped)
print(type(onehot_reshaped))

onehot_fitted = onehot_encoder.fit_transform(onehot_reshaped)
print(onehot_fitted)
print(type(onehot_fitted))


hp_bin = ['보통출력','보통출력','보통출력','보통출력','보통출력','고출력', '고출력', '고출력', '고출력', '고출력'
,'고출력', '보통출력','보통출력', '고출력', '저출력']

label_encoders = preprocessing.LabelEncoder()
print(label_encoders.fit_transform(hp_bin))

labels = label_encoders.fit_transform(hp_bin)
print(label_encoders.classes_)

labels_2d = labels.reshape(-1, 1)
print(labels_2d)

one_hot_encoders = preprocessing.OneHotEncoder()
ohe_labels = one_hot_encoders.fit_transform(labels_2d)
print(ohe_labels)
print(ohe_labels.toarray())


df.horsepower = df.horsepower/abs(df.horsepower.max())
print(df.horsepower)

min_x = df.horsepower - df.horsepower.min()
min_max = df.horsepower.max() - df.horsepower.min()
df.horsepower = min_x / min_max
print(df.horsepower.head())

df = pd.read_csv('stock-data.csv')
print(df.head())
print(df.info())

df['new_Date'] = pd.to_datetime(df['Date'])

print(df.head())
print('\n')
print(df.info())
print('\n')
print(type(df['new_Date'][0]))

df.set_index('new_Date', inplace = True)
df.drop('Date', axis = 1, inplace = True)

print(df.head())
print('\n')
print(df.info())

df = df.reset_index()
df['Year'] = df['new_Date'].dt.year
df['Month'] = df['new_Date'].dt.month
df['Day'] = df['new_Date'].dt.day
print(df.head())

df.set_index('new_Date', inplace = True)

df_y = df.loc['2018']
print(df_y.head())

df_ym = df.loc['2018-07']
print(df_ym)

df_ym_cols = df.loc['2018-07', 'Start':'High']
print(df_ym_cols)

df_ymd = df.loc['2018-07-02']
print(df_ymd)

df = df.sort_index()
df_ymd_range = df['2018-06-25':'2018-06-30']
print(df_ymd_range)

today = pd.to_datetime('2018-12-25')
df['time_delta'] = today - df.index
df.set_index('time_delta', inplace = True)
df_180 = df['180 days':'189 days']
print(df_180)

import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
df['ten'] = 10
print(df.head())

def add_10(n):
    return n + 10

def add_two_obj(a, b):
    return a + b

print(add_10(10))
print(add_two_obj(10, 10))

sr1 = df['age'].apply(add_10)
print(sr1.head())

sr2 = df['age'].apply(add_two_obj, b=10)
print(sr2.head())

sr3 = df['age'].apply(lambda x : add_10(x))
print(sr3.head())

def missing_value(series):
    return series.isnull()

result = df.apply(missing_value, axis=0)
print(result.head())

def min_max(x):
    return x.max() - x.min()

result = df.apply(min_max)
print(result)

df['add'] = df.apply(lambda x: add_two_obj(x['age'], x['ten']), axis = 1)
print(df.head())

df = titanic.loc[0:4, 'survived':'age']
print(df)

columns = list(df.columns.values)
print(columns)

columns_sorted = sorted(columns)
df_sorted = df[columns_sorted]
print(df_sorted)

columns_reversed = list(reversed(columns))
df_reversed = df[columns_reversed]
print(df_reversed)

columns_customed = ['pclass', 'sex', 'age', 'survived']
df_customed = df[columns_customed]
print(df_customed)


df = pd.read_excel('./주가데이터.xlsx', engine='openpyxl')
print(df.head())
print(df.dtypes)

df['연월일'] = df['연월일'].astype('str')
dates = df['연월일'].str.split('-')
print(dates.head())

df['연'] = dates.str.get(0)
df['월'] = dates.str.get(1)
df['일'] = dates.str.get(2)
print(df.head())


mask1 = (titanic.age >= 10) & (titanic.age < 20)
df_teenage = titanic.loc[mask1, :]
print(df_teenage.head())

mask2 = (titanic.age < 10) & (titanic.sex == 'female')
df_female_under10 = titanic.loc[mask2, :] 
print(df_female_under10.head())

mask3 = (titanic.age < 10) | (titanic.age >= 60)
df_um = titanic.loc[mask3, ['age', 'sex', 'alone']]
print(df_um.head())

mask4 = titanic['sibsp'] == 3
mask5 = titanic['sibsp'] == 4
mask6 = titanic['sibsp'] == 5

df_boolean = titanic[mask4 | mask5 | mask6]
print(df_boolean.head())

isin_filter = titanic['sibsp'].isin([3, 4, 5])
df_isin = titanic[isin_filter]
print(df_isin.head())


df1 = pd.DataFrame({'a': ['a0', 'a1', 'a2', 'a3'],
                    'b': ['b0', 'b1', 'b2', 'b3'],
                    'c': ['c0', 'c1', 'c2', 'c3']},
                    index=[0, 1, 2, 3])
 
df2 = pd.DataFrame({'a': ['a2', 'a3', 'a4', 'a5'],
                    'b': ['b2', 'b3', 'b4', 'b5'],
                    'c': ['c2', 'c3', 'c4', 'c5'],
                    'd': ['d2', 'd3', 'd4', 'd5']},
                    index=[2, 3, 4, 5])

print(df1)
print(df2)

result1 = pd.concat([df1, df2])
print(result1)

result2 = pd.concat([df1, df2], ignore_index=True)
print(result2)

result3 = pd.concat([df1, df2], axis=1)
print(result3)

result3_in = pd.concat([df1, df2], axis=1, join = 'inner')
print(result3_in)


sr1 = pd.Series(['e0', 'e1', 'e2', 'e3'], name='e')
sr2 = pd.Series(['f0', 'f1', 'f2'], name='f', index=[3, 4, 5])
sr3 = pd.Series(['g0', 'g1', 'g2', 'g3'], name='g')

result4 = pd.concat([df1, sr1], axis = 1)
print(result4)

result5 = pd.concat([df2, sr2], axis = 1, sort = True)
print(result5)

result6 = pd.concat([sr1, sr3], axis=1)
print(result6)

result7 = pd.concat([sr1, sr3], axis=0)
print(result7)


df1 = pd.read_excel('./stock price.xlsx')
df2 = pd.read_excel('./stock valuation.xlsx')

print(df1)
print(df2)

merge_inner = pd.merge(df1, df2)
print(merge_inner)

merge_outer = pd.merge(df1, df2, how = 'outer', on = 'id')
print(merge_outer)

merge_left = pd.merge(df1, df2, how='left', left_on='stock_name', right_on='name')
print(merge_left)

merge_right = pd.merge(df1, df2, how='right', left_on='stock_name', right_on='name')
print(merge_right)

price = df1[df1['price'] < 50000]
print(price.head())

value = pd.merge(price, df2)
print(value)


df1 = pd.read_excel('./stock price.xlsx', index_col='id')
df2 = pd.read_excel('./stock valuation.xlsx', index_col='id')

df3 = df1.join(df2)
print(df3)

df4 = df1.join(df2, how='inner')
print(df4)


df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]
print(df.head())

grouped = df.groupby(['class'])
print(grouped)
print(df['class'].unique())

for key, group in grouped:
    print('* key :', key)
    print('* number :', len(group))
    print(group.head())
    print('='*100)

#average = grouped.mean()
#print(average)

group3 = grouped.get_group('Third')
print(group3.head())

grouped_two = df.groupby(['class', 'sex'])

for key, group in grouped_two:
    print('* key :', key)
    print('* number :', len(group))
    print(group.head())
    print('='*100)

avg_two = grouped_two.mean()
print(avg_two)

group3f = grouped_two.get_group(('Third', 'female'))
print(group3f.head())

#std_all = grouped.std()
#print(std_all)

std_fare = grouped.fare.std()
print(std_fare)

#agg_minmax = grouped.agg(min_max)
#print(agg_minmax.head())

agg_all = grouped.agg(['min', 'max'])
print(agg_all.head())

agg_sep = grouped.agg({'fare':['min', 'max'], 'age':'mean'})
print(agg_sep)

age_mean = grouped.age.mean()
print(age_mean)

age_std = grouped.age.std()
print(age_std)

for key, group in grouped.age:
    group_zscore = (group - age_mean.loc[key]) / age_std.loc[key]
    print('* origin :', key)
    print(group_zscore.head())
    print('='*100)

def z_score(x):
    return (x - x.mean())/x.std()

age_zscore = grouped.age.transform(z_score)
print(age_zscore.loc[[1, 9, 0]])
print('\n')
print(len(age_zscore))
print('\n')
print(age_zscore.loc[:9])
print('\n')
print(type(age_zscore))

grouped_filter = grouped.filter(lambda x: len(x) >= 200)
print(grouped_filter)

age_filter = grouped.filter(lambda x: x.age.mean() < 30)
print(age_filter)

age_filter['class'].unique()

agg_grouped = grouped.apply(lambda x: x.describe())
print(agg_grouped)

age_zscore = grouped.age.apply(z_score)
print(age_zscore)

age_filter = grouped.apply(lambda x: x.age.mean() < 30)
print(age_filter)

for x in age_filter.index:
    if age_filter[x] == True:
        age_filter_df = grouped.get_group(x)
        print(age_filter_df)
        print('='*100)

pdf1 = pd.pivot_table(df,
                      index = 'class',
                      columns = 'sex',
                      values = 'age',
                      aggfunc = 'mean')

print(pdf1)

pdf2 = pd.pivot_table(df,
                      index = 'class',
                      columns = 'sex',
                      values = 'survived',
                      aggfunc = ['mean', 'sum'])

print(pdf2)

pdf3 = pd.pivot_table(df,
                      index = ['class', 'sex'],
                      columns = 'survived',
                      values = ['age', 'fare'],
                      aggfunc = ['mean', 'max'])

print(pdf3)
print(pdf3.xs('First'))
print(pdf3.xs(('First', 'female')))
print(pdf3.xs('male', level = 'sex'))
print(pdf3.xs(('Second', 'male'), level = [0, 'sex'])) # 레벨 0에서 Second, sex에서 male
print(pdf3.xs(('Second', 'male'), level = [0, 1]))
print(pdf3.xs('mean', axis = 1))
print(pdf3.xs(('mean', 'age'), axis = 1))
print(pdf3.xs(1, level = 'survived', axis = 1)) # survived 레벨이 1인 경우

