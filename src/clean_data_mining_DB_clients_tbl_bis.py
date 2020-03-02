#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from datetime import datetime

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

# // Faire péter celles ou DTNAIS pourris
# date_none = datetime.strptime(0, 0, 0000)
cleaned_clients_tbl = clients_tbl.loc[(clients_tbl['DTNAIS'] != "0000-00-00") & (clients_tbl['DTNAIS'] != "1900-01-00") ]
print(cleaned_clients_tbl)

cleaned_clients_tbl_selected_cols = cleaned_clients_tbl[cols]
print(cleaned_clients_tbl_selected_cols)
# date_2007 = datetime.strptime(1, 1, 2007)
# datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')

# si CDMOTDEM masi pas DTDEM -> mettre 01/01/2007
# isolated_client_tbl = clients_tbl.get(cols)
#
# removed_aberent_data = isolated_client_tbl.loc[(isolated_client_tbl['MTREV'] < 1000000) ]
