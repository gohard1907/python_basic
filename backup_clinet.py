# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 15:22:35 2023

@author: Jung
"""

import python_module as pm


pm.test()

result = pm.adds([11, 32, 67, 89])
print(result)

pm.print_list(['a', 'b', 'c', 'd'])


print(pm.sum_data(10))

print(pm.factorial_data(10))

print(pm.create_dict(10))

pm.colab_contents()

print(pm.strings('''Humans are odd. They think order and chaos are somehow opposites and try to control what won't be. But there is grace in their failings.'''))

s = '''Humans are odd. They think order and chaos are somehow opposites and try to control what won't be. But there is grace in their failings.'''

result = pm.splitString(s)
print(result)


target = 100
result = pm.create_list(target)

print(result)


target = 'python'
pm.app_ext_list(target)