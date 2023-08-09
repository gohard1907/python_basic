# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 16:10:57 2023

@author: Jung
"""

import streamlit as st
from utils import foliummap_module as fumm

def app():
    st.write('3번 세트를 선택했습니다.')
    user_input = st.text_input('글을 입력한 후 버튼을 눌러 주세요.')
    button = st.button('실행버튼')
    if button:
        st.write('버튼을 눌렀기 때문에 다음 문장이 나타납니다.')
        st.write(user_input)
    fumm.foliummap(fumm.data)



 