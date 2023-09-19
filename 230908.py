# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 13:38:46 2023

@author: Jung
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df2 = pd.read_csv('./survey.csv')
print(df2.head())
print(df2.income.mean())
print(df2.income.sum())
print(df2.income.median())
print(df2.groupby(df2.sex).mean())


from scipy import stats

grouped = df2.groupby(['sex'])

for key, group in grouped:
    print(key)
    print(group)

m = grouped.get_group('m')['income']
f = grouped.get_group('f')['income']

print(m)
print(f)

result = stats.ttest_ind(m, f) # 등분산 방식
print(result)

result = stats.ttest_ind(m, f, equal_var = False) # 이분산 방식
print(result)

alpha = 0.05
p_value = result[1]
print(p_value)

if p_value < alpha:
    print('두 평균에 차이가 있습니다.')
else:
    print('두 평균에 차이가 없습니다.')


stat, p_value = stats.levene(m, f)
print(p_value)

if p_value < alpha:
    print('등분산을 가정할 수 없습니다. p-value : ', p_value)
else:
    print('등분산을 가정할 수 있습니다. p-value : ', p_value)


print(stats.shapiro(m))
print(stats.shapiro(f))

x = stats.norm.rvs(loc=5, scale=3, size=600)
shapiro_test = stats.shapiro(x)
print(shapiro_test)


rv = stats.norm(2, 0.5) # loc = 2 : 평균, scale = 0.5 : 표준편차
print(rv.mean())
print(rv.var())

x = np.arange(0, 4.1, 0.1)
y = rv.pdf(x)

plt.plot(x, y)
plt.grid()

print(rv.cdf(2.0)) # 확률을 구할 때 사용하는 method
print(rv.cdf(1.7))
print(rv.isf(0.3)) # 결과 값은 x, 0.3(cdf 값)
print(rv.isf(0.5))

print(rv.isf(0.95), rv.isf(0.05))
print(rv.interval(0.9))


rv = stats.norm(130, np.sqrt(9/14)) # loc=2 : 평균, scale = np.sqrt(9/14) : 표준편차
print(rv.isf(0.95))


sample = np.array([122.02, 131.73, 130.6 , 131.82, 132.05, 126.12, 124.43, 132.89,
       122.79, 129.95, 126.14, 134.45, 127.64, 125.68])

s_mean = np.mean(sample)
print(s_mean)

z = (s_mean-130)/np.sqrt(9/14) # 검정통계량 : Z
print(z)

rv = stats.norm()
print(rv.isf(0.95)) # 임계값
print(rv.cdf(z))


x = [8, 3, 6, 6, 9, 4, 3, 9, 3, 4]
y = [6, 2, 4, 6, 10, 5, 1, 8, 4, 5]

print(stats.pearsonr(x, y))
plt.scatter(x, y)


#print(df2)
#print(df2.corr(method='spearman'))
#print(df2.corr())




