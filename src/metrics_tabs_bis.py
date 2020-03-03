#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

from histogram import discretize_histogram
from histogram import histogram_cat

plt.ioff()

# def histogram.py(data, col, data_origine):
#     print(data)
#     print(col)
#     fig = plt.figure()
#     plt.subplot(211)
#     matplotlib.pyplot.xticks(fontsize=6)
#     pd.cut(data[col],10).value_counts(sort=False).plot.bar()
#     plt.xticks(rotation=25)
#     # discretize with equal-sized bins
#     plt.subplot(212)
#     matplotlib.pyplot.xticks(fontsize=6)
#     # TODO: plot with qcut
#     pd.qcut(data[col],10, duplicates='drop').value_counts(sort=False).plot.bar()
#     plt.xticks(rotation=25)
#     plt.suptitle('Histogram for '+col+' discretized with equal-intervaled and equal-sized bins')
#     plt.savefig('../fig/'+col+'_histogram_discretization_'+ data_origine)
#     plt.close(fig)

clients_tbl = pd.read_csv('../donnees/source/data_mining_DB_clients_tbl_bis.csv', sep=',')

numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
clients_tbl_nums = clients_tbl.select_dtypes(include=numerics)
clients_tbl_cat = clients_tbl.select_dtypes(exclude=numerics)
del  clients_tbl_nums['Id']
del  clients_tbl_nums['CDSEXE']
clients_tbl_cat['CDSEXE'] = clients_tbl['CDSEXE']
del  clients_tbl_nums['CDTMT']
clients_tbl_cat['CDTMT'] = clients_tbl['CDTMT']
clients_tbl_cat['NBENF'] = clients_tbl['NBENF']
del  clients_tbl_nums['CDCATCL']
clients_tbl_cat['CDCATCL'] = clients_tbl['CDCATCL']
del  clients_tbl_cat['DTNAIS']
del  clients_tbl_cat['DTADH']
del  clients_tbl_cat['DTDEM']
print(clients_tbl_nums)
print(clients_tbl_cat)

print('===========Analyse des numérics===========')
for col in clients_tbl_nums:
    col_num = pd.DataFrame(clients_tbl_nums[col])
    print('-------Colonne: '+ col + "------------")
    print(col_num)
    print("--min: ")
    print(col_num.min())
    print("--max: ")
    print(col_num.max())
    print("--moyenne: ")
    print(col_num.mean())
    print("--equart-type: ")
    print(col_num.std())
    print("--Description: ")
    print(col_num.describe())
    print("--Histogramme: ")
    discretize_histogram(clients_tbl_nums, col, 'bis')


print('===========Analyse des catégories===========')
print(clients_tbl_cat)
for col in clients_tbl_cat:
    print('-------Colonne: '+ col + "------------")
    # print(col)
    col_cat = pd.DataFrame(clients_tbl_cat[col])
    print(col_cat)
    print("--Valeurs: ")
    print(clients_tbl_cat[col].unique())
    print("--Valeurs count: ")
    print(clients_tbl_cat[col].value_counts())
    print("--Valeurs NaN: ")
    print(clients_tbl_cat[col].isna().sum())
    print("--Description: ")
    print(col_cat.astype('object').describe())
    # print("--Histogramme: ")
    histogram_cat(clients_tbl_cat, col, 'bis')
    # histogram.py(clients_tbl_cat, col)
