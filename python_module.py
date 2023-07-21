# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 15:22:28 2023

@author: Jung
"""

    
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


def app_ext_list(sample_list, target):
    sample_list.append(target)
    sample_list.extend(target)
    return sample_list
       

def find_min_max(sample_list):
    
    min_x = sample_list[0]
    max_x = sample_list[0]
    
    for i in sample_list:
        if i < min_x:
            min_x = i
        if i > max_x:
            max_x = i
        
    print('최소값', min_x)
    print('최대값', max_x)
    
    
def create_dict(n):
    sample_dict = {}
    for i in range(1, n+1):
        sample_dict[i] = i**2
    return sample_dict
    
    
def add_dict(sample_dict, keys_list, values_list):
    for i in range(len(keys_list)):
        sample_dict[keys_list[i]] = values_list[i]
    return sample_dict
    
        
def cannon_add_dict(result, a, b):
    if isinstance(a, list):
        #for i in range(len(a)):
            #result[a[i]] = b[i]     
        add_dict(result, a, b)    
    else:
        result[a] = b
    return result
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        