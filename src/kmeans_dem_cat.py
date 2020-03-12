#!/usr/bin/env python
# -*- coding: utf-8 -*-
from R_square_clustering import r_square


def cah_cat():
    import pandas as pd
    import matplotlib.pyplot as plt
    from sklearn.cluster import KMeans
    print("###############################################")
    print("#####RUN KMEANS DEMISSIONAIRES CATEGORIELS#####")
    print("###############################################")
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

    X_cat_one_hot = pd.get_dummies(clients_dem.astype(str))
    print(X_cat_one_hot)

    ####
    ## kmeans
    ####

    # Compute R-square, i.e. V_inter/V

    # Plot elbow graphs for KMeans using R square and purity scores
    lst_k=range(2,8)
    lst_rsq = []
    lst_purity = []
    for k in lst_k:
        est=KMeans(n_clusters=k)
        est.fit(X_cat_one_hot)
        lst_rsq.append(r_square(X_cat_one_hot.to_numpy(), est.cluster_centers_,est.labels_,k))
        # TODO: complete lst_purity
        print("------------- Groupe de " + str(k) +  " clusters ---------")
        clusters = {"code": pd.DataFrame(clients_dem.index.values.tolist()), "cluster": est.labels_}
        print( pd.DataFrame(clusters))

    fig = plt.figure()
    plt.plot(lst_k, lst_rsq, 'bx-')
    # plt.plot(lst_k, lst_purity, 'rx-')
    plt.xlabel('k')
    plt.ylabel('RSQ/purity score')
    plt.title('The Elbow Method showing the optimal k')
    plt.savefig('../fig/k-means_elbow_method')
    plt.close()

    print("###############################################")
    print("#####END KMEANS DEMISSIONAIRES CATEGORIELS#####")
    print("###############################################")

if __name__ == "__main__":
    cah_cat()