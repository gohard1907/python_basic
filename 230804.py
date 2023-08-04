# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 16:17:55 2023

@author: Jung
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('./example_data/ex5.csv', index_col=[0])
print(df)

df = pd.read_csv('./example_data/ex5.csv')
print(pd.isnull(df))

df = pd.read_csv('./example_data/ex6.csv')
print(df)
print(df.info())
print(df.describe())

df.to_csv('./out.csv')
df.to_csv('./No_index.csv', index = False)
df.to_csv('./test.csv', index = False, header=False)
df.to_csv('pipe.csv', sep='|')
df.to_csv('null.csv', na_rep='NULL')


import os
import re


pattern = r'life'
script = 'life'
print(re.match(pattern, script))
print(re.match(pattern, script).group())
print(re.match(r'life', 'life').group())


def refinder(pattern, script):
    if re.match(pattern, script):
        print('Match!')
    else:
        print('Not a match!')

pattern = r'Life'
script = 'Life is so cool'
refinder(pattern, script)

pattern = r'life'
script = 'Life is so cool'
refinder(pattern, script)

number = 'My number is 511223-1****** and yours is 521012-2******'
print(re.findall('\d{6}', number))

sentence = 'I have a lovely dog, really. I am not telling a lie. What a pretty dog! I love this dog.'
print(re.sub(r'dog', 'cat', sentence))
words = 'I am home now. \n\n\nI am with my cat. \n\n'
print(words)
print(re.sub(r'\n', '', words))


with open('friends101.txt', 'r', encoding = 'utf8') as f:
    script101 = f.read()
print(script101[:100])

Line = re.findall(r'Monica:.+', script101)
print(Line[:3])

for item in Line[:3]:
    print(item)

with open('monica.txt', 'w', encoding = 'utf8') as f:
    monica = ''
    for i in Line:
        monica += i + '\n'
    f.write(monica)

#with open('monica.txt', 'w', encoding = 'utf8') as f:
#    f.write('\n'.join(Line))


char = re.compile(r'[A-Z][a-z]+:')
print(re.findall(char, script101))

z = list(set(re.findall(char, script101)))
print(z)

name_list=[]
for i in z:
    name_list.append(i[:-1])
print(name_list)

#character = [x[:-1] for x in z]


print(re.findall(r'\([A-Za-z].+?[a-z|\.]\)', script101)[:6])

with open('friends101.txt', 'r') as f:
    sentences = f.readlines()
    
for i in sentences[:20]:
    if re.match(r'[A-Za-z]+:', i):
        print(i) 

lines = [i for i in sentences if re.match(r'[A-Za-z]+:', i)]
for i in lines:
    if re.search('would', i):
        print(i)

would = [i for i in sentences if re.match(r'[A-Za-z]+:', i) and re.search('would', i)]
take = [i for i in sentences if re.match(r'[A-Za-z]+:', i) and re.search('take', i)]
print(would)
print(take)

with open('would.txt', 'w') as newf:
    newf.writelines(would)
    
    
    
print(re.match('c[abc]t', 'cat'))
print(re.match('c[abc]t', 'cbt'))
print(re.match('c[abc]t', 'cct'))
print(re.match('c[abc]t', 'ct'))    
    
print(re.match('[1-4]', '4567').group())    
print(re.match('[0-9]', '567').group())
print(re.match('[1-4]', '45367').group())
print(re.match('5[1-4]', '51267').group())
print(re.match('[0-9]+', '512367').group())    
    
print(re.match('[0-9]', '567').group())
print(re.match('\d', '567').group())    
    
print(re.match('[0-9]+', '567').group())
print(re.match('\d+', '567').group())   
    
print(re.match(r'https?', 'https'))
print(re.match(r'https?', 'http'))    
    
print(re.match('python', '10 python'))
print(re.search('python', '10 python'))
print(re.search('python', '10 python').span())    
print(re.findall(r'[a-z]+', 'python 3 version program')) 
    
p = re.compile(r'([A-Za-z]\w*)\s+=\s*(\d+)')    
print(p.search('a = 123'))
print(p.search('a = 123').groups())
print(re.search(r'=', 'a = 123').group())
print(re.search(r'[^a-z0-9\s]+', 'a = 123').group())


p = re.compile(r'\W')
sub_ = p.sub('::', 'a=123')
print(sub_)
    

import requests    
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
    
url = 'https://quotes.toscrape.com/tag/life/'
html = urlopen(url)

print(html.read()[:100])

html = urlopen(url)
soup = bs(html.read(), 'html.parser')
print(soup)

print(soup.find_all('span'))

quote = soup.find_all('span')
print(quote[0])
print(quote[0].text)

for i in quote:
    print(i.text)

print(soup.find_all('div', {'class':'quote'})[0])
print(soup.find_all('div', {'class':'quote'})[0].text)













    
    
    
    