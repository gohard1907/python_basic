# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 17:49:40 2023

@author: Jung
"""

from urllib.request import urlopen, Request
import pandas as pd
import os, re
from bs4 import BeautifulSoup as bs


page = open('./test.html', 'r', encoding='utf8').read()
print(page)

soup = bs(page, 'html.parser')
print(soup)
print(soup.prettify())

soup_children_list = list(soup.children)
print(soup_children_list)
print(soup.body)
print(list(soup.body.children))
print(soup.head)
print(soup.head.next_sibling)
print(soup.head.next_sibling.next_sibling)

print(soup.find_all('p'))
for i in soup.find_all('p'):
    print(i.text)



news = 'https://news.daum.net/'
soup = bs(urlopen(news).read(), 'html.parser')
print(soup)

print(soup.find_all('div', {'class':'item_issue'}))
for i in soup.find_all('div', {'class':'item_issue'}):
    print(i.text)
   
    
news = 'https://news.daum.net/'
soup = bs(urlopen(news).read(), 'html.parser')  

soup.find_all('a')[:5]
for i in soup.find_all('a')[:5]:
    print(i.get('href'))
    
for i in soup.find_all('div', {'class':'item_issue'}):
    print(i.find_all('a'))

for i in soup.find_all('div', {'class':'item_issue'}):
    print(i.find_all('a')[0].get('href'))    
   
    
article1 = 'https://go.seoul.co.kr/news/newsView.php?id=20200427004004&wlog_tag3=daum'    
soup2 = bs(urlopen(article1).read(), 'html.parser')    

for i in soup2.find_all('p'):
    print(i.text)    


news = 'https://news.daum.net/'
soup = bs(urlopen(news).read(), 'html.parser')  
    
headline = soup.find_all('div', {'class':'item_issue'})    
print(headline[0].text)   
 
for i in headline:
    print(i.text)

print(i.find_all('a')[0].get('href'))

soup3 = bs(urlopen(i.find_all('a')[0].get('href')).read(), 'html.parser')
print(soup3)

for j in soup3.find_all('p'):
    print(j.text)


with open('links.txt', 'w') as f:
    for i in soup.find_all('div', {'class':'item_issue'}):
        f.write(i.find_all('a')[0].get('href') + '\n')


article1 = 'https://v.daum.net/v/20230807094500170'
soup = bs(urlopen(article1).read(), 'html.parser')

with open('article_1.txt', 'w') as f:
    for i in soup.find_all('p'):
        f.write(i.text)


url = 'https://news.daum.net/'
soup = bs(urlopen(url).read(), 'html.parser')

with open('article_total.txt', 'w') as f:
    for i in soup.find_all('div', {'class':'item_issue'}):
        try:
            f.write(i.text + '\n')
            f.write(i.find_all('a')[0].get('href') + '\n')
            soup2 = bs(urlopen(i.find_all('a')[0].get('href')).read(), 'html.parser')
            for j in soup2.find_all('p'):
                f.write(j.text + '\n')
        except:
            pass


url = 'https://www.chicagomag.com/chicago-magazine/january-2023/our-30-favorite-things-to-eat-right-now/'

hdr = {'User-Agent':'Mozilla/5.0'}
req = Request(url, headers = hdr)
page = urlopen(req)

soup = bs(page, 'html.parser')
tmp = soup.find_all('div', 'article-body')[0]

food_list=[]
for item in tmp.find_all('h2'):
    food_list.append(item.text)

restaurant_list=[]
for item in tmp.find_all('h3'):
    restaurant_list.append(item.text[3:])

money_list=[]
address_list=[]
for item in tmp.find_all('p'):
    sample_text = item.get_text()
    idx_of_dollar = sample_text.index('$')
    money = sample_text[idx_of_dollar:].split(' ')[0].strip('.')
    dummy_address = sample_text[idx_of_dollar+len(money)+1:]
    if dummy_address.split(' ')[0] == 'for':
        dummy_address = dummy_address[dummy_address.index('. ')+2:]
    money_list.append(money)
    address_list.append(dummy_address.strip())

data = {'food':food_list, 'restaurant':restaurant_list,
        'price':money_list, 'address':address_list}
df = pd.DataFrame(data)
print(df)



    