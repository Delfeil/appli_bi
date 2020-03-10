#!/usr/bin/env python
# -*- coding: utf-8 -*-



def linear_regression_cat():
    import pandas as pd
    from sklearn.model_selection import cross_val_score

    from sklearn.linear_model import LogisticRegression
    print("###################################")
    print("#####RUN LINEAR REGRESSION CAT#####")
    print("###################################")
    ###
    # Récupération des données
    ###
    clients = pd.read_csv('../donnees/fusion/dem_adh.csv', sep=',')

    print(clients)

    classes = clients['is_adh']
    del clients['is_adh']

        # enlever les valeurs numériques
    del clients['DTADH']
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

    X_cat_one_hot = pd.get_dummies(clients.astype(str))
    print(X_cat_one_hot)

    ###
    # Régression linéaire
    ###
    logreg = LogisticRegression()
    clf = logreg.fit(X_cat_one_hot, classes)
    print(clf.get_params(deep=False))

    print(clf.score(X_cat_one_hot, classes))
    coefs = clf.coef_
    # print(coefs)
    i =0
    for col in X_cat_one_hot:
        print(col, coefs[0, i])
        # coefs_df[col] = coefs[0][i]
        i = i+1

    print("###################################")
    print("#####END LINEAR REGRESSION CAT#####")
    print("###################################")

if __name__ == "__main__":
    linear_regression_cat()


#####
## Analyse des résultats
#####
## Coefficients
# CDSITFAM_D 1.118413161910858
# CDSITFAM_G -1.7219124840623572
# CDSITFAM_P -1.0247680033985953
# CDSITFAM_V 1.1398790234365668
# CDCATCL_10 -3.1456361841714835
# CDCATCL_21 2.4830131382896874
# CDCATCL_23 -1.4999566358532732
# CDCATCL_40 2.251789080143869
# CATAGEAD_0_10 -4.666788525651991
# CATAGEAD_11_20 -1.2014484706151616
# CATAGEAD_21_30 1.7016079529094594
# CATAGEAD_31_40 1.1640696997974922

