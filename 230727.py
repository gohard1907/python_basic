# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 13:39:07 2023

@author: Jung
"""

import matplotlib.pyplot as plt

prices = [7, 1, 5, 3, 6,4]
print(plt.plot(prices))

def stock_profit(price):
    buy = min(price)
    buy_index = price.index(buy)
    sell = max(price[buy_index + 1:])
    profit = sell - buy
    return profit

print(stock_profit(prices))


def trans_matrix(file):
    with open('data.txt') as f:
        matrix = [list(map(int, line.strip().split())) for line in f]
        return [list(row) for row in zip(*matrix)]
        #*matrix == [1, 2, 3], [4, 5, 6], [7, 8, 9]
        
file = 'data.txt'
print(trans_matrix(file))


data = {
'Eoleumgol' : [35.570678, 128.986135],
'Bangujeong' : [37.867614, 126.752505], 'Abgujeong':[37.531713, 127.029154],
'Guemgangsonamusup': [36.985459, 129.205468],
'Heonanseolheonmyo': [37.425569, 127.296012],
'Baegdamsa': [38.164890, 128.374023],
'Moagsan mileugbul' : [35.723051, 127.053816],
'Hailli' : [37.680120, 126.398192],
'Ieodo': [32.116883, 125.166683],
'Bughansan' : [37.659318, 126.9775415],
'Ondalsanseong' : [37.057707, 128.484972],
'Cheonglyeongpo' : [37.176118, 128.445583],
'Hansanseom' : [34.816761, 128.423040],
'Haeinsa' : [35.801479, 128.098052],
'Sancheonjae' : [35.275175, 127.849891],
'Seomjingang' : [34.963452, 127.760620],
'Baegheungam' : [35.994240, 128.778653],
'Guksaseonangdang': [37.696354, 128.753741],
'Mudeungsan' : [35.134134, 126.988756],
'Busanseong' : [36.268112, 126.914802],
'Cheolsanri' : [37.808038, 126.450912], 'Odusan' : [37.773131, 126.677203]
}


import folium
maps = folium.Map(location = [37.5602, 126.982], zoom_start = 7, tiles = 'cartodbpositron')

for i in data:
    name = i
    lat_ = data[i][0]
    long_ = data[i][1]
    folium.CircleMarker([lat_, long_], radius = 4, popup = name, color = 'red', fill_color = 'red').add_to(maps)
    #print(name, lat_, long_)

maps.save('tour.html')

def MarkMap(data):
    maps = folium.Map(location = [37.5602, 126.982], zoom_start = 7)
    for i in data:
        name = i
        lat_ = data[i][0]
        long_ = data[i][1]
        folium.CircleMarker([lat_, long_], radius = 4, popup = name, color = 'red', fill_color = 'red').add_to(maps)
    maps.save('myplace.html')

data = {'home':[37.504611497754084, 126.91929428963795], 'cgv_yeouido':[37.52481642897817, 126.92606015165578], 'chungjuho':[36.98028035426848, 128.08915312422508], 'dokdo':[37.2407534640442, 131.8695212529367]}
MarkMap(data)



class Calculator:
    def __init__(self): #생성자, 메서드
        self.result = 0
    def add(self, num): #메서드
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))



url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=c3a0fa760324363ef7cde2afa0d73297&targetDt=20230726'

import requests
resp = requests.get(url)
data = resp.json()

def movie_info(data):
    info_list = []
    for data in data_list:
        rank = data.get('rank')
        movie_name = data.get('movieNm')
        open_date = data.get('openDt')
        sales_amount = data.get('salesAmt')

        info_list.append({
            'Rank': rank,
            'Movie Name': movie_name,
            'Open Date': open_date,
            'Sales Amount': sales_amount
        })

    return info_list

data_list = data['boxOfficeResult']['dailyBoxOfficeList']
print(movie_info(data_list))


import pandas as pd

datas = pd.DataFrame(data['boxOfficeResult']['dailyBoxOfficeList'])
print(datas)




















