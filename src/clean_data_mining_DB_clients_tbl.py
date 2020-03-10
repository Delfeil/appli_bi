#!/usr/bin/env python
# -*- coding: utf-8 -*-

def clean_client_tbl():
    print("##############################")
    print("#####RUN CLEAN CLIENT TBL#####")
    print("##############################")
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
    mask_sup_nbenf = (removed_aberent_data['NBENF'] >=1)
    removed_aberent_data['NBENF'][mask_sup_nbenf] = 'enfants'


        ###
        # Trnasformer les ages en tranche d'âge
        ###
    ## entre 0-10, 11-20; 21-30; 31-40; 41-50; 51-60; 61-70; 71+
    print(removed_aberent_data['AGEAD'])
    #  AGEAD
    AGEAD_0_10 = (removed_aberent_data['AGEAD'] <=10)
    AGEAD_11_20 = ((removed_aberent_data['AGEAD'] > 10) & (removed_aberent_data['AGEAD'] <= 20))
    AGEAD_21_30 = ((removed_aberent_data['AGEAD'] > 20) & (removed_aberent_data['AGEAD'] <= 30))
    AGEAD_31_40 = ((removed_aberent_data['AGEAD'] > 30) & (removed_aberent_data['AGEAD'] <= 40))
    AGEAD_41_50 = ((removed_aberent_data['AGEAD'] > 40) & (removed_aberent_data['AGEAD'] <= 50))
    AGEAD_51_60 = ((removed_aberent_data['AGEAD'] > 50) & (removed_aberent_data['AGEAD'] <= 60))
    AGEAD_61_70 = ((removed_aberent_data['AGEAD'] > 60) & (removed_aberent_data['AGEAD'] <= 70))
    AGEAD_71 = (removed_aberent_data['AGEAD'] > 70)
    removed_aberent_data['CATAGEAD'] = ''
    removed_aberent_data['CATAGEAD'][AGEAD_0_10] = '0_10'
    removed_aberent_data['CATAGEAD'][AGEAD_11_20] = '11_20'
    removed_aberent_data['CATAGEAD'][AGEAD_21_30] = '21_30'
    removed_aberent_data['CATAGEAD'][AGEAD_31_40] = '31_40'
    removed_aberent_data['CATAGEAD'][AGEAD_41_50] = '41_50'
    removed_aberent_data['CATAGEAD'][AGEAD_51_60] = '51_60'
    removed_aberent_data['CATAGEAD'][AGEAD_61_70] = '61_70'
    removed_aberent_data['CATAGEAD'][AGEAD_71] = '71plus'

    # adh
    adh_0_10 = (removed_aberent_data['adh'] <=10)
    adh_11_20 = ((removed_aberent_data['adh'] > 10) & (removed_aberent_data['adh'] <= 20))
    adh_21_30 = ((removed_aberent_data['adh'] > 20) & (removed_aberent_data['adh'] <= 30))
    adh_31_40 = ((removed_aberent_data['adh'] > 30) & (removed_aberent_data['adh'] <= 40))
    adh_41_50 = ((removed_aberent_data['adh'] > 40) & (removed_aberent_data['adh'] <= 50))
    adh_51_60 = ((removed_aberent_data['adh'] > 50) & (removed_aberent_data['adh'] <= 60))
    adh_61_70 = ((removed_aberent_data['adh'] > 60) & (removed_aberent_data['adh'] <= 70))
    adh_71 = (removed_aberent_data['adh'] > 70)
    removed_aberent_data['CATadh'] = ''
    removed_aberent_data['CATadh'][adh_0_10] = '0_10'
    removed_aberent_data['CATadh'][adh_11_20] = '11_20'
    removed_aberent_data['CATadh'][adh_21_30] = '21_30'
    removed_aberent_data['CATadh'][adh_31_40] = '31_40'
    removed_aberent_data['CATadh'][adh_41_50] = '41_50'
    removed_aberent_data['CATadh'][adh_51_60] = '51_60'
    removed_aberent_data['CATadh'][adh_61_70] = '61_70'
    removed_aberent_data['CATadh'][adh_71] = '71plus'

    # agedem
    agedem_0_10 = (removed_aberent_data['agedem'] <=10)
    agedem_11_20 = ((removed_aberent_data['agedem'] > 10) & (removed_aberent_data['agedem'] <= 20))
    agedem_21_30 = ((removed_aberent_data['agedem'] > 20) & (removed_aberent_data['agedem'] <= 30))
    agedem_31_40 = ((removed_aberent_data['agedem'] > 30) & (removed_aberent_data['agedem'] <= 40))
    agedem_41_50 = ((removed_aberent_data['agedem'] > 40) & (removed_aberent_data['agedem'] <= 50))
    agedem_51_60 = ((removed_aberent_data['agedem'] > 50) & (removed_aberent_data['agedem'] <= 60))
    agedem_61_70 = ((removed_aberent_data['agedem'] > 60) & (removed_aberent_data['agedem'] <= 70))
    agedem_71 = (removed_aberent_data['agedem'] > 70)
    removed_aberent_data['CATagedem'] = ''
    removed_aberent_data['CATagedem'][agedem_0_10] = '0_10'
    removed_aberent_data['CATagedem'][agedem_11_20] = '11_20'
    removed_aberent_data['CATagedem'][agedem_21_30] = '21_30'
    removed_aberent_data['CATagedem'][agedem_31_40] = '31_40'
    removed_aberent_data['CATagedem'][agedem_41_50] = '41_50'
    removed_aberent_data['CATagedem'][agedem_51_60] = '51_60'
    removed_aberent_data['CATagedem'][agedem_61_70] = '61_70'
    removed_aberent_data['CATagedem'][agedem_71] = '71plus'

    ###
    # ajout de la classe is_adh = démissionnaire
    ###
    removed_aberent_data['is_adh'] = 'demissionnaire'



    print(removed_aberent_data)
    # exit()
    removed_aberent_data.to_csv('../donnees/cleaned/data_mining_DB_clients_tbl_cleaned.csv', sep=",", index=False)
    print("##############################")
    print("#####END CLEAN CLIENT TBL#####")
    print("##############################")

if __name__ == "__main__":
    clean_client_tbl()