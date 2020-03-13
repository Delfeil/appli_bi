#!/usr/bin/env python
# -*- coding: utf-8 -*-

def decision_tree_num():
    print("###############################")
    print("#####RUN DECISION TREE NUM#####")
    print("###############################")
    import pandas as pd

    from sklearn import tree
    from sklearn.model_selection import cross_val_score

    ###
    # On récuoère les données numériques
    ###

    def cross_validation(lst_classif,lst_classif_names,X,y):
        for clf,name_clf in zip(lst_classif,lst_classif_names):
            # TODO : complete with function cross_val_score
            scores = cross_val_score(clf, X, y, cv=5, verbose=False)
            # print(pd.DataFrame(scores))
            print("Accuracy of "+name_clf+" classifier on cross-validation: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

    clients_adh = pd.read_csv('../donnees/fusion/adh.csv', sep=',')
    clients_dem = pd.read_csv('../donnees/fusion/dem.csv', sep=',')

    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

    clients_adh_num = clients_adh.select_dtypes(include=numerics)
    # del clients_adh_num['DTADH']
    del clients_adh_num['Id']
    del clients_adh_num['CDSEXE']
    del clients_adh_num['CDTMT']
    del clients_adh_num['CDCATCL']
    clients_adh_num['is_adh'] = "adherent"
    clients_adh_num = clients_adh_num.rename(columns={"ageactu": 'agedem'})
    print(clients_adh_num)


    clients_dem_num = clients_dem.select_dtypes(include=numerics)
    # del clients_dem_num['DTDEM']
    # del clients_dem_num['DTADH']
    del clients_dem_num['CDSEXE']
    del clients_dem_num['CDTMT']
    del clients_dem_num['CDCATCL']
    clients_dem_num['is_adh'] = "demissionnaire"
    print(clients_dem_num)

    fusion_clients_num = pd.DataFrame(clients_adh_num).append( pd.DataFrame(clients_dem_num))
    print(fusion_clients_num)

    from sklearn.utils import shuffle
    fusion_clients_num = shuffle(fusion_clients_num)

    ###
    # Arbre de décision
    ###
    # feature_names = ['MTREV', 'NBENF', 'AGEAD', 'agedem']
    # feature_names = ['MTREV', 'AGEAD', 'agedem']
    feature_names = ['AGEAD', 'adh']
    # feature_names = ['NBENF', 'AGEAD', 'agedem']
    X = fusion_clients_num[feature_names]
    y = fusion_clients_num['is_adh']

    # from sklearn.preprocessing import StandardScaler
    # standard_scaler = StandardScaler()
    # X_norm = pd.DataFrame(standard_scaler.fit_transform(X))
    # print(X_norm)

    print("normalized")
    print(X)

    dectree = tree.DecisionTreeClassifier()


    lst_classif = [dectree]
    lst_classif_names = ['Decision tree']

    # cross_validation(lst_classif, lst_classif_names, X_norm, y)

    for clf,name_clf in zip(lst_classif,lst_classif_names):
        clf.fit(X, y)
        # TODO
        # y_pred = clf.predict(X_test)
        #
        print('Accuracy of '+name_clf+' classifier on training set: {:.2f}'
              .format(clf.score(X, y)))
        # print('Accuracy of '+name_clf+' classifier on test set: {:.2f}'
        #  .format(clf.score(X_test, y_test)))
        # print(confusion_matrix(y_test, y_pred))

    import graphviz
    dot_data = tree.export_graphviz(dectree, out_file=None,
                                    feature_names=feature_names,
                                    class_names=fusion_clients_num['is_adh'].unique(),
                                    filled=True, rounded=True,
                                    special_characters=True, max_depth=5)
    graph = graphviz.Source(dot_data)
    graph.render(directory='../fig',filename='decision_tree_num')
    print("###############################")
    print("#####END DECISION TREE NUM#####")
    print("###############################")

if(__name__ == "__main__"):
    decision_tree_num()