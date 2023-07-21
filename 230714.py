# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 13:04:19 2023

@author: Jung
"""

def strings(a):
    a = a.strip().replace('.','').replace("'", '')
    result = a.split()
    return '/'.join(result)

sen = '''Humans are odd. They think order and chaos are somehow opposites and try to control what won't be. But there is grace in their failings.'''

strings(sen)

def in_out_gugudan(a, b = None):
    if b is None:
        for i in range(1, 10):
            result = a * i
            print(f'{a} x {i} = {result}')
    else:
        for i in range(a, b+1):
            for j in range(1, 10):
                result = i * j
                print(f'{i} x {j} = {result}')
                
a = 2
b = 4

in_out_gugudan(a, b)
in_out_gugudan(a)


def minus(height, width):
    return height - width

print(minus(170, 60))
print(minus(60, 170)) #positional argument : 위치에 따라 값이 달라짐
print(minus(width = 60, height = 170)) #keyword argument : 인수값을 주는 것. 순서에 상관없이 쓸 수 있음
print(minus(170, width = 60))
#print(minus(width = 170, 60)) #positional argument가 먼저 와야 함
#print(minus(170, height = 60))


def varg(a, *arg):
    print(a, arg)

varg(2, 3)
varg(2, 3, 4, 5, 6, 7)

def printf(format, *args):
    print(format % args)

printf("I've spent %d days and %d night to do this", 6, 5)


sample_list = [10, 20, 30]

def len_user(data):
    count = 0
    for i in data:
        count += 1
    print(count)
    
len_user(sample_list)


def f(width, height, **kwargs):
    print(width, height)
    print(kwargs)

f(width = 10, height = 5, depth = 10, dimension = 3)
f(1, 2, a = 2, b =4)


def g(a, b, *args, **kwargs):
    print(a, b)
    print('*args:', args)
    print('**kwargs:', kwargs)
    
g(1, 2, 3, 4, c = 5, d = 6)    
g(10, 20, [1, 2, 3, 4], {11:22, 22:33}, c = 2, k = 3)


def h(a, b, c):
    print(a, b, c)
    
h(1, 2, 3)
a = (10, 20, 30)  
h(a[0], a[1], a[2])
h(*a)
dargs = {'a':1, 'b':2, 'c':3}
h(**dargs)
args = (10, 20)
dargs = {'c':30}
h(*args, **dargs)


def gg(t):
    t = [5, 6, 7]

b = [8, 9, 10]
gg(b)
print(b)

def ff(t):
    t[1] = 1000000

ff(b)
print(b)


def n_squared(a, b):
    '''
    a : sequence
    b : int
    '''
    nsqr_list = []
    for i in a:
        nsqr_list.append(i**b)
    return(nsqr_list)

n_squared([2, 3, 4], 2)


import copy

target_list = [1, [11, 21], 3, 4]

def gen_edit(sample_list):
    sample_list[1] = 100
    print('subroutine : ', sample_list)

target_list = [1, [11, 21], 3, 4]
gen_edit(target_list)
print(target_list)


def copy_edit(sample_list):
    dummy_list = copy.copy(sample_list)
    dummy_list[1] = 100
    print('subroutine : ', dummy_list)

target_list = [1, [11, 21], 3, 4]
copy_edit(target_list)
print(target_list)


def copy_edit_2nd(sample_list):
    dummy_list = copy.copy(sample_list)
    dummy_list[1][0] = 100
    print('subroutine : ', dummy_list)

target_list = [1, [11, 21], 3, 4] #객체가 여러개(다중객체)일땐 copy로 막아주지 못함
copy_edit_2nd(target_list)
print(target_list)


def deep_copy_edit(sample_list):
    dummy_list = copy.deepcopy(sample_list)
    dummy_list[1][0] = 100
    print('subroutine : ', dummy_list)

target_list = [1, [11, 21], 3, 4] 
deep_copy_edit(target_list)
print(target_list)


def no_change_edit(sample_list):
    new_list = []
    for i in range(len(sample_list)):
        new_list.append(sample_list[i])
    new_list[1] = 100
    print(new_list)

target_list = list(range(6))
no_change_edit(target_list)
target_list


import time

sample_list = list(range(1000000))

def e_method(sample_list):
    dummy_list = []
    dummy_list.extend(sample_list)

def s_method(sample_list):
    dummy_list = sample_list[:]

def compare(sampple_list):
    start_time = time.time()
    e_method(sample_list)
    e_time = time.time() - start_time

    start_time = time.time()
    s_method(sample_list)
    s_time = time.time() - start_time

    print(f"extend를 이용한 실행 시간: {e_time} 초")
    print(f"slicing을 이용한 실행 시간: {s_time} 초")

compare(sample_list)



import random

data_list = range(1, 46)

print(random.sample([1, 2, 3, 4, 5], 2))
print(random.sample(data_list, 6))

raffle_list = []
for i in range(1000000):
    raffle_number = random.sample(data_list, 6)
    raffle_list.append(raffle_number)

print(len(raffle_list))
print(random.choice([1, 2, 3 ,4 ,5]))
print(random.choice(raffle_list))

def Lotto(n = 100000):
    data_list = range(1, 46)
    raffle_list = []
    for i in range(n):
        raffle_number = random.sample(data_list, 6)
        raffle_list.append(raffle_number)  
    return random.choice(raffle_list)

print(Lotto())




