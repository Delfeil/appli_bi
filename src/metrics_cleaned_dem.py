#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from analyse import analyse_cat
from analyse import analyse_num
import sys


if(len(sys.argv) == 1):
    name = "dem_cleaned"
else:
    name = sys.argv[1]

clients_dem = pd.read_csv('../donnees/fusion/dem.csv', sep=',')


numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
clients_dem_nums = clients_dem.select_dtypes(include=numerics)
clients_dem_cat = clients_dem.select_dtypes(exclude=numerics)

del  clients_dem_nums['CDSEXE']
clients_dem_cat['CDSEXE'] = clients_dem['CDSEXE']
del  clients_dem_nums['CDTMT']
clients_dem_cat['CDTMT'] = clients_dem['CDTMT']
del  clients_dem_nums['CDCATCL']
clients_dem_cat['CDCATCL'] = clients_dem['CDCATCL']

del  clients_dem_cat['DTADH']
del  clients_dem_cat['DTDEM']
clients_dem_cat['NBENF'] = clients_dem['NBENF']

print(clients_dem_nums)
print(clients_dem_cat)

analyse_num(clients_dem_nums, name)

analyse_cat(clients_dem_cat, name)