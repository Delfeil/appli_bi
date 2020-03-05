#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from analyse import analyse_cat
from analyse import analyse_num
import sys

if(len(sys.argv) == 1):
    name = "adh_cleaned"
else:
    name = sys.argv[1]


clients_adh = pd.read_csv('../donnees/fusion/adh.csv', sep=',')


numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
clients_adh_nums = clients_adh.select_dtypes(include=numerics)
clients_adh_cat = clients_adh.select_dtypes(exclude=numerics)


del  clients_adh_nums['Id']
del  clients_adh_nums['CDSEXE']
clients_adh_cat['CDSEXE'] = clients_adh['CDSEXE']
del  clients_adh_nums['CDCATCL']
clients_adh_cat['CDCATCL'] = clients_adh['CDCATCL']
del  clients_adh_nums['CDTMT']
clients_adh_cat['CDTMT'] = clients_adh['CDTMT']


del  clients_adh_cat['DTADH']
clients_adh_cat['NBENF'] = clients_adh['NBENF']

print(clients_adh_nums)
print(clients_adh_cat)


analyse_num(clients_adh_nums, name)

analyse_cat(clients_adh_cat, name)