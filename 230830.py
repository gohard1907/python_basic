# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 13:04:30 2023

@author: Jung
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

index = pd.date_range('2023-07-10', '2023-07-26')
print(index)

print(pd.date_range(start = '2023-07-10', periods = 20))
print(pd.date_range(end = '2023-07-10', periods = 20))
print(pd.date_range('2023-01-01', '2023-12-31', freq='BM')) # 매월 마지막 영업일
print(pd.date_range('2023-05-02 12:56:31', periods = 5))
print(pd.date_range('2023-05-02 12:56:31', periods = 5, normalize = True)) # 자정으로 시간을 세팅
print(pd.date_range('2023-07-10', '2023-07-14 23:59', freq = '4h'))
print(pd.date_range('2023-07-10', periods = 10, freq = '1h30min'))

rng = pd.date_range('2023-01-01', '2023-09-01', freq = 'WOM-3FRI')
print(rng)
print(list(rng))

ts = pd.Series(np.random.randn(4), 
               index = pd.date_range('1/1/2023', periods = 4, freq = 'M'))

print(ts)
print(ts.shift(2))
print(ts.shift(-1))
print(ts.shift(2, freq = 'M'))
print(ts.shift(2, freq = 'D'))
print(ts.shift(1, freq = '90T'))

rng = pd.date_range('2023-01-01', periods = 100, freq = 'D')
ts = pd.Series(np.random.randn(len(rng)), index = rng)

print(ts)
print(ts.resample('M').mean())
print(ts.resample('M', kind = 'period').mean())

rng = pd.date_range('2023-01-01', periods = 12, freq = 'T')
print(rng)

ts = pd.Series(np.arange(12), index = rng)
print(ts)
print(ts.resample('5min', closed = 'left').sum())
print(ts.resample('5min', closed = 'right', label = 'right').sum())
print(ts.resample('5min', closed = 'right', label = 'right', loffset = '-1s').sum())

rng = pd.date_range('2023-01-01', periods =1440, freq = 'T')
print(rng)

ts = pd.Series(np.arange(1, len(rng)+1), index = rng)
print(ts)
print(ts.resample('60min').mean())
print(ts.resample('H').agg(['mean', 'size']))
print(ts.resample('3H').agg(['mean', 'size']))
print(ts.resample('D').agg(['mean', 'size']))
print(ts.resample('5min').ohlc()) # Open-High-Low-Close


frame = pd.DataFrame(np.random.randn(8, 4), 
                     index = pd.date_range('1-2022', '3-2022', freq = 'W-WED'),
                     columns = ['daum', 'naver', 'nate', 'zum'])

print(frame)
print(frame.resample('D').asfreq()) # 앞의 주기로 freq를 고친다
print(frame.resample('D').ffill())
print(frame.resample('D').ffill(limit = 2))
print(frame.resample('W-THU').ffill())


close_px_all = pd.read_csv('./stock_px_2.csv', parse_dates = True, index_col=0) # 첫번째 칼럼을 datetime으로 받아줌
print(close_px_all)
print(close_px_all.info())

close_px = close_px_all[['AAPL', 'MSFT', 'XOM']]
print(close_px)

close_px.AAPL.plot()
close_px.AAPL.rolling(250).mean().plot() 
# 첫번째 데이터부터 250번째 데이터까지 평균, 두번째부터 251번째까지 평균... = 이동평균

close_px.rolling(250).mean().plot() 

df = close_px.AAPL.rolling(10).mean()
print(df.head(10))

df = close_px.AAPL.rolling(10, min_periods = 4).mean()
print(df.head(10))

rng = pd.date_range('2023-01-01', periods = 1440, freq = 'T')
ts = pd.DataFrame({'number':np.arange(1, len(rng)+1), 'dts':rng})

df = ts.rolling(10).sum()
print(df.head(10))

df = ts.rolling(10, min_periods = 4).sum()
print(df.head(10))

ts = pd.Series(np.arange(1, len(rng)+1), rng)
df = ts.rolling(10, min_periods = 4).sum()
print(df.head(10))
print(ts.rolling('10min').sum().head(10))
print(ts.rolling(10).sum().head(14))
print(ts.rolling(4).sum().head(10))
print(ts.rolling('4min').sum().head(10))

ts[::2] = np.nan
print(ts)
print(ts.rolling('4min').sum().head(10))


df = pd.read_csv('./times.csv')
print(df)

df['Yr_Mo_Dy'] = pd.to_datetime(df['Yr_Mo_Dy'])
df['Yr_Mo_Dy'] = df['Yr_Mo_Dy'].apply(lambda x: x.replace(year = x.year - 100) if x.year >= 2000 else x)

df['rdt']=pd.to_datetime(df['Yr_Mo_Dy'])
print(df.info())
print(df.rdt.dt.year.unique())

df['YMD'] = df.loc[:, 'rdt'].apply(lambda x:x.replace(year=x.year-100)
if x.year>2000 else x)

print(df.RPT.groupby(df.YMD.dt.year).mean())
print(df.YMD.dt.year)

print(df.resample('Y', on = 'YMD').agg({'RPT':['size','mean']}))
print(df.resample('Y', on = 'YMD').agg({'RPT':['size','mean']}).droplevel(level=0, axis=1))

data= [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
idx = [['idx1','idx1','idx2','idx2'],['row1','row2','row3','row4']]
col = [['col1','col1','col2','col2'],['val1','val2','val3','val4']]
df_ = pd.DataFrame(data = data, index = idx, columns = col)

print(df_)
print(df_.droplevel(axis = 0, level = 0))
print(df_.droplevel(axis = 0, level = 1))
print(df_.droplevel(axis = 1, level = 0))
print(df_.droplevel(axis = 1, level = 1))

print(df.YMD.dt.weekday) # 6 : 일요일, 0 : 월요일
df['weekday'] = df.YMD.dt.weekday.map(lambda x: 1 if x in [5, 6] else 0)
print(df.head())

print(df.groupby(df.YMD.dt.month).mean())
print(df.groupby(df.YMD.dt.to_period('M')).mean())


data = {'age':[10, 10, 21, 22], 'weight':[20, 30, 60, 70]}
df = pd.DataFrame(data)
print(df)
print(df.query('age == 10'))

expr_str = 'age == 10'
print(df.query(expr_str))

expr_str = 'age != 10'
print(df.query(expr_str))

expr_str = 'age > 20'
print(df.query(expr_str))

expr_str = 'age == [21, 22]'
print(df.query(expr_str))

expr_str = 'age not in [21, 22]'
print(df.query(expr_str))

expr_str = '(age == 10) and (weight >= 30)'
print(df.query(expr_str))

num_age = 10
num_weight = 30
expr_str = f'(age == {num_age}) and (weight >= {num_weight})'
print(df.query(expr_str))

def max_user(x, y):
    return max(x, y)
expr_str = 'age >= @max_user(1, 22)' # 함수를 쓰고 싶을땐 사용자 함수를 만들어서 넣어야 됨
print(df.query(expr_str))

expr_str = 'index > 1'
print(df.query(expr_str))

data = {'name':['White tiger', 'Tiger black', 'Red tiger'], 'age':[5, 7, 9]}
df = pd.DataFrame(data)
print(df)

expr_str = '''name.str.contains('tiger')'''
print(df.query(expr_str, engine = 'python'))

expr_str = '''name.str.contains('tiger', case = False)''' # 대소문자 구분
print(df.query(expr_str, engine = 'python'))

expr_str = '''name.str.startswith('Tiger')'''
print(df.query(expr_str, engine = 'python'))

expr_str = '''name.str.endswith('tiger')'''
print(df.query(expr_str, engine = 'python'))


import pandas_datareader.data as web

code_all=pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download')
print(code_all)

code_df = code_all[0]
print(code_df.head())

names = '삼성전자'
expr_str = f'''회사명=='{names}' '''
code = code_df.query(expr_str)
print(code)

print('{:06d}'.format(code['종목코드'].values[0]))
print('00' + code['종목코드'].to_string(index=False))

target_code = '{:06d}'.format(code['종목코드'].values[0])
df = web.DataReader(target_code, 'naver', start='2012-01-01', end='2023-08-29')

y = df.Close.map(int)
x = df.index
plt.plot(x, y)

df = df.astype({'Close':'int'})
df.Close.plot(figsize=(12, 6), grid=True)


print(len(df))
df_train = df.iloc[:2800, :] # 훈련 자료 == A
df_test = df.iloc[2800:, :] # 테스트 자료 == B

print(df_train.head())
print(df_train.tail())
print(df_test.head())
print(df_test.tail())



















