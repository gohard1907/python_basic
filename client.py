# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 15:22:35 2023

@author: Jung
"""

import python_module as pm

target = 100
result = pm.create_list(target)
print(result)

sample_list = result

target = 'python'
result = pm.app_ext_list(sample_list, target)
print(result)
items_list = [12, 567, 34, 9, 17]
pm.find_min_max(items_list)

n = 9
result = pm.create_dict(n)
print(result)

keys_list = ['name', 'year', 'attr']
values_list = ['Joker', 2019, 'villain']
dict_result = pm.add_dict(result, keys_list, values_list)
print(dict_result)

result_of_cannon = pm.cannon_add_dict(dict_result, (10, 9), 1729)
print(result_of_cannon)    

key_list = ['one', 'two']
value_list = [100, 200]
roc_2 = pm.cannon_add_dict(result_of_cannon, key_list, value_list)
print(roc_2)



