#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from sklearn.model_selection import cross_val_score

def cross_validation(lst_classif,lst_classif_names,X,y):
    for clf,name_clf in zip(lst_classif,lst_classif_names):
        # TODO : complete with function cross_val_score
        scores = cross_val_score(clf, X, y, cv=5, verbose=False)
        # print(pd.DataFrame(scores))
        print("Accuracy of "+name_clf+" classifier on cross-validation: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

def validation_cat():
    print("##################################")
    print("#####RUN CROSS VALIDATION CAT#####")
    print("##################################")
    # Récupération des données

    clients = pd.read_csv('../donnees/fusion/dem_adh.csv', sep=',')

    print(clients)

    classes = clients['is_adh']
    del clients['is_adh']
    print(classes)


    ###
    # Récupération des données catégorielles
    ###
    # MTREV  AGEAD  adh
    # DTADH
        # enlever les valeurs numériques et innutiles
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

    # exit()

    ####
    # Test des classifications
    ####
    from sklearn.dummy import DummyClassifier
    from sklearn.naive_bayes import GaussianNB
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.linear_model import LogisticRegression

    dummycl = DummyClassifier(strategy="most_frequent")
    gmb = GaussianNB()
    dectree = DecisionTreeClassifier()
    logreg = LogisticRegression()

    lst_classif = [dummycl, gmb, dectree, logreg]
    lst_classif_names = ['Dummy most_frequent', 'Naive Bayes', 'Decision tree', 'Logistic regression']


    ###
    #
    ###

    X_cat_one_hot = pd.get_dummies(clients.astype(str))
    print(X_cat_one_hot)

    print("----------Cross_validation: labor_cat------------")
    cross_validation(lst_classif, lst_classif_names, X_cat_one_hot, classes)
    print("##################################")
    print("#####END CROSS VALIDATION CAT#####")
    print("##################################")

if __name__ == "__main__":
    validation_cat()