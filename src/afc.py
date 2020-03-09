#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from fanalysis.ca import CA

clients_adh = pd.read_csv('../donnees/fusion/adh.csv', sep=',')
clients_dem = pd.read_csv('../donnees/fusion/dem.csv', sep=',')

numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
# print(clients_adh)
clients_adh_cat = clients_adh.select_dtypes(exclude=numerics)
del clients_adh_cat['DTADH']
del clients_adh_cat['is_adh']
del clients_adh_cat['CATageactu']
clients_adh_cat['CDSEXE'] = clients_adh['CDSEXE']
clients_adh_cat['CDTMT'] = clients_adh['CDTMT']
clients_adh_cat['CDCATCL'] = clients_adh['CDCATCL']
print(clients_adh_cat)

# print(clients_dem)
clients_dem_cat = clients_dem.select_dtypes(exclude=numerics)
del clients_dem_cat['CDMOTDEM']
del clients_dem_cat['DTADH']
del clients_dem_cat['DTDEM']
del clients_dem_cat['is_adh']
del clients_dem_cat['CATagedem']
clients_dem_cat['CDSEXE'] = clients_dem['CDSEXE']
clients_dem_cat['CDTMT'] = clients_dem['CDTMT']
clients_dem_cat['CDCATCL'] = clients_dem['CDCATCL']
print(clients_dem_cat)

categories = []

for col_cat in clients_dem_cat:
    # print(col_cat)
    cats = col_cat + '-' + clients_dem_cat[col_cat].apply(str).unique()
    # print(cats)
    categories.extend(cats.tolist())

print(categories)

exit()
clients_dem_adh_cat = pd.DataFrame(clients_adh_cat).append( pd.DataFrame(clients_dem_cat))
print(clients_dem_adh_cat)

my_ca = CA(row_labels=clients_dem_adh_cat.index.values, col_labels=clients_dem_adh_cat.columns.values)


###
# Créer un Tableau compatible avec l'AFC
###
#               | NBEND_0 | NBEND1+ | CDSITFAM_M | CDSITFAM_A...
# demissionaire |
# --------------|-----------------------
# adhérent      |

print(my_ca)

print(my_ca.row_topandas())