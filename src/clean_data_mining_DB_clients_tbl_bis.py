#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from datetime import datetime
import numpy as np

clients_tbl = pd.read_csv('../donnees/source/data_mining_DB_clients_tbl_bis.csv', sep=',')

# print(clients_tbl)

cols_dem = ['Id', 'CDSEXE', 'MTREV', 'NBENF', 'CDSITFAM', 'DTADH', 'CDTMT', 'DTDEM', 'CDMOTDEM', 'CDCATCL', 'AGEAD', 'agedem', 'adh']
cols_adh = ['Id', 'CDSEXE', 'MTREV', 'NBENF', 'CDSITFAM', 'DTADH', 'CDTMT', 'CDCATCL', 'AGEAD', 'ageactu', 'adh']

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
cleaned_clients_tbl = clients_tbl.loc[(clients_tbl['DTNAIS'] != "0000-00-00") & (clients_tbl['DTNAIS'] != "1900-01-00") ]

    ###
    # Enlever les lignes avec une valeur dans CDMOTDEM
    # Mais la valeur par défaut dans
    ###
# print(cleaned_clients_tbl)
cleaned_clients_tbl = clients_tbl.loc[((pd.notna(cleaned_clients_tbl['CDMOTDEM'])) & (clients_tbl['DTDEM'] != "1900-12-31")) | (pd.isna(cleaned_clients_tbl['CDMOTDEM'])) ]
# print(cleaned_clients_tbl)
#
# exit()
####
# Transformer NBENF en catégorie
####
    # Si NBENF > 4 -> '4et+'
mask_sup_nbenf = (cleaned_clients_tbl['NBENF'] > 3)
cleaned_clients_tbl['NBENF'][mask_sup_nbenf] = '4 et plus'

        # On calcul AGEAD (L'âge de la personne quand il ait adhéré)
    # AGAD = DTADH - DTNAIS
cleaned_clients_tbl["AGEAD"] = cleaned_clients_tbl.apply(lambda row: datetime.strptime(row['DTADH'], '%Y-%m-%d').year - datetime.strptime(row['DTNAIS'], '%Y-%m-%d').year, axis=1)

    # On isole les clients toujours adhérents des clients démissionaires
cleaned_clients_tbl_adh = cleaned_clients_tbl.loc[(pd.isna(cleaned_clients_tbl['CDMOTDEM']))]
cleaned_clients_tbl_dem = cleaned_clients_tbl.loc[(pd.notna(cleaned_clients_tbl['CDMOTDEM']))]
del cleaned_clients_tbl_adh['CDMOTDEM']
del cleaned_clients_tbl_adh['DTDEM']

print(cleaned_clients_tbl_adh)
print(cleaned_clients_tbl_dem)
    # si CDMOTDEM masi pas DTDEM -> mettre 2007-01-01
print(cleaned_clients_tbl_dem['CDMOTDEM'])
print(cleaned_clients_tbl_dem.loc[(pd.notna(cleaned_clients_tbl_dem['CDMOTDEM'])) & (cleaned_clients_tbl_dem['DTDEM'] == '1900-12-31')])

    # MAsk contenant seulement les lignes avec CDMOTDEM non nul et DTDEM non défini
mask = (pd.notna(cleaned_clients_tbl_dem['CDMOTDEM'])) & (cleaned_clients_tbl_dem['DTDEM'] == '1900-12-31')
cleaned_clients_tbl_dem['DTDEM'][mask] = '2007-01-01'
print(cleaned_clients_tbl_dem)
# print(cleaned_clients_tbl_adh)

############
#   Ajout des colonnes manquantes
#######

    # On calcul agedem: L'âge de la personne quand il a démissioné (pour les démissionaires)
cleaned_clients_tbl_dem["agedem"] = cleaned_clients_tbl_dem.apply(lambda row: datetime.strptime(row['DTDEM'], '%Y-%m-%d').year - datetime.strptime(row['DTNAIS'], '%Y-%m-%d').year, axis=1)

    # On calcul ageactu: L'âge en 2007 des personnes adhérentes
cleaned_clients_tbl_adh["ageactu"] = cleaned_clients_tbl_adh.apply(lambda row: datetime.strptime('2007-01-01', '%Y-%m-%d').year - datetime.strptime(row['DTNAIS'], '%Y-%m-%d').year, axis=1)

    # On calcul adh: la durée d'adhésion
cleaned_clients_tbl_dem["adh"] = cleaned_clients_tbl_dem.apply(lambda row: datetime.strptime(row['DTDEM'], '%Y-%m-%d').year - datetime.strptime(row['DTADH'], '%Y-%m-%d').year, axis=1)
        # Pour les personnes toujours adhérentes, on compare avec 2007-01-01
cleaned_clients_tbl_adh["adh"] = cleaned_clients_tbl_adh.apply(lambda row: datetime.strptime('2007-01-01', '%Y-%m-%d').year - datetime.strptime(row['DTADH'], '%Y-%m-%d').year, axis=1)
print(cleaned_clients_tbl_adh)

    # Sélection des collones
print("----------------------ICI--------------------")
# cleaned_clients_tbl_selected_cols = cleaned_clients_tbl[cols]
cleaned_clients_tbl_adh_selected_cols = cleaned_clients_tbl_adh[cols_adh]
cleaned_clients_tbl_dem_selected_cols = cleaned_clients_tbl_dem[cols_dem]
print(cleaned_clients_tbl_adh_selected_cols)
print(cleaned_clients_tbl_dem_selected_cols)



    # Ecriture dans les csv
cleaned_clients_tbl_adh_selected_cols.to_csv('../donnees/fusion/adh.csv', sep=",", index=False)
cleaned_clients_tbl_dem_selected_cols.to_csv('../donnees/cleaned/data_mining_DB_clients_tbl_bis_dem_cleaned.csv', sep=",", index=False)
