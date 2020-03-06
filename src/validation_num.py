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


# Récupération des données

clients = pd.read_csv('../donnees/fusion/dem_adh.csv', sep=',')

print(clients)

classes = clients['is_adh']
del clients['is_adh']
print(classes)


###
# Récupératoin des données numériques
###
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

clinets_num = clients.select_dtypes(include=numerics)

del clinets_num['CDSEXE']
del clinets_num['CDTMT']
del clinets_num['CDCATCL']

print(clinets_num)

###
# Récupération des données catégorielles
###
clinets_cat = clients.select_dtypes(exclude=numerics)

clinets_cat['CDSEXE'] = clients['CDSEXE']
clinets_cat['CDTMT'] = clients['CDTMT']
clinets_cat['CDCATCL'] = clients['CDCATCL']

print(clinets_cat)



####
# Test des classifications
####
from sklearn.dummy import DummyClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

dummycl = DummyClassifier(strategy="most_frequent")
gmb = GaussianNB()
dectree = DecisionTreeClassifier()
logreg = LogisticRegression()
svc = SVC()

lst_classif = [dummycl, gmb, dectree, logreg, svc]
lst_classif_names = ['Dummy most_frequent', 'Naive Bayes', 'Decision tree', 'Logistic regression', "SVC"]


###
# Normalisation des données numériques
###
from sklearn.preprocessing import StandardScaler

standard_scaler = StandardScaler()
X_num = pd.DataFrame(standard_scaler.fit_transform(clinets_num))
print("labor normalized")
print(X_num)

###
# Cross_validation sur les données numériques
###
print("----------Cross_validation: labor_num------------")
cross_validation(lst_classif, lst_classif_names, clinets_num, classes)

###
#
###
X_cat = []