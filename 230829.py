# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 13:04:30 2023

@author: Jung
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tips = pd.read_csv('./tips.csv')

grouped = tips.groupby(['day', 'smoker'])
func = ['count', 'mean', 'max']

result = grouped['tip_pct', 'total_bill'].agg(func)
print(result)

ftuples = [('평균', 'mean'), ('차이', np.var)]
result = grouped['tip_pct', 'total_bill'].agg(ftuples)
print(result)
print(result['tip_pct'])

print(grouped.agg({'tip':np.max, 'size':'sum'}))
print(grouped.agg({'tip_pct':['min', 'max', 'mean', 'std'], 'size':'sum'}))

print(tips.groupby(['day', 'smoker'], as_index=False).mean())

def top(df, n=5, column='tip_pct'):
    return df.sort_values(by=column)[-n:]

print(top(tips))
print(tips.groupby('smoker').apply(top))
print(tips.groupby(['smoker', 'day']).apply(top, n=1, column='total_bill'))

result = tips.groupby('smoker')['tip_pct'].describe()
print(result)


s = pd.Series(np.random.randn(6))
s[::2] = np.nan
print(s.fillna(s.mean()))


states = ['Ohio', 'New York', 'Vermont', 'Florida',
          'Oregon', 'Nevada', 'California', 'Idaho']
group_key = ['East'] * 4 + ['West'] * 4
data = pd.Series(np.random.randn(8), index=states)

print(data)
data[['Vermont', 'Nevada', 'Idaho']] = np.nan
print(data.groupby(group_key).mean())

fill_mean = lambda g: g.fillna(g.mean())
print(data.groupby(group_key, group_keys=True).apply(fill_mean))
print(data.groupby(group_key, group_keys=False).apply(fill_mean))

df = pd.DataFrame()
df['A'] = np.arange(5)*10
df['B'] = np.arange(5, 10)*10
df['C'] = np.arange(10, 15)*10

print(df)
print(df.apply(np.square))
print(df.apply(np.sum))
print(df.apply(np.sum, axis = 1))

print(df.apply(lambda x : x/10 if x.name in ['A'] else x)) # axis = 0
print(df.apply(lambda x : x/10 if x.name % 2 == 1 else x, axis=1))

df2 = df.copy()
df2.index = ['i', 'j', 'ks', 'l', 'm']
print(df2.apply(lambda x : np.square(x) if len(x.name) == 2 else x, axis = 1))

def my_sum(x, a, b):
    return a*x+b

print(df.apply(lambda x : my_sum(x, 3, 2)))
dict_args = {'a':3, 'b':2}
print(df.apply(my_sum, **dict_args))
print(df.apply(my_sum, args=(3,2)))

fill_values = {'East':0.5, 'West':-1}
fill_func = lambda x : x.fillna(fill_values[x.name])
print(data.groupby(group_key, group_keys = True).apply(fill_func))


suits = ['H', 'S', 'C', 'D']
card_val = (list(range(1,11))+[10]*3)*4
base_names = ['A'] + list(range(2, 11)) + ['J', 'K', 'Q']

cards = []
for suit in suits :
    cards.extend(str(num) + suit for num in base_names)
print(cards)

def draw(deck, n=5):
    return deck.sample(n)

deck = pd.Series(card_val, index=cards)
print(draw(deck))

get_suit = lambda card : card[-1]
deck.groupby(get_suit).apply(lambda x : draw(x, 2))

print(deck.groupby(get_suit).apply(draw, n=2))
print(deck.groupby(get_suit, group_keys=False).apply(draw, n=2))



import re
from sklearn.linear_model import LinearRegression
from matplotlib import font_manager
font_path = './NanumGothic.ttf'
fontprop = font_manager.FontProperties(fname = font_path, size = 15)

cctv = pd.read_excel('./CCTV_Seoul_new.xlsx')
cctv_data = cctv.iloc[:, [1, 5]] # 관리기관명과 카메라대수 열만 선택

pattern = re.compile(r'(\S+)구') # 공백이 아닌 문자
cctv_data['gu'] = cctv_data['관리기관명'].apply(lambda x: pattern.search(x).group() if pattern.search(x) else '')

cctv_sum = pd.DataFrame(cctv_data['카메라대수'].groupby(cctv_data['gu']).sum())
cctv_sum = cctv_sum.rename(columns={'카메라대수': 'cctv_total'})

pop = pd.read_csv('./POP_Seoul.csv', sep=',', skiprows = [0, 2])
pop_data = pop[['동별(2)', '계 (명)']]
pop_data = pop_data.rename(columns={'동별(2)': 'gu', '계 (명)':'pop_total'})

data = pd.merge(cctv_sum, pop_data, on = 'gu')

x = data.pop_total[:, np.newaxis] # 2차원으로 변경
y = data.cctv_total
model = LinearRegression()
model.fit(x, y) # 직선의 방정식을 구함

data['predict_lr'] = model.predict(x)
data['res'] = data.cctv_total - data.predict_lr

data_sort = data.sort_values(by = 'res', ascending = False)
data_sort = data_sort.reset_index(drop = True)

plt.figure(figsize=(8,8))
plt.scatter(data_sort.pop_total, data_sort.cctv_total, c = data_sort.res, s = 50)
plt.plot(data_sort.pop_total, data_sort.predict_lr, ls = '-', lw = 1, color = 'r')

for n in range(3):
    plt.text(data_sort.loc[n, 'pop_total']*1.02, data_sort.loc[n, 'cctv_total']*1.02,
             data_sort.loc[n, 'gu'], fontsize = 10, fontproperties = fontprop)

for n in range(22, 24):
    plt.text(data_sort.loc[n, 'pop_total']*1.02, data_sort.loc[n, 'cctv_total']*1.02,
             data_sort.loc[n, 'gu'], fontsize = 10, fontproperties = fontprop)

plt.colorbar()
plt.grid()
plt.ylabel('CCTV 개수', fontproperties = fontprop)
plt.xlabel('인구 수', fontproperties = fontprop)
plt.show()



df = pd.DataFrame([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9],
                   [np.nan, np.nan, np.nan]],
                  columns=['A', 'B', 'C'])

print(df)
print(df.agg(['sum', 'min']))
print(df.agg({'A':['sum', 'min'], 'B':['min', 'max']}))
print(df.agg(x = ('A', 'max'), y = ('B', 'min'), z = ('C', np.mean)))

df = pd.DataFrame({
    'city': ['부산', '부산', '부산', '부산', '서울', '서울', '서울'],
    'fruits': ['apple', 'orange', 'banana', 'banana', 'apple', 'apple', 'banana'],
    'price': [100, 200, 250, 300, 150, 200, 400],
    'quantity': [1, 2, 3, 4, 5, 6, 7]})

print(df)
print(df.groupby('city').mean())
print(df.groupby('city').get_group('부산'))
print(df.groupby(['city', 'fruits'], as_index = False).apply(lambda d : (d.price * d.quantity).sum()))


from datetime import datetime
from datetime import timedelta

now = datetime.now()
print(now)
print(now.day)

delta = datetime(2011, 1, 7) - datetime(2008, 6, 24, 8, 15)
print(delta)

start = datetime(2023, 8, 29)
print(start + timedelta(7))
print(start - 2 * timedelta(12))

stamp = datetime(2023, 8, 29)
print(stamp.strftime('%Y====%m====%d'))
value = str(stamp)
print(datetime.strptime(value[:10], '%Y-%m-%d'))

from dateutil.parser import parse

print(parse('2023-08-29'))
print(parse('Jan 31, 1997 10:45 PM'))

datestrs = ['2023-07-06 12:00:00', '2023-08-06 00:00:00']
print(datestrs)
print(pd.to_datetime(datestrs))

idx = pd.to_datetime(datestrs + [None])
print(idx)
print(idx[2])
print(pd.isnull(idx))

dates = [datetime(2023, 1, 2), datetime(2023, 1, 5), 
         datetime(2023, 1, 7), datetime(2023, 1, 8),
         datetime(2023, 1, 10), datetime(2023, 1, 12)]


print(dates)

ts = pd.Series(np.random.randn(6), index = dates)
print(ts)
print(ts.index)
print(ts[::2])
print(ts + ts[::2])

stamp = ts.index[2]
print(stamp)
print(ts[stamp])
print(ts['1/10/2023'])
print(ts['20230112'])

longer_ts = pd.Series(np.random.randn(1000), 
                      index = pd.date_range('1/1/2023', periods = 1000))

print(longer_ts)
print(longer_ts['2024'])
print(longer_ts['2024-08'])
print(longer_ts[datetime(2025, 9, 22):])
print(longer_ts['2/3/2024':'1/1/2025'])
print(longer_ts.truncate(after='8/9/2023'))

dates = pd.date_range('1/1/2023', periods = 100, freq = 'W-WED') # 수요일만
print(dates)

long_df = pd.DataFrame(np.random.randn(100, 4),
                       index = dates,
                       columns = ['A', 'B', 'C', 'D'])

print(long_df)
print(long_df.loc['8-2023'])

dates = pd.DatetimeIndex(['1/1/2023', '1/2/2023', '1/2/2023', '1/2/2023',
                          '1/3/2023'])

print(dates)

dup_ts = pd.Series(np.arange(5), index = dates)
print(dup_ts)
print(dup_ts['1/2/2023'])
print(dup_ts['1/3/2023'])

grouped = dup_ts.groupby(level=0).sum()
print(grouped)









