#!/usr/bin/env python
# -*- coding: utf-8 -*-

def clean_client_tbl_bis():
    print("##################################")
    print("#####RUN CLEAN CLIENT TBL BIS#####")
    print("##################################")
    import pandas as pd
    from datetime import datetime
    import numpy as np

    clients_tbl = pd.read_csv('../donnees/source/data_mining_DB_clients_tbl_bis.csv', sep=',')

    # print(clients_tbl)

    cols_dem = ['Id', 'CDSEXE', 'MTREV', 'NBENF', 'CDSITFAM', 'DTADH', 'CDTMT', 'DTDEM', 'CDMOTDEM', 'CDCATCL', 'AGEAD', 'agedem', 'adh', 'CATAGEAD', 'CATagedem', 'CATadh', 'is_adh']
    cols_adh = ['Id', 'CDSEXE', 'MTREV', 'NBENF', 'CDSITFAM', 'DTADH', 'CDTMT', 'CDCATCL', 'AGEAD', 'ageactu', 'adh', 'CATAGEAD', 'CATageactu', 'CATadh', 'is_adh']

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
    mask_sup_nbenf = (cleaned_clients_tbl['NBENF'] >= 1)
    cleaned_clients_tbl['NBENF'][mask_sup_nbenf] = 'enfants'

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



        ###
        # Trnasformer les ages en tranche d'âge pour les demissionaires
        ###
    ## entre 0-10, 11-20; 21-30; 31-40; 41-50; 51-60; 61-70; 71+
    print(cleaned_clients_tbl_dem['AGEAD'])
    #  AGEAD
    AGEAD_0_10 = (cleaned_clients_tbl_dem['AGEAD'] <=10)
    AGEAD_11_20 = ((cleaned_clients_tbl_dem['AGEAD'] > 10) & (cleaned_clients_tbl_dem['AGEAD'] <= 20))
    AGEAD_21_30 = ((cleaned_clients_tbl_dem['AGEAD'] > 20) & (cleaned_clients_tbl_dem['AGEAD'] <= 30))
    AGEAD_31_40 = ((cleaned_clients_tbl_dem['AGEAD'] > 30) & (cleaned_clients_tbl_dem['AGEAD'] <= 40))
    AGEAD_41_50 = ((cleaned_clients_tbl_dem['AGEAD'] > 40) & (cleaned_clients_tbl_dem['AGEAD'] <= 50))
    AGEAD_51_60 = ((cleaned_clients_tbl_dem['AGEAD'] > 50) & (cleaned_clients_tbl_dem['AGEAD'] <= 60))
    AGEAD_61_70 = ((cleaned_clients_tbl_dem['AGEAD'] > 60) & (cleaned_clients_tbl_dem['AGEAD'] <= 70))
    AGEAD_71 = (cleaned_clients_tbl_dem['AGEAD'] > 70)
    cleaned_clients_tbl_dem['CATAGEAD'] = ''
    cleaned_clients_tbl_dem['CATAGEAD'][AGEAD_0_10] = '0_10'
    cleaned_clients_tbl_dem['CATAGEAD'][AGEAD_11_20] = '11_20'
    cleaned_clients_tbl_dem['CATAGEAD'][AGEAD_21_30] = '21_30'
    cleaned_clients_tbl_dem['CATAGEAD'][AGEAD_31_40] = '31_40'
    cleaned_clients_tbl_dem['CATAGEAD'][AGEAD_41_50] = '41_50'
    cleaned_clients_tbl_dem['CATAGEAD'][AGEAD_51_60] = '51_60'
    cleaned_clients_tbl_dem['CATAGEAD'][AGEAD_61_70] = '61_70'
    cleaned_clients_tbl_dem['CATAGEAD'][AGEAD_71] = '71plus'

    # adh
    adh_0_10 = (cleaned_clients_tbl_dem['adh'] <=10)
    adh_11_20 = ((cleaned_clients_tbl_dem['adh'] > 10) & (cleaned_clients_tbl_dem['adh'] <= 20))
    adh_21_30 = ((cleaned_clients_tbl_dem['adh'] > 20) & (cleaned_clients_tbl_dem['adh'] <= 30))
    adh_31_40 = ((cleaned_clients_tbl_dem['adh'] > 30) & (cleaned_clients_tbl_dem['adh'] <= 40))
    adh_41_50 = ((cleaned_clients_tbl_dem['adh'] > 40) & (cleaned_clients_tbl_dem['adh'] <= 50))
    adh_51_60 = ((cleaned_clients_tbl_dem['adh'] > 50) & (cleaned_clients_tbl_dem['adh'] <= 60))
    adh_61_70 = ((cleaned_clients_tbl_dem['adh'] > 60) & (cleaned_clients_tbl_dem['adh'] <= 70))
    adh_71 = (cleaned_clients_tbl_dem['adh'] > 70)
    cleaned_clients_tbl_dem['CATadh'] = ''
    cleaned_clients_tbl_dem['CATadh'][adh_0_10] = '0_10'
    cleaned_clients_tbl_dem['CATadh'][adh_11_20] = '11_20'
    cleaned_clients_tbl_dem['CATadh'][adh_21_30] = '21_30'
    cleaned_clients_tbl_dem['CATadh'][adh_31_40] = '31_40'
    cleaned_clients_tbl_dem['CATadh'][adh_41_50] = '41_50'
    cleaned_clients_tbl_dem['CATadh'][adh_51_60] = '51_60'
    cleaned_clients_tbl_dem['CATadh'][adh_61_70] = '61_70'
    cleaned_clients_tbl_dem['CATadh'][adh_71] = '71plus'

    # agedem
    agedem_0_10 = (cleaned_clients_tbl_dem['agedem'] <=10)
    agedem_11_20 = ((cleaned_clients_tbl_dem['agedem'] > 10) & (cleaned_clients_tbl_dem['agedem'] <= 20))
    agedem_21_30 = ((cleaned_clients_tbl_dem['agedem'] > 20) & (cleaned_clients_tbl_dem['agedem'] <= 30))
    agedem_31_40 = ((cleaned_clients_tbl_dem['agedem'] > 30) & (cleaned_clients_tbl_dem['agedem'] <= 40))
    agedem_41_50 = ((cleaned_clients_tbl_dem['agedem'] > 40) & (cleaned_clients_tbl_dem['agedem'] <= 50))
    agedem_51_60 = ((cleaned_clients_tbl_dem['agedem'] > 50) & (cleaned_clients_tbl_dem['agedem'] <= 60))
    agedem_61_70 = ((cleaned_clients_tbl_dem['agedem'] > 60) & (cleaned_clients_tbl_dem['agedem'] <= 70))
    agedem_71 = (cleaned_clients_tbl_dem['agedem'] > 70)
    cleaned_clients_tbl_dem['CATagedem'] = ''
    cleaned_clients_tbl_dem['CATagedem'][agedem_0_10] = '0_10'
    cleaned_clients_tbl_dem['CATagedem'][agedem_11_20] = '11_20'
    cleaned_clients_tbl_dem['CATagedem'][agedem_21_30] = '21_30'
    cleaned_clients_tbl_dem['CATagedem'][agedem_31_40] = '31_40'
    cleaned_clients_tbl_dem['CATagedem'][agedem_41_50] = '41_50'
    cleaned_clients_tbl_dem['CATagedem'][agedem_51_60] = '51_60'
    cleaned_clients_tbl_dem['CATagedem'][agedem_61_70] = '61_70'
    cleaned_clients_tbl_dem['CATagedem'][agedem_71] = '71plus'


        ###
        # Trnasformer les ages en tranche d'âge pour les adhérents
        ###
    ## entre 0-10, 11-20; 21-30; 31-40; 41-50; 51-60; 61-70; 71+
    print(cleaned_clients_tbl_adh['AGEAD'])
    #  AGEAD
    AGEAD_0_10 = (cleaned_clients_tbl_adh['AGEAD'] <=10)
    AGEAD_11_20 = ((cleaned_clients_tbl_adh['AGEAD'] > 10) & (cleaned_clients_tbl_adh['AGEAD'] <= 20))
    AGEAD_21_30 = ((cleaned_clients_tbl_adh['AGEAD'] > 20) & (cleaned_clients_tbl_adh['AGEAD'] <= 30))
    AGEAD_31_40 = ((cleaned_clients_tbl_adh['AGEAD'] > 30) & (cleaned_clients_tbl_adh['AGEAD'] <= 40))
    AGEAD_41_50 = ((cleaned_clients_tbl_adh['AGEAD'] > 40) & (cleaned_clients_tbl_adh['AGEAD'] <= 50))
    AGEAD_51_60 = ((cleaned_clients_tbl_adh['AGEAD'] > 50) & (cleaned_clients_tbl_adh['AGEAD'] <= 60))
    AGEAD_61_70 = ((cleaned_clients_tbl_adh['AGEAD'] > 60) & (cleaned_clients_tbl_adh['AGEAD'] <= 70))
    AGEAD_71 = (cleaned_clients_tbl_adh['AGEAD'] > 70)
    cleaned_clients_tbl_adh['CATAGEAD'] = ''
    cleaned_clients_tbl_adh['CATAGEAD'][AGEAD_0_10] = '0_10'
    cleaned_clients_tbl_adh['CATAGEAD'][AGEAD_11_20] = '11_20'
    cleaned_clients_tbl_adh['CATAGEAD'][AGEAD_21_30] = '21_30'
    cleaned_clients_tbl_adh['CATAGEAD'][AGEAD_31_40] = '31_40'
    cleaned_clients_tbl_adh['CATAGEAD'][AGEAD_41_50] = '41_50'
    cleaned_clients_tbl_adh['CATAGEAD'][AGEAD_51_60] = '51_60'
    cleaned_clients_tbl_adh['CATAGEAD'][AGEAD_61_70] = '61_70'
    cleaned_clients_tbl_adh['CATAGEAD'][AGEAD_71] = '71plus'

    # adh
    adh_0_10 = (cleaned_clients_tbl_adh['adh'] <=10)
    adh_11_20 = ((cleaned_clients_tbl_adh['adh'] > 10) & (cleaned_clients_tbl_adh['adh'] <= 20))
    adh_21_30 = ((cleaned_clients_tbl_adh['adh'] > 20) & (cleaned_clients_tbl_adh['adh'] <= 30))
    adh_31_40 = ((cleaned_clients_tbl_adh['adh'] > 30) & (cleaned_clients_tbl_adh['adh'] <= 40))
    adh_41_50 = ((cleaned_clients_tbl_adh['adh'] > 40) & (cleaned_clients_tbl_adh['adh'] <= 50))
    adh_51_60 = ((cleaned_clients_tbl_adh['adh'] > 50) & (cleaned_clients_tbl_adh['adh'] <= 60))
    adh_61_70 = ((cleaned_clients_tbl_adh['adh'] > 60) & (cleaned_clients_tbl_adh['adh'] <= 70))
    adh_71 = (cleaned_clients_tbl_adh['adh'] > 70)
    cleaned_clients_tbl_adh['CATadh'] = ''
    cleaned_clients_tbl_adh['CATadh'][adh_0_10] = '0_10'
    cleaned_clients_tbl_adh['CATadh'][adh_11_20] = '11_20'
    cleaned_clients_tbl_adh['CATadh'][adh_21_30] = '21_30'
    cleaned_clients_tbl_adh['CATadh'][adh_31_40] = '31_40'
    cleaned_clients_tbl_adh['CATadh'][adh_41_50] = '41_50'
    cleaned_clients_tbl_adh['CATadh'][adh_51_60] = '51_60'
    cleaned_clients_tbl_adh['CATadh'][adh_61_70] = '61_70'
    cleaned_clients_tbl_adh['CATadh'][adh_71] = '71plus'

    # ageactu
    ageactu_0_10 = (cleaned_clients_tbl_adh['ageactu'] <=10)
    ageactu_11_20 = ((cleaned_clients_tbl_adh['ageactu'] > 10) & (cleaned_clients_tbl_adh['ageactu'] <= 20))
    ageactu_21_30 = ((cleaned_clients_tbl_adh['ageactu'] > 20) & (cleaned_clients_tbl_adh['ageactu'] <= 30))
    ageactu_31_40 = ((cleaned_clients_tbl_adh['ageactu'] > 30) & (cleaned_clients_tbl_adh['ageactu'] <= 40))
    ageactu_41_50 = ((cleaned_clients_tbl_adh['ageactu'] > 40) & (cleaned_clients_tbl_adh['ageactu'] <= 50))
    ageactu_51_60 = ((cleaned_clients_tbl_adh['ageactu'] > 50) & (cleaned_clients_tbl_adh['ageactu'] <= 60))
    ageactu_61_70 = ((cleaned_clients_tbl_adh['ageactu'] > 60) & (cleaned_clients_tbl_adh['ageactu'] <= 70))
    ageactu_71 = (cleaned_clients_tbl_adh['ageactu'] > 70)
    cleaned_clients_tbl_adh['CATageactu'] = ''
    cleaned_clients_tbl_adh['CATageactu'][ageactu_0_10] = '0_10'
    cleaned_clients_tbl_adh['CATageactu'][ageactu_11_20] = '11_20'
    cleaned_clients_tbl_adh['CATageactu'][ageactu_21_30] = '21_30'
    cleaned_clients_tbl_adh['CATageactu'][ageactu_31_40] = '31_40'
    cleaned_clients_tbl_adh['CATageactu'][ageactu_41_50] = '41_50'
    cleaned_clients_tbl_adh['CATageactu'][ageactu_51_60] = '51_60'
    cleaned_clients_tbl_adh['CATageactu'][ageactu_61_70] = '61_70'
    cleaned_clients_tbl_adh['CATageactu'][ageactu_71] = '71plus'

    ###
    # ajout de la classe is_adh = démissionnaire | adherent
    ###
    cleaned_clients_tbl_dem['is_adh'] = 'demissionnaire'
    cleaned_clients_tbl_adh['is_adh'] = 'adherent'



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
    print("##################################")
    print("#####END CLEAN CLIENT TBL BIS#####")
    print("##################################")

if __name__ == "__main__":
    clean_client_tbl_bis()