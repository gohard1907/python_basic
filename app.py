# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 09:23:05 2023

@author: Jung
"""

import streamlit as st
from datetime import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from page import st_page as spg
from page import foliummap as fum

st.title('시험용 메세지입니다.')

todays = dt.today()
tod = todays.strftime('%m 월 %d 일')

st.header(f'오늘은 {tod} 입니다.')

item = st.sidebar.selectbox('항목을 골라요', ['선택1', '콤보2', '세트3'])


if item == '선택1':
    spg.app()
elif item == '콤보2':
    st.write('2번 콤보를 선택했습니다.')
    df = pd.DataFrame(np.arange(15))
    fg, ax = plt.subplots(figsize=(8,8))
    ax.plot(df)
    st.pyplot(fg)
elif item == '세트3':
    fum.app()

























