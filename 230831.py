# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 13:07:56 2023

@author: Jung
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader.data as web
from datetime import datetime

df = web.DataReader('005930', 'naver', start='2012-01-01', end='2023-08-29')
df = df.astype({'Close':'int'})
df.Close.plot(figsize = (12,8), grid = True)

df_train = df.iloc[:2800, :] # 훈련 자료 == A
df_test = df.iloc[2800:, :] # 테스트 자료 == B

x = np.arange(len(df_train)).reshape(-1, 1)
y = df_train.Close.astype(float).to_numpy()

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

polynomial_features = PolynomialFeatures(degree = 10, include_bias = False)
linear_regression = LinearRegression()
pipeline = Pipeline([('polynomial_features', polynomial_features),
                     ('linear_regression', linear_regression)])
pipeline.fit(x, y)

plt.figure(figsize=(12,6))
plt.plot(x, pipeline.predict(x), label = 'Model')
plt.scatter(x, y, edgecolor = 'b', s = 5, label = 'Samples')
plt.legend(loc = 'best') # 최적의 위치에 범례를 놓는다
plt.show()

from prophet import Prophet

df_prophet = df_train.Close
df2 = df_prophet.reset_index()
df2.columns = ['ds', 'y']
m = Prophet()
m.fit(df2)

print(datetime(2023, 8, 29) - datetime(2023, 5, 15))
future = m.make_future_dataframe(periods = 107) # 6-10 숫자 개수 5개 = 10 - 6 + 1
print(future)
forecast = m.predict(future)
m.plot(forecast)

degree = [3, 4, 6, 8, 10, 12, 14]
X = x

for i, j in enumerate(degree):
    polynomial_features = PolynomialFeatures(degree=j, include_bias=False)
    linear_regression = LinearRegression()
    pipeline = Pipeline( [ ('polynomial_features', polynomial_features), ('linear_regression', linear_regression) ] )
    pipeline.fit(X, y)

    plt.figure(figsize=(10, 50))
    plt.subplot(7, 1, i+1)
    plt.plot(X, pipeline.predict(X), label='Model', color='red')
    plt.scatter(X, y, edgecolors='b', s=5, label='Samples', color='skyblue')
    plt.title(f'Degree={j}')
    plt.legend(loc='best')
    plt.show()


data_file = './temperature_ts_data'
data = pd.read_csv(data_file, parse_dates=[0], index_col=0)
diurnal_data = data.dropna().resample('D').agg({'mean', 'size'})
print(diurnal_data)

diurnal_data.loc[diurnal_data.temperature['size']<19, ('temperature', 'mean')]=np.nan
print(diurnal_data)

fig = diurnal_data.loc[:, ('temperature', 'mean')].plot()
fig.set_title('Air Temperature', size = 15)
fig.set_xlabel('Time', size = 15)
fig.set_ylabel('Diurnal Mean Temperature (C)', size = 15)
fig.grid()
fig.get_figure().tight_layout()
#fig.get_figure().savefig('all_data_plot.png')

df = diurnal_data.temperature['mean'].iloc[:120]
fig = df.plot()
fig.set_title('Air Temperature', size = 15)
fig.set_xlabel('Time', size = 15)
fig.set_ylabel('Diurnal Mean Temperature (C)', size = 15)
fig.grid()
fig.get_figure().tight_layout()
#fig.get_figure().savefig('all_data_plot.png')

methods = ['linear', 'quadratic', 'cubic']
df_gapfilled = pd.DataFrame({m : df.interpolate(method=m) for m in methods})
print(df_gapfilled)

fig=df_gapfilled.plot()
fig.set_title('Air Temperature', size=15)
fig.set_xlabel('Time', size=15)
fig.set_ylabel('Diurnal Mean Temperature (C)', size=15)
fig.grid()
fig.get_figure().tight_layout()
#fig.get_figure().savefig('all_data_plot.png')