#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from fanalysis.mca import MCA

clients_adh = pd.read_csv('../donnees/fusion/adh.csv', sep=',')
clients_dem = pd.read_csv('../donnees/fusion/dem.csv', sep=',')

numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
# print(clients_adh)
clients_adh_cat = clients_adh.select_dtypes(exclude=numerics)
del clients_adh_cat['DTADH']
del clients_adh_cat['is_adh']
del clients_adh_cat['CATageactu']
clients_adh_cat['CDSEXE'] = clients_adh['CDSEXE']
clients_adh_cat['CDTMT'] = clients_adh['CDTMT']
clients_adh_cat['CDCATCL'] = clients_adh['CDCATCL']
print(clients_adh_cat)

# print(clients_dem)
clients_dem_cat = clients_dem.select_dtypes(exclude=numerics)
del clients_dem_cat['CDMOTDEM']
del clients_dem_cat['DTADH']
del clients_dem_cat['DTDEM']
del clients_dem_cat['is_adh']
del clients_dem_cat['CATagedem']
clients_dem_cat['CDSEXE'] = clients_dem['CDSEXE']
clients_dem_cat['CDTMT'] = clients_dem['CDTMT']
clients_dem_cat['CDCATCL'] = clients_dem['CDCATCL']
print(clients_dem_cat)

clients_dem_adh_cat = pd.DataFrame(clients_adh_cat).append( pd.DataFrame(clients_dem_cat))
print(clients_dem_adh_cat)
X = clients_dem_adh_cat.to_numpy(dtype='str')
print(X)
print(clients_dem_adh_cat.columns.values)
mca = MCA(row_labels=clients_dem_adh_cat.index.values.astype('str'), var_labels=clients_dem_adh_cat.columns.values, n_components=4)

mca.fit(X)
print(mca.eig_)
print(mca.col_labels_)

interpretationTable = pd.DataFrame({'val_axe1': mca.col_coord_[:, 0],
                                    'contrib_axe1': mca.col_contrib_[:, 0],
                                    'cos2_axe1': mca.col_cos2_[:, 0],
                                    'val_axe2': mca.col_coord_[:, 1],
                                    'contrib_axe2': mca.col_contrib_[:, 1],
                                    'cos2_axe2': mca.col_cos2_[:, 1],
                                    # 'val_axe3': mca.col_coord_[:, 2],
                                    # 'contrib_axe3': mca.col_contrib_[:, 2],
                                    # 'cos2_axe3': mca.col_cos2_[:, 2]
                                    }, index=mca.col_labels_)

mask_sup_5 = ((interpretationTable['cos2_axe1'] > 0.2) | (interpretationTable['cos2_axe2'] > 0.2))
print(interpretationTable[mask_sup_5])

#######
## Analyse des corrélations:
#######
###
# Axe 1
###
# | Variable   | Axe 1     | Contribution | Cos²     |
# |------------|-----------|--------------|----------|
# | CDTMT_0    | -0.442087 | 6.712632     | 0.653512 |
# | CDTMT_2    | 1.478252  | 22.408965    | 0.652125 |
# | CDCATCL_10 | 1.299346  | 18.993881    | 0.569235 |

# CDTMT = 0 Est corrélé nagativement avec l'axe 1
# CDTMT = 2 Est corrélé positivement avec l'axe 1
# CDCATCL = 10 est corrélé positivement avec l'axe 1

###
# Axe 2
###
# | Variable   | Axe 1    | Contribution | Cos²     |
# |------------|----------|--------------|----------|
# | CDSITFAM_C | 1.875497 | 25.311278    | 0.563016 |
# | CDSEXE_4   | 2.047329 | 27.318874    | 0.598641 |

# CDSITFAM = C est corrélé positivement avec l'axe 2
# CDSEXE = 4 est corrélé positivement avec l'axe 2

# mca.plot_eigenvalues()




# print(mca.row_labels)
# print(mca.col_labels_)

# print(mca.col_contrib_[:, 3])
# print(mca.col_cos2_)

# mca.plot_col_cos2(num_axis=1, short_labels=False, nb_values=5)
# mca.plot_col_cos2(num_axis=2, short_labels=False, nb_values=5)
# mca.plot_col_contrib(num_axis=1, short_labels=False, nb_values=5)
# mca.plot_col_contrib(num_axis=2, short_labels=False, nb_values=5)

mca.mapping_col(num_x_axis=1, num_y_axis=2, short_labels=False)
# mca.mapping_row(num_x_axis=1, num_y_axis=2)