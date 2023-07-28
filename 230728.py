# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 13:08:55 2023

@author: Jung
"""

import json
def get_data(file_names):
    with open(file_names, encoding = 'utf-8') as f:
        datas = json.load(f)
    return datas

data = get_data('gg_toilet.json')

print(data[0])

import folium
def map_add(maps, data):
    for item in data:
        name = item['PBCTLT_PLC_NM']
        latitude = item['REFINE_WGS84_LAT']
        longitude = item['REFINE_WGS84_LOGT']

        try:
            latitude = float(latitude)
            longitude = float(longitude)
        except ValueError:
            continue

        folium.CircleMarker([latitude, longitude], radius=4, popup=name, color='red', fill_color='red').add_to(maps)
    
    return maps

def FoliumMap(data, save_file='result.html'):
    maps = folium.Map(location=[37.5602, 126.982], zoom_start=7)
    map_add(maps, data).save(save_file)
    
FoliumMap(data)


class S1:
    a = 1
    
x = S1()
print(type(x))
print(S1.a)

x.c = 10
print(x.c)
print(x.a)
x.a = 10
print(x.a)
S1.b = 2
x.b = 4
y = S1()
print(y.a)
print(y.b)
y.a = 100
y.b = 200
print(S1.a, S1.b, x.a, x.b, y.a, y.b)


class MyClass:
    def __add__(self, x):
        print(f'add {x} called')
        return x

a = MyClass()
print(a + 3)


class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

mc_1 = MyClass('아무개', '아무살')
print(mc_1.name)
print(mc_1.age)

mc2 = MyClass('tom', 21)
print(mc2.age)
print(mc2.name)

class MyClass:
    def __init__(self):
        self.age = 21
        self.name = 'Guido'
        
mc3 = MyClass()
print(mc3.age)
print(mc3.name)


class MyClass:
    def __init__(self, age=21, name='Guido'):
        self.age = age
        self.name = name

mc4 = MyClass()
mc5 = MyClass(23)
mc6 = MyClass(23, 'python')

print(mc5.age)
print(mc5.name)
print(mc6.age, mc6.name)


class MyClass:
    def __init__(self, phone, age=21, name='Guido'):
        self.phone = phone
        self.age = age
        self.name = name
    def print_attr(self, number):
        self.number = number
        print(self.phone)
        self.phone = self.number
        return self.phone

mc7 = MyClass('마구눌러')
print(mc7.print_attr('01012345678'))

mc8 = MyClass('010123456899')
print(mc8.print_attr('마구눌러'))


class A:
    def f(self):
        print('base')
class B(A):
    pass

b = B()
print(b.f())
print(B.__bases__)


class MyClass:
    def set(self, v):
        self.value = v
    def get(self):
        return self.value
    def temp(self):
        self.value2 = self.get()
        print(self.value2)

mc9 = MyClass()
mc9.set('egg')
mc9.temp()

MyClass.set(mc9, 100) #unbound method 호출
print(mc9.set)
print(MyClass.get(mc9))


class MyClass2:
    def set(self, v):
        self.value = v
    def get(self):
        return self.value
    def incr(self):
        self.value += 1
        return self.get()

mc10 = MyClass2()
mc10.set(10)
print(mc10.incr())


from time import time, ctime, sleep

class Life:
    def __init__(self):
        self.birth = ctime()
        print('Birthday', self.birth)
    def __del__(self):
        print('Deathday', ctime())

life_io = Life()
del(life_io) #del() 함수에 __del__(self)가 대응된다.


class Var:
    c_mem = 100 #클래스 멤버
    def f(self):
        self.i_mem = 200 #인스턴스 멤버
    def g(self):
        return self.i_mem, self.c_mem

print(Var.c_mem)

v1 = Var()
v2 = Var()
print(v1.c_mem)
print(v2.c_mem)
v1.c_mem = 50
print(v1.c_mem)


class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def mul(self):
        return self.first * self.second

    def sub(self):
        return self.first - self.second

    def div(self):
        return self.first / self.second

fc1 = FourCal(10, 5)
print(fc1.add())
print(fc1.sub())
print(fc1.mul())
print(fc1.div())

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        return self.first / self.second





