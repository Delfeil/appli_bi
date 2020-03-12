#!/usr/bin/env python
# -*- coding: utf-8 -*-

def cah_cat():
    import pandas as pd
    import matplotlib.pyplot as plt
    print("####################################################")
    print("#####RUN CLASSIFICATION ASCENDENTE HIÉRARCHIQUE#####")
    print("####################################################")
    ###
    # Récupération des données
    ###
    clients = pd.read_csv('../donnees/fusion/dem.csv', sep=',')

    print(clients)

    classes = clients['is_adh']
    del clients['is_adh']

        # enlever les valeurs numériques
    del clients['DTADH']
    del clients['DTDEM']
    del clients['MTREV']
    del clients['AGEAD']
    del clients['adh']

    ## enlever les valeurs catégorielles innutiles
    # del clients['CDSEXE']
    # del clients['NBENF']
    # del clients['CATAGEAD']
    # del clients['CATadh']

    ##enlever les valeurs catégorieles utiles
    # del clients['CDSITFAM']
    # del clients['CDTMT']
    # del clients['CDCATCL']

    print(clients)

    # clients_reduced = clients.iloc[2500:]
    # del clients
    X_cat_one_hot = pd.get_dummies(clients.astype(str))
    print(X_cat_one_hot)
    # print(type(X_cat_one_hot.index.values), X_cat_one_hot.index.values.tolist())

    # hierarchical clustering
    from scipy.cluster.hierarchy import dendrogram, linkage

    # lst_labels = map(lambda pair: pair[0]+str(pair[1]), X_cat_one_hot.index.values.tolist())
    linkage_matrix = linkage(X_cat_one_hot, 'ward')
    fig = plt.figure()
    dendrogram(
        linkage_matrix,
        color_threshold=0,
        labels=X_cat_one_hot.index.values.tolist(),
    )
    plt.title('Hierarchical Clustering Dendrogram (Ward)')
    plt.xlabel('sample index')
    plt.ylabel('distance')
    plt.tight_layout()
    plt.savefig('../fig/hierarchical-clustering')
    plt.close()
    print("####################################################")
    print("#####RUN CLASSIFICATION ASCENDENTE HIÉRARCHIQUE#####")
    print("####################################################")

if __name__ == "__main__":
    cah_cat()