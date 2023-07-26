# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 09:14:07 2023

@author: Jung
"""

import filesearch_module as fsm

(file_list, s_path) = fsm.Filecollection('numpy', 'py')
#print(file_list)

f_dict = fsm.GetFileSentence(file_list, 'index', s_path)
#print(f_dict)

fsm.print_result(f_dict)
