#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from fanalysis.ca import CA

clients_adh = pd.read_csv('../donnees/fusion/adh.csv', sep=',')
clients_dem = pd.read_csv('../donnees/fusion/dem.csv', sep=',')

numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
# print(clients_adh)
clients_adh_cat = clients_adh.select_dtypes(exclude=numerics)
del clients_adh_cat['DTADH']
# del clients_adh_cat['is_adh']
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
# del clients_dem_cat['is_adh']
del clients_dem_cat['CATagedem']
clients_dem_cat['CDSEXE'] = clients_dem['CDSEXE']
clients_dem_cat['CDTMT'] = clients_dem['CDTMT']
clients_dem_cat['CDCATCL'] = clients_dem['CDCATCL']
print(clients_dem_cat)

categories = []

for col_cat in clients_dem_cat:
    if(col_cat == 'is_adh'):
        continue
    # print(col_cat)
    cats = col_cat + '-' + clients_dem_cat[col_cat].apply(str).unique()
    # print(cats)
    categories.extend(cats.tolist())

print(categories)

afc_dataframe = pd.DataFrame({})

for cat in categories:
    cat_info = cat.split('-')
    row_name = cat_info[0]
    row_value = cat_info[1]
    # print(row_name, row_value)
    row_adh = clients_adh_cat[(clients_adh_cat[row_name].astype('str') == row_value)]
    row_dem = clients_dem_cat[(clients_dem_cat[row_name].astype('str') == row_value)]
    # print(row_adh, len(row_adh))
    # print(row_dem, len(row_dem))
    row = [
        len(row_adh),
        len(row_dem)
    ]
    afc_dataframe[cat] = row
afc_dataframe = afc_dataframe.rename(index={
    0: "adherent",
    1: 'demissionnaire'
})

print(afc_dataframe)

# X = afc_dataframe.to_numpy(dtype='str')
X = afc_dataframe.to_numpy()
print(X)

# exit()
# clients_dem_adh_cat = pd.DataFrame(clients_adh_cat).append( pd.DataFrame(clients_dem_cat))
# print(clients_dem_adh_cat)

my_ca = CA(row_labels=afc_dataframe.index.values, col_labels=afc_dataframe.columns.values)


###
# Créer un Tableau compatible avec l'AFC
###
#               | NBEND_0 | NBEND1+ | CDSITFAM_M | CDSITFAM_A...
# demissionaire |
# --------------|-----------------------
# adhérent      |

my_ca.fit(X)
print(my_ca.eig_)
my_ca.plot_eigenvalues()

df_rows = my_ca.row_topandas()
df_cols = my_ca.col_topandas()

print(df_cols)
print(df_rows)

my_ca.mapping(num_x_axis=1, num_y_axis=1)

# print(my_ca.row_topandas())


 ######
 ### Analyse
 ######

 ###
 # Axe 1
 ###
# | Variable       | Axe 1     | Contribution | Cos² |
# |----------------|-----------|--------------|------|
# | CDTMT-0        | 0.344449  | 7.360246     | 1.0  |
# | CDTMT-2        | -1.152083 | 24.584209    | 1.0  |
# | CDCATCL-21     | 0.524974  | 15.616062    | 1.0  |
# | CDCATCL-10     | -1.382079 | 38.814501    | 1.0  |

# | NBENF-enfants  | -0.455895 | 2.623237     | 1.0  | Les utiliser?
# | CDSITFAM-A     | 0.286592  | 3.022574     | 1.0  | Les utiliser?

# |----------------|-----------|--------------|------|
# | demissionnaire | 0.283797  | 31.238268    | 1.0  |
# | adherent       | -0.624694 | 68.761732    | 1.0  |

# CDTMT = 0 est corrélé positivement avec l'axe 1
# CDCATCL = 21 est corrélé positivement avec l'axe 1
# CDTMT = 2 est corrélé négativement avec l'axe 1
# CDCATCL = 10 est corrélé négativement avec l'axe 1
# ----------------------------------------------------
# is_adh = adherent est corrélé négativement avec l'axe 1
# is_adh = demissionnaire est corrélé négativement avec l'axe 1

# On observe un sur-effectif d'adhérents avec la variable CDTMT = 2
# On observe un sur-effectif d'adhérents avec la variable CDCATCL = 10
# On observe un sous-effectif d'adhérents avec la variable CDTMT = 0
# On observe un sous-effectif d'adhérents avec la variable CDCATCL = 21
# ------------------------------------------------------------------------
# On observe un sur-effectif de demissionnaires avec la variable CDTMT = 0
# On observe un sur-effectif de demissionnaires avec la variable CDCATCL = 21
# On observe un sous-effectif de demissionnaires avec la variable CDTMT = 2
# On observe un sous-effectif de demissionnaires avec la variable CDCATCL = 10


# Ainsi on remarque que les adhérents ont tendance à avoir la variable CDTMT = 2 et CDCATCL = 10,
# Tandis que les démissionaires ont la variable CDTMT = 0 et CDCATCL = 21.