# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 13:38:51 2023

@author: Jung
"""

import glob

def Filecollection(L_name, file_types):
    s_path = '\\'.join(str(__import__(L_name)).split()[-1].strip('\'').split('\\')[:-1]) + '\\'
    #s_path = str(__import__(L_name)).split('\'')[3][:-11]
    #print(s_path)
    dummy_arg = s_path + '**\\\*.' + file_types
    file_lists = glob.glob(dummy_arg, recursive = True)
    return (file_lists, s_path)

def GetFileSentence(file_list, search_sentences, s_path):
    file_dict = {}
    for filename in file_list:
        #print(filename)
        sentence_list = []
        with open(filename, encoding = 'utf-8') as f:
            lines = f.readlines()
        for item in lines:
            if search_sentences in item:
                sentence_list.append(item)
        if sentence_list:
            file_dict[filename[len(s_path):]] = sentence_list
    return(file_dict)

def print_result(fdr):
    for i in fdr:
        print(i)
        print('===' * 10)
        for j in fdr[i]:
            print('-   ', j.strip())
        print()
        
    
(file_list, s_path) = Filecollection('numpy', 'py')
f_dict = GetFileSentence(file_list, 'index', s_path)
print_result(f_dict)
