# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 15:22:28 2023

@author: Jung
"""

import numpy as np

print('out layer')
def test():
    print('ok')
    
def adds(data_list):
    sums = 0
    for i in data_list:
        sums += i
    return sums

def print_list(d_list, n=0):
    for i, j in enumerate(d_list, start=n):
        print(i, j)

def sum_data(n):
    sums = 0
    for i in range(1, n+1):
        sums += i
    return sums
        
def factorial_data(n):
    '''
    팩토리얼 값을 구해주는 함수
    '''
    sums = 1
    for i in range(1, n+1):
        sums *= i
    return sums

def create_dict(n):
    s_dict = {}
    for i in range(1, n+1):
        s_dict[i] = i*i
    return s_dict

def create_dict2(n):
    return {i : i*i for i in range(1, n+1)}

def colab_contents():
    a = {1:100, 2:200, 3:300}
    print(a.keys())
    print(type(a.keys()))


def strings(a):
    a = a.strip().replace('.','').replace("'", '')
    result = a.split()
    return '/'.join(result)

def splitString(text1, symbol1 = '/'):
    result = symbol1.join(text1.strip().replace('.', '').replace(".", '').split(' '))
    return result
 
    
def create_list(target):
    '''
    리스트 생성 함수
    target : value; int, float, string, any
    return
        output : list
    create_list(1234) --> [1234]
    '''
    dummy_list = []
    dummy_list.append(target)
    return dummy_list


def app_ext_list(target):
    list1 = []
    list2 = []
    a = list1.append(target)
    b = list2.extend(target)
    print(a)
    print(b)




