#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

remove_vals = True
to_shuffle = True

clients_adh = pd.read_csv('../donnees/fusion/adh.csv', sep=',')
clients_dem = pd.read_csv('../donnees/fusion/dem.csv', sep=',')

del clients_adh['Id']
if remove_vals:
    del clients_adh['ageactu']
    del clients_adh['CATageactu']
    del clients_dem['CATagedem']
    del clients_dem['agedem']
else:
    clients_adh = clients_adh.rename(columns={"ageactu": 'agedem'})
    clients_adh = clients_adh.rename(columns={"CATageactu": 'CATagedem'})

print(clients_adh)

del clients_dem['DTDEM']
del clients_dem['CDMOTDEM']
print(clients_dem)

fusion_clients = pd.DataFrame(clients_dem).append( pd.DataFrame(clients_adh))

if to_shuffle:
    from sklearn.utils import shuffle
    fusion_clients = shuffle(fusion_clients)
print(fusion_clients)

fusion_clients.to_csv('../donnees/fusion/dem_adh.csv', sep=",", index=False)