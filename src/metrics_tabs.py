#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

from analyse import analyse_cat
from analyse import analyse_num

plt.ioff()

clients_tbl = pd.read_csv('../donnees/source/data_mining_DB_clients_tbl.csv', sep=',')

numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
clients_tbl_nums = clients_tbl.select_dtypes(include=numerics)
clients_tbl_cat = clients_tbl.select_dtypes(exclude=numerics)
del clients_tbl_nums['Id']
del clients_tbl_nums['ANNEE_DEM']
del  clients_tbl_nums['CDDEM']
del  clients_tbl_nums['CDSEXE']
clients_tbl_cat['CDSEXE'] = clients_tbl['CDSEXE']
del  clients_tbl_nums['CDTMT']
clients_tbl_cat['CDTMT'] = clients_tbl['CDTMT']
del  clients_tbl_nums['CDCATCL']
clients_tbl_cat['CDCATCL'] = clients_tbl['CDCATCL']
print(clients_tbl_nums)
del clients_tbl_cat['DTADH']
del clients_tbl_cat['DTDEM']
del clients_tbl_cat['rangagead']
del clients_tbl_cat['rangdem']
del clients_tbl_cat['rangadh']
del clients_tbl_cat['rangagedem']
clients_tbl_cat['NBENF'] = clients_tbl['NBENF']
print(clients_tbl_cat)

analyse_num(clients_tbl_nums, '')
# print('===========Analyse des numérics===========')
# for col in clients_tbl_nums:
#     col_num = pd.DataFrame(clients_tbl_nums[col])
#     print('-------Colonne: '+ col + "------------")
#     print(col_num)
#     print("--min: ")
#     print(col_num.min())
#     print("--max: ")
#     print(col_num.max())
#     print("--moyenne: ")
#     print(col_num.mean())
#     print("--equart-type: ")
#     print(col_num.std())
#     print("--Description: ")
#     print(col_num.describe())
#     print("--Histogramme: ")
#     discretize_histogram(clients_tbl_nums, col, '')


analyse_cat(clients_tbl_cat, '')
# print('===========Analyse des catégories===========')
# print(clients_tbl_cat)
# for col in clients_tbl_cat:
#     print('-------Colonne: '+ col + "------------")
#     # print(col)
#     col_cat = pd.DataFrame(clients_tbl_cat[col])
#     print(col_cat)
#     print("--Valeurs: ")
#     print(clients_tbl_cat[col].unique())
#     print("--Valeurs count: ")
#     print(clients_tbl_cat[col].value_counts())
#     print("--Valeurs NaN: ")
#     print(clients_tbl_cat[col].isna().sum())
#     print("--Description: ")
#     print(col_cat.astype('object').describe())
#     # print("--Histogramme: ")
#     histogram_cat(clients_tbl_cat, col, '')
#     # histogram.py(clients_tbl_cat, col)
