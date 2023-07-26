# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 13:08:57 2023

@author: Jung
"""

f = lambda x, y: x + y

def f(x, y):
    return x + y

print(f(1, 2))
print(f('test', 'python'))
print(f([1, 2], [3, 4]))

g = lambda : 1
print(g())

f = lambda x : x + 1
print(f(2))

incre = lambda x, i = 1 : x + i
print(incre(2))
print(incre(2,10)) #함수를 호출하는 쪽의 argument가 우선함

vargs = lambda x, *args :args
print(vargs(1, 2, 3, 4, 5))

def f1(x):
    return x*x + 3*x -10

def f2(x):
    return x*x*x

def g(func):
    return [func(x) for x in range(-2, 3)]

print(g(f1))
print(g(f2))

print(g(lambda x: x*x + 3*x -10))
print(g(lambda x: x*x*x))


func_list = [
    lambda x, y: x + y,
    lambda x, y: x - y,
    lambda x, y: x * y,
    lambda x, y: x / y
    ]

for i in func_list:
    print(i(2, 1))

plus = lambda x, y: x + y
minus = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y

list_operation = [plus, minus, multiply, divide]

for i in list_operation:
    print(i(2,1))


def increment(n):
    return n + 1
def square(n):
    return n ** 2

for data, action in (2, increment), (4, square):
    print(action(data))


def f(x):
    return x*x

data = [1, 2, 3, 4]

list_result = []
for i in data:
    list_result.append(f(i))
print(list_result)

result_map = map(f, data)
print(type(result_map))
print(list(result_map))
print(list(map(f, data)))
print(list(map(lambda x: x*x, data)))
print(list(map(lambda x: x*x + 3*x + 5, range(10))))

string = ['Hello', 'python', 'Programming']
print(list(map(lambda x: len(x), string)))

xx = list(range(1, 6))
yy = list(range(6, 11))
z = list(map(lambda x, y: x+y, xx, yy))
print(z)

z = map(lambda x, y: x+y, xx, yy)
print(z)
print(next(z))


print(list(filter(lambda x: x>3, [2, 3, 4, 5, 6])))
print(type(filter(lambda x: x>3, [2, 3, 4, 5, 6])))

list_3 = []
for i in [2, 3, 4, 5, 6]:
    if i > 3:
        list_3.append(i)
print(list_3)

print(list(filter(lambda x: x % 2 == 1, range(0, 11))))
print(list(filter(lambda x: x % 2 == 0, range(0, 11))))


list_ = ['high', 'level', '', None, 'builtint', 'func']
print(list(filter(None, list_))) # None = 아무런 조건식이 없어, 입력값 자체를 진릿값으로 사용한다는 의미로 해석

fnames = ['a_thumb.jpg', 'b01_thumb.jpg', 'S100_thumb.jpg', 'S100.jpg', 'b01.jpg']
print(list(filter(lambda x: 'thumb' not in x, fnames)))
print(list(filter(lambda x: 'thumb' in x, fnames)))


L = [3, 2, [3, [[3, 4]]]]

def change_values(data, num, c_num):
    for i in range(len(data)):
        if data[i] == num:
            data[i] = c_num
        elif isinstance(data[i], list):
            change_values(data[i], num, c_num)
    return data

print(change_values(L, 3, 5))


def frange(arg1, *args):
    result = []
    current = float(arg1)

    if len(args) == 2:
        stop, step = args
        if arg1 < stop:
            while current < stop:
                result.append(round((current), 2))
                current += step
        elif arg1 > stop:
            while current > stop:
                result.append(round((current), 2))
                current += step

    if len(args) == 1:
        stop = float(args[0])
        step = 1.0
        while current < stop:
            result.append(round((current), 2))
            current += step

    if len(args) == 0:
        stop = float(arg1)
        start = 0.0
        step = 1.0
        while start < stop:
            result.append(round((start), 2))
            start += step
    
    return result

print(frange(1, 3, 0.2))
print(frange(3, 1, -0.2))
print(frange(4, 9))
print(frange(9))


import mymath
print(mymath.area(5))

from mymath import area, mypi
print(area(5))

from mymath import *
print(mypi)







