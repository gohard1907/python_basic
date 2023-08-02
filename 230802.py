# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 13:05:40 2023

@author: Jung
"""

from datetime import datetime, timedelta

dt = datetime(2023, 8, 2, 9, 13)
print(dt)
print(dt.day)
print(dt.month)
print(dt.year)
print(dt.hour)
print(dt.minute)

dt = datetime.now()
print(dt)
print(dt.date())
print(dt.time())

print(dt.strftime('%m/%d/%Y %a %H:%M'))
print(datetime.strptime('20230802', '%Y%m%d'))
print(dt)
print(dt.replace(minute=0, second=0))
print(dt.microsecond)

delta = datetime.now() - dt
print(delta)
print(type(delta))

print(dt + timedelta(hours=2))
print(dt + timedelta(13))
print(dt + timedelta(30))

base_time = datetime.now().replace(minute=0, second=0, microsecond=0)
print(base_time)
future_time = datetime(2023, 12, 26)
print(future_time)
print((future_time - base_time).total_seconds())
print((future_time - base_time))
print((future_time - base_time).days)

diff = future_time - base_time
print(diff.total_seconds() / 3600)
diff = future_time - datetime.now()
print(diff)
print(diff.seconds)
print(diff.total_seconds())

for i in range(diff.days):
    print(i)



import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x_seq = list(range(10))
print(x_seq)
data = np.arange(10)
print(data)
print(data*3)


plt.plot(data, data**2)

y = data**2
x = data
fig = plt.figure()
axes = fig.add_subplot()
axes.plot(x, y)

fig, axes = plt.subplots()
axes.plot(x, y)

plt.plot(x, x*x) #stateful

x = np.arange(-10, 11, 1) #stateless
fig, ax = plt.subplots(figsize = (4, 4))
plt.plot(x, x*x)
ax.spines['left'].set_position('center')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

t = np.arange(0, 5, 0.5)
plt.figure(figsize=(10,6))
plt.plot(t, t, 'r--')
plt.plot(t, t**2, 'gs')
plt.plot(t, t**3, 'b>')
plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
plt.plot(np.random.randn(50).cumsum(), 'k--')
_ = ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
ax2.scatter(np.arange(30), np.arange(30)+3 * np.random.randn(30))
plt.show()

fig, axes = plt.subplots(2, 2, sharex = True, sharey = True)
for i in range(2):
    for j in range(2):
        axes[i, j].hist(np.random.randn(500), bins=50, color='k', alpha=0.5)
plt.subplots_adjust(wspace=0, hspace=0)
plt.show()

x = np.arange(10)
y = x*10 + 2
fig, ax = plt.subplots()
ax.plot(x, y, linestyle = '--', color = 'g')
plt.show()

plt.plot(np.random.randn(30).cumsum(), 'ko--')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(np.random.randn(1000).cumsum())
ticks = ax.set_xticks([0, 250, 500, 750, 1000])
labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'], rotation = 30)
ax.set_title('My first plot', fontsize = 20)
ax.set_xlabel('Stages', fontsize = 15)
ax.set_ylabel('y_values')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(np.random.randn(1000).cumsum())
ticks = ax.set_xticks([0, 250, 500, 750, 1000])
labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'], rotation = 30)
plt.show()

x = np.arange(1, 10, 0.1)
loss = lambda x : np.exp(-x)
acc = lambda x : -np.exp(-x)

x1 = np.random.randn(len(x))

fig, loss_ax = plt.subplots(figsize=(8,6))

acc_ax = loss_ax.twinx() # x축을 공유하는 새로운 axes 객체를 만들어 준다. 결과적으로 x축은 같고 y축만 다른 그래프가 생긴다.

loss_ax.plot(x, loss(x), 'y', label = 'train loss')
loss_ax.plot(x, loss(x-x1/5), 'r', label = 'validation loss')

acc_ax.plot(x, acc(x), 'b', label = 'train acc')
acc_ax.plot(x, acc(x-x1/7), 'g', label = 'val acc')
for label in acc_ax.get_yticklabels(): # y축 tick 색깔 지정
    label.set_color('blue')

loss_ax.set_xlabel('epoch', size = 20)
loss_ax.set_ylabel('loss', size = 22)
acc_ax.set_ylabel('accuracy', color = 'blue', size = 20)

loss_ax.legend(loc = 'upper right')
acc_ax.legend(loc = 'lower right')
fig.savefig('test1.png')
plt.show()

x = np.arange(0,10, np.pi/100)
f = lambda x : np.sin(x)+x/10

XTN=[r'$0 \pi$',r'$\pi/2$',r'$\pi$',r'$3\pi/2$',r'$2\pi$',r'$5\pi/2$',r'$3\pi$']
plt.figure(figsize=(8,6))
plt.plot(x, f(x))
plt.title('Plot Exercise',position=(0.5,1.04), fontsize=20)
plt.xlabel (r'$x$',fontsize=20)
plt.ylabel (r'$f (x) = sin(x) + x$', fontsize=20)
plt.xticks(np.arange(0.0,10.0,np.pi/2), labels=XTN, fontsize=15)
plt.yticks(np.arange(-1,2.1,np.pi/5), fontsize=15)
plt.text(0.8,-0.3,'Test Messages', color='k', fontsize=18)
plt.grid()
plt.tight_layout()
plt.savefig('test2.png')
plt.show()



x = [10, 20, 30]
array_x = np.array(x)
print(array_x)

obj = pd.Series(array_x)
print(obj)
print(obj.values)
print(obj.index)
for i in obj.index:
    print(i, obj[i])

obj2 = pd.Series([4, 7, -5, 3], index = ['a', 'b', 'c', 'd'])
print(obj2)
print(obj2.index)
for i in obj2.index:
    print(i, obj2[i])
print(obj2['a'])
obj2['d'] = 6
print(obj2)
print(obj2[['c', 'a', 'd']])
print(obj2[obj2>0])

data = pd.Series([-1, 0, 1], index = ['a', 'b', 'c'])
print(data[data<0])
print(data*2)
print(np.exp(data))

print('c' in data)
print('e' in data)
print(1 in data)

sdata = {'Ohio':35000, 'Texas':71000, 'Oregon':1600, 'Utah':5000}
obj3 = pd.Series(sdata)
print(obj3)
print(obj3.index)
print(list(obj3.index))

std__ = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index = std__)
print(obj4)
print(pd.isnull(obj4))
print(pd.notnull(obj4))
print(obj4.isnull())
print(obj3 + obj4)

obj4.name = 'population'
obj4.index.name = 'state'
print(obj4)
obj4.index = ['Bob', 'Steve', 'Jeff', 'Ted']
print(obj4)


data = {'state':['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year':[2000, 2001, 2002, 2001, 2002, 2003],
        'pop':[1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}

df = pd.DataFrame(data)
print(df)

인구1 = {'인구':{'하나':1542, '여섯':9776, '둘':1535},
       '지역':{'하나':'대전', '여섯':'서울', '둘':'대전', '셋':'대전'}}

df2 = pd.DataFrame(인구1)
print(df2)
print(pd.DataFrame(data, columns=['year', 'state', 'seoul']))

df3 = pd.DataFrame(data, columns = ['year', 'state', 'pop', 'debt'],
                   index = ['one', 'two', 'three', 'four', 'five', 'six'])
print(df3)
print(df3.index)
print(df3.columns)
print(df3.state)

print(df2['인구'])
print(df2.인구)

print(df3.year)
print(df3.debt)


print(df3.loc['three'])
print(df3.loc['three', 'year'])
print(df3.iloc[2])


df3['debt'] = 16.5
print(df3)
df3.debt = np.arange(6.)
print(df3)

val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
print(val)
df3.debt = val
print(df3)

df3['stern'] = df3.state == 'Ohio'
print(df3)

del df3['debt']
del df3['stern']
print(df3)


pops = {'Nevada':{2001:2.4, 2002:2.9}, 'Ohio':{2000:1.5, 2001:1.7, 2002:3.6}}
df4 = pd.DataFrame(pops)
print(df4)
print(df4.T)
print(pd.DataFrame(pops, index=[2001, 2002, 2003]))
print(df4['Ohio'][:-1])
print(df4['Ohio'][:3])

pdata = {'Ohio':df4['Ohio'][:-1],
         'Nevada':df4['Nevada'][:2]}
print(pdata)
print(pd.DataFrame(pdata))


df2.index.name = '번호'
df2.columns.name = '분류'
print(df2)


obj5 = pd.Series(range(3), index = ['a', 'b', 'c'])
obj5.rename(index={'a': 'A'}, inplace=True)
print(obj5)

obj6 = pd.Series(range(3), index = ['a', 'b', 'c'])
obj6.index.values[0] = 'A'
print(obj6)

print('인구' in df2)
print('인구' in df2.columns)
print('하나' in df2.index)


df = pd.Series([3, -8, 2, 0], index = ['d', 'b', 'a', 'c'])
print(df)
print(df.reindex(['a', 'b', 'c', 'd', 'e']))
print(df.reindex(range(4)))


df = pd.DataFrame(np.arange(6).reshape(3,2), 
                  index = range(0, 5, 2), columns = ['A', 'B'])
print(df)




















