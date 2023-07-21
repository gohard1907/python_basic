# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 10:24:37 2023

@author: Jung
"""

with open('s.txt', 'r') as f:
    lines = f.readlines()
    lines = sorted(lines)
    for line in lines:
        print(line, end='')


sample_list = ['good', 'very good!', 'excellent', 'nice!']

print(sorted(sample_list))
print(sorted(sample_list, key = lambda x: x[1]))
print(sorted(sample_list, key = len))


with open('s.txt', 'r') as f:
    lines = f.readlines()
lines.sort(key = lambda x: x.split()[1])
print(''.join(lines))


with open('s.txt') as f:
    lines = f.read().split()
for i in range(0, len(lines), 3):
    print(' '.join(lines[i:i+3]))
    
    
from collections import Counter

with open('log_webserver', 'r') as f:
    lines = f.readlines()

counts = Counter((line.split(':')[0], line.split(':')[1]) for line in lines)

for visit, count in counts.items():
    ip, page = visit
    print(f'{ip} \n{page} : {count}')
    

import collections

print(collections.Counter([10, 10, 20, 20, 20, 30]))

count_from_list = collections.Counter([10, 10, 20, 20, 20, 30])
print(count_from_list[10])
print(count_from_list[20])
print(count_from_list[30])

print(count_from_list.items())
print(count_from_list.keys())
print(type(count_from_list))



with open('log_webserver', 'r') as f:
    for line in f:
        ip, url, times = line.split(':')
        print(ip, url, times)
    
        
    
ip_group = {}
with open('log_webserver') as f:
    for line in f:
        ip, url, times = line.split(':')
        if ip not in ip_group:
            ip_group[ip] = []
        ip_group[ip].append(url)        
for i in ip_group:
    print(i)
    k = collections.Counter(ip_group[i])
    for url, count in k.items():
        print(url, ':', count)
    print('='*50)        
    
    
import hashlib   

password = 'password_my_2'
encrypted1 = hashlib.sha1(password.encode()).hexdigest()
print(encrypted1)
print(hashlib.sha1('12345'.encode()).hexdigest()) 


def savePasswd(ids, passwd):
    with open('access', 'a') as f:
        encrypted = hashlib.sha1(passwd.encode()).hexdigest()
        f.write(f'{ids}:{encrypted}\n')

savePasswd('kth', 'password_my_2')
savePasswd('guest', '12345')   

with open('access', 'r') as file:
    print(file.readlines())
    
def checkIfUserValid2(ids, passwd):
    encrypted = hashlib.sha1(passwd.encode()).hexdigest()
    with open('access', 'r') as f:
        for line in f:
            tid, tpass = line.split(':')
            #print('encrypted:', encrypted[-1])
            #print('tpass:', tpass[-1])
            #print(len(encrypted))
            #print(len(tpass))
            if tid == ids and encrypted == tpass.strip():
                #눈으로 확인해도 문제가 없다면 맨 끝의 빈 칸을 한 번 확인해 볼 것
                return True
    return False          

print(checkIfUserValid2('guest', '12345'))
print(checkIfUserValid2('guest', '00000'))

        