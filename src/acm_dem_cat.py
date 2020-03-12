#!/usr/bin/env python
# -*- coding: utf-8 -*-
from R_square_clustering import r_square


def acp_dem_cat():
    import pandas as pd
    from fanalysis.mca import MCA
    print("############################################")
    print("#####RUN ACP DEMISSIONAIRES CATEGORIELS#####")
    print("############################################")
    clients_dem = pd.read_csv('../donnees/fusion/dem.csv', sep=',')
    print(clients_dem)

    del clients_dem['is_adh']
    del clients_dem['DTADH']
    del clients_dem['DTDEM']

    ## Remove numerics data
    del clients_dem['MTREV']
    del clients_dem['AGEAD']
    del clients_dem['agedem']
    del clients_dem['adh']



    print(clients_dem)

    X = clients_dem.to_numpy(dtype='str')
    print(X)
    mca = MCA(row_labels=clients_dem.index.values.astype('str'), var_labels=clients_dem.columns.values)
    mca.fit(X)

    print(mca.eig_)
    print(mca.col_labels_)

    interpretationTable = pd.DataFrame({'val_axe1': mca.col_coord_[:, 0],
                                        'contrib_axe1': mca.col_contrib_[:, 0],
                                        'cos2_axe1': mca.col_cos2_[:, 0],
                                        'val_axe2': mca.col_coord_[:, 1],
                                        'contrib_axe2': mca.col_contrib_[:, 1],
                                        'cos2_axe2': mca.col_cos2_[:, 1],
                                        'val_axe3': mca.col_coord_[:, 2],
                                        'contrib_axe3': mca.col_contrib_[:, 2],
                                        'cos2_axe3': mca.col_cos2_[:, 2]
                                        }, index=mca.col_labels_)

    mask_sup_5 = ((interpretationTable['cos2_axe1'] > 0.2) | (interpretationTable['cos2_axe2'] > 0.2))
    print("################")
    print("####Table des Contributions####")
    print("################")
    print(interpretationTable[mask_sup_5])
    print("################")
    print("################")

    mca.plot_eigenvalues()

    print(mca.row_labels)
    print(mca.col_labels_)

    print(mca.col_contrib_[:, 3])
    print(mca.col_cos2_)

    mca.plot_col_cos2(num_axis=1, short_labels=False, nb_values=5)
    mca.plot_col_cos2(num_axis=2, short_labels=False, nb_values=5)
    mca.plot_col_contrib(num_axis=1, short_labels=False, nb_values=5)
    mca.plot_col_contrib(num_axis=2, short_labels=False, nb_values=5)

    mca.mapping_col(num_x_axis=1, num_y_axis=2, short_labels=False)
    mca.mapping_row(num_x_axis=1, num_y_axis=2)


    print("############################################")
    print("#####END ACP DEMISSIONAIRES CATEGORIELS#####")
    print("############################################")

if __name__ == "__main__":
    acp_dem_cat()