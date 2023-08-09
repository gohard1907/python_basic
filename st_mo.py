# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 14:13:14 2023

@author: Jung
"""
import requests
import pandas as pd
import json

def get_movie():
    url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=c3a0fa760324363ef7cde2afa0d73297&targetDt=20230807'
    resp = requests.get(url)
    data = resp.json()['boxOfficeResult']['dailyBoxOfficeList']
    dataframe_of_movie = pd.DataFrame(data)
    df = dataframe_of_movie.loc[:, ['rank', 'movieNm', 'openDt', 'salesAmt']]
    return df




