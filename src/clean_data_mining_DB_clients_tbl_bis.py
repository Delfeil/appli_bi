#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from datetime import datetime
import numpy as np

clients_tbl = pd.read_csv('../donnees/source/data_mining_DB_clients_tbl_bis.csv', sep=',')

print(clients_tbl)

cols = ['Id', 'CDSEXE', 'MTREV', 'NBENF', 'CDSITFAM', 'DTADH', 'CDTMT', 'DTDEM', 'CDMOTDEM', 'CDCATCL']
add_cols = ['AGEAD', 'agedem', 'adh']

# Données :
# Id
# CDSEXE
# MTREV
# NBENF
# CDSITFAM
# DTADH
# CDTMT
# DTDEM
# CDMOTDEM (!!vide = NaN)
# CDCATCL
# Age debut -> AGEAD
# Age Fin -> agedem
# Durée du contrat -> adh

    # Faire péter celles ou DTNAIS pourris
# date_none = datetime.strptime(0, 0, 0000)
cleaned_clients_tbl = clients_tbl.loc[(clients_tbl['DTNAIS'] != "0000-00-00") & (clients_tbl['DTNAIS'] != "1900-01-00") ]
print(cleaned_clients_tbl)

cleaned_clients_tbl_selected_cols = cleaned_clients_tbl[cols]
print(cleaned_clients_tbl_selected_cols)
# date_2007 = datetime.strptime(1, 1, 2007)
# datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')

    # si CDMOTDEM masi pas DTDEM -> mettre 2007-01-01

print(cleaned_clients_tbl_selected_cols['CDMOTDEM'])
# pd.notna()
print(cleaned_clients_tbl_selected_cols.loc[(pd.notna(cleaned_clients_tbl_selected_cols['CDMOTDEM'])) & (cleaned_clients_tbl_selected_cols['DTDEM'] == '1900-12-31')])

mask = (pd.notna(cleaned_clients_tbl_selected_cols['CDMOTDEM'])) & (cleaned_clients_tbl_selected_cols['DTDEM'] == '1900-12-31')
cleaned_clients_tbl_selected_cols['DTDEM'][mask] = '2007-01-01'
print(cleaned_clients_tbl_selected_cols)

    # On isole les clients toujours adhérents des clients ayant quittés
cleaned_clients_tbl_selected_cols_adh = cleaned_clients_tbl_selected_cols.loc[(pd.isna(cleaned_clients_tbl_selected_cols['CDMOTDEM']))]
cleaned_clients_tbl_selected_cols_dem = cleaned_clients_tbl_selected_cols.loc[(pd.notna(cleaned_clients_tbl_selected_cols['CDMOTDEM']))]
del cleaned_clients_tbl_selected_cols_adh['CDMOTDEM']
print(cleaned_clients_tbl_selected_cols_adh)
# print(cleaned_clients_tbl_selected_cols_dem)
# rules_supermarket["nb_consequents"] = rules_supermarket["consequents"].map(lambda consequents: len(consequents))

cleaned_clients_tbl_selected_cols_adh.to_csv('../donnees/cleaned/data_mining_DB_clients_tbl_bis_adh_cleaned.csv', sep=",", index=False)
cleaned_clients_tbl_selected_cols_dem.to_csv('../donnees/cleaned/data_mining_DB_clients_tbl_bis_dem_cleaned.csv', sep=",", index=False)
