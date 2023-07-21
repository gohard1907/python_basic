# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 09:07:51 2023

@author: Jung
"""

print([i for i in range(10)])

test = (i < -100 for i in range(10))
for i in test:
    print(i)
    
print(any(test))
print(any([False, False, True]))

bool_list = [True, True, False]
print(all(bool_list))
print(any(bool_list))


list_data = [1, 2, 3, 4, 5]
print(all(i < 10 for i in list_data))
print(all(i < 5 for i in list_data))
print(any(i < 5 for i in list_data)) # any(True, True, True, True, False))

sample_list = [1, 2, 3]
sample_list[1] = 20
print(sample_list)


import glob
file_list = glob.glob('**/*.*', recursive = True)
print(file_list)

print(file_list[1])
print(file_list[:3])


n_list = list(range(1, 10))

sums = 0
for i in n_list:
    sums += i
print(sums)


def print_list(file_lists):
    for i, j in enumerate(file_lists):
        print(i, j)

print_list(file_list)


file_list[1:3] = ['sample_data/read', 'sample_data/output']
print(print_list(file_list))



sample_list = []
sample_list.append(file_list)
print(sample_list)
print(len(sample_list))

sample_list.clear()
sample_list.extend(file_list)
print(sample_list)
print(len(sample_list))

sample_list.append('python')
print(sample_list)

sample_list.extend('python')
print(sample_list)


temp = 'test python program'
sample_list.extend([temp])
print(sample_list)

import time
print(time.time())

start = time.time()
sample_list.append('아무거나')
print(time.time() - start)


list2 = []
start_time = time.time()

list2.append(temp)

end_time = time.time()
spend_time = end_time - start_time
print("append 걸린 시간:", spend_time)

list2 = []
start_time2 = time.time()

list2.extend([temp])

end_time2 = time.time()
spend_time2 = end_time2 - start_time2
print("extend 걸린 시간:", spend_time)

if spend_time > spend_time2:
    print("extend가 더 빠릅니다.")
else:
    print("append가 더 빠릅니다.")
    
    

sample_list.clear()
sample_list = ['test python program']
sample_list.extend(file_list)
print(sample_list)

sample_list.insert(2, 'python')
print(sample_list)

sample_list.remove('python')
print(sample_list)

sample_list.pop()
print(sample_list)

last_element = sample_list.pop()
print(sample_list)
sample_list.append(last_element)

sample_list.sort() #오름차순 정렬
print(sample_list)


file_list_2nd = sample_list.copy()
print(file_list_2nd)

file_list_3rd = sample_list
print(file_list_3rd)

print(sample_list)

file_list_2nd.pop()
print(file_list_2nd)
print(sample_list)

file_list_3rd.pop()
print(file_list_3rd)
print(sample_list)


sample_list.pop(2)
print(sample_list)

print(set(sample_list)) # 중복 원소 제거
dummy_set = set(sample_list)
print(type(dummy_set))

re_list = list(dummy_set)
print(re_list)

sample_list = sample_list + file_list
print(sample_list)

print(sample_list.count('sample_data/read'))


student_list = ['이황', '이이', '원효']

student_list.append('의상')
student_list.sort()
student_list

for num, name in enumerate(student_list, start=1):
    print(num, name)


def print_list(file_lists, n = 0): # n = 0: 기본값을 0으로 한 것
    for i, j in enumerate(file_lists, start = n):
        print(i, j)

print_list(student_list)
print_list(student_list, 21)


for i in range(30):
    print(i*i)

squared_list = [i**2 for i in range(30)]
print(squared_list)

squared_list = []
for i in range(30):
    squared_list.append(i*i)
print(squared_list)


fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
newlist = []

for x in fruits:
    if 'a' in x:
        newlist.append(x)
print(newlist)

newlist = []
newlist = [x for x in fruits if 'a' in x]
print(newlist)


new_squared_list = [i*i for i in range(30) if i % 2 != 0]
print(new_squared_list)


seq1 = 'abc'
seq2 = (1, 2, 3)

print([(x, y) for x in seq1 for y in seq2])



print(file_list)
f_tuple = tuple(file_list)
print(f_tuple)

print_list(f_tuple)
print(f_tuple[-1])

a = (12,)
print(type(a))

print('client.py' in f_tuple)

(green, yellow, *red) = f_tuple 
print(green)
print(yellow)
print(red)

print(f_tuple + (1, 2, 3, 455))

print(f_tuple.count('write'))
print(f_tuple.index('230713.py'))


thisset = {1, 2, 3, 4, 4, 4, 3, 3, 3, 2}
print(thisset)


a = {1:100, 2:200, 3:300}
print(a.keys())
print(type(a.keys()))
print(list(a.keys())[0])
print(a[1])

for i in a:
    print(i, a[i])

sample_dict = {}

sample_dict['one'] = 1
sample_dict['two'] = 2
sample_dict['3'] = 'three'
print(sample_dict)

sample_dict2 = dict(three = 3, four = 4)
print(sample_dict2)

sample_dict3 = {'five':5, 'six':6}
print(sample_dict3)

for i in sample_dict:
    print(i)

for i in sample_dict.keys():
    print(i)

for i in sample_dict.values():
    print(i)

for i in sample_dict.items(): #key와 value를 튜플 형태로 반환
    print(i)
    
sample_dict['color'] = {'red':(255, 0, 0), 'green':(0, 255, 0), 'blue':(0, 0, 255)}
print(sample_dict['color']['blue'][2])
print(sample_dict.keys())
print(sample_dict.values())
print(sample_dict.items())



