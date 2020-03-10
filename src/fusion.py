#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

def fusion_dem():
    print("########################")
    print("#####RUN FUSION DEM#####")
    print("########################")
    client_dem = pd.read_csv('../donnees/cleaned/data_mining_DB_clients_tbl_cleaned.csv', sep=',')
    client_dem_bis = pd.read_csv('../donnees/cleaned/data_mining_DB_clients_tbl_bis_dem_cleaned.csv', sep=',')


    del client_dem['Id']
    del client_dem_bis['Id']
    fusion_dem = pd.DataFrame(client_dem).append( pd.DataFrame(client_dem_bis))

    print(client_dem)
    print(client_dem_bis)
    print(fusion_dem)

    fusion_dem.to_csv('../donnees/fusion/dem.csv', sep=",", index=False)
    print("########################")
    print("#####END FUSION DEM#####")
    print("########################")

if(__name__ == "__main__"):
    fusion_dem()