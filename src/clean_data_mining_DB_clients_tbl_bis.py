#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

clients_tbl = pd.read_csv('../donnees/source/data_mining_DB_clients_tbl_bis.csv', sep=',')

print(clients_tbl)

cols = ['Id', 'CDSEXE', 'MTREV', 'NBENF', 'CDSITFAM', 'DTADH', 'CDTMT', 'DTDEM', 'CDMOTDEM', 'CDCATCL', 'AGEAD', 'agedem', 'adh']

