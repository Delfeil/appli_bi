#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

clients_tbl = pd.read_csv('../donnees/source/data_mining_DB_clients_tbl.csv', sep=',')

print(clients_tbl)

cols = ['Id', 'CDSEXE', 'MTREV', 'NBENF', 'CDSITFAM', 'DTADH', 'CDTMT', 'DTDEM', 'CDMOTDEM', 'CDCATCL', 'AGEAD', 'agedem', 'adh']

isolated_client_tbl = clients_tbl.get(cols)

removed_aberent_data = isolated_client_tbl.loc[(isolated_client_tbl['MTREV'] < 1000000) ]


####
# Transformer NBENF en catégorie
####
    # Si NBENF > 4 -> '4et+'
mask_sup_nbenf = (removed_aberent_data['NBENF'] > 3)
removed_aberent_data['NBENF'][mask_sup_nbenf] = '4 et plus'
print(removed_aberent_data)

removed_aberent_data.to_csv('../donnees/cleaned/data_mining_DB_clients_tbl_cleaned.csv', sep=",", index=False)
