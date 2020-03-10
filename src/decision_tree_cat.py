#!/usr/bin/env python
# -*- coding: utf-8 -*-

def decision_tree_cat():
    print("###############################")
    print("#####RUN DECISION TREE NUM#####")
    print("###############################")
    import pandas as pd

    from sklearn import tree
    from sklearn.model_selection import cross_val_score

    ###
    # On récuoère les données catégoriques
    ###

    def cross_validation(lst_classif,lst_classif_names,X,y):
        for clf,name_clf in zip(lst_classif,lst_classif_names):
            # TODO : complete with function cross_val_score
            scores = cross_val_score(clf, X, y, cv=5, verbose=False)
            # print(pd.DataFrame(scores))
            print("Accuracy of "+name_clf+" classifier on cross-validation: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

    def discretize(data, feature_names):
        list_prefix = ['eqsized_bins_', 'eqintervaled_bins_']
        nb_bin = 10
        for prefix in list_prefix:
            print("###### Discretization with "+prefix+" ######")

            for attr in feature_names:
                if 'sized' in prefix:
                    data[prefix+attr]=pd.qcut(data[attr],nb_bin)
                else:
                    data[prefix+attr]=pd.cut(data[attr],nb_bin)
                # use pd.concat to join the new columns with your original dataframe
                data=pd.concat([data,pd.get_dummies(data[prefix+attr],prefix=prefix+attr)],axis=1)
                # now drop the original column (you don't need it anymore)
                data.drop(prefix+attr,axis=1, inplace=True)

            feature_names_bins = filter(lambda x: x.startswith(prefix) and x.endswith(']'), list(data))
            X_discret = data[feature_names_bins]
            print(X_discret.head())
            return X_discret

    clients_adh = pd.read_csv('../donnees/fusion/adh.csv', sep=',')
    clients_dem = pd.read_csv('../donnees/fusion/dem.csv', sep=',')

    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    # print(clients_adh)
    clients_adh_cat = clients_adh.select_dtypes(exclude=numerics)
    del clients_adh_cat['DTADH']
    clients_adh_cat['CDSEXE'] = clients_adh['CDSEXE']
    clients_adh_cat['CDTMT'] = clients_adh['CDTMT']
    clients_adh_cat['CDCATCL'] = clients_adh['CDCATCL']
    clients_adh_cat['is_adh'] = "adherent"
    print(clients_adh_cat)

    # print(clients_dem)
    clients_dem_cat = clients_dem.select_dtypes(exclude=numerics)
    del clients_dem_cat['CDMOTDEM']
    del clients_dem_cat['DTADH']
    del clients_dem_cat['DTDEM']
    clients_dem_cat['CDSEXE'] = clients_dem['CDSEXE']
    clients_dem_cat['CDTMT'] = clients_dem['CDTMT']
    clients_dem_cat['CDCATCL'] = clients_dem['CDCATCL']
    clients_dem_cat['is_adh'] = "demissionnaire"
    print(clients_dem_cat)

    fusion_clients_cat = pd.DataFrame(clients_adh_cat).append( pd.DataFrame(clients_dem_cat))
    print(fusion_clients_cat)

    from sklearn.utils import shuffle
    fusion_clients_cat = shuffle(fusion_clients_cat)

    ###
    # Arbre de décision
    ###
    # feature_names = ['NBENF', 'CDSITFAM', 'CDSEXE', 'CDTMT', 'CDCATCL']
    feature_names = ['CDSITFAM', 'CDTMT', 'CDCATCL', 'CATAGEAD', 'CATadh']
    X = fusion_clients_cat[feature_names]
    y = fusion_clients_cat['is_adh']

    # X_discret = discretize(X, feature_names)
    X_cat_one_hot = pd.get_dummies(X.astype(str))

    print("labor normalized")
    print(X)
    print(X_cat_one_hot)
    feature_names = list(X_cat_one_hot.columns)
    # print(list(X_cat_one_hot.columns))
    # exit()

    dectree = tree.DecisionTreeClassifier()


    lst_classif = [dectree]
    lst_classif_names = ['Decision tree']

    # cross_validation(lst_classif, lst_classif_names, X_norm, y)

    for clf,name_clf in zip(lst_classif,lst_classif_names):
        clf.fit(X_cat_one_hot, y)
        # TODO
        # y_pred = clf.predict(X_test)
        #
        # print('Accuracy of '+name_clf+' classifier on training set: {:.2f}'
        #       .format(clf.score(X, y)))
        # print('Accuracy of '+name_clf+' classifier on test set: {:.2f}'
        #  .format(clf.score(X_test, y_test)))
        # print(confusion_matrix(y_test, y_pred))

    import graphviz
    dot_data = tree.export_graphviz(dectree, out_file=None,
                                    feature_names=feature_names,
                                    class_names=fusion_clients_cat['is_adh'].unique(),
                                    filled=True, rounded=True,
                                    special_characters=True,
                                    max_depth=5)
    graph = graphviz.Source(dot_data)
    graph.render(directory='../fig',filename='decision_tree_cat')
    print("###############################")
    print("#####END DECISION TREE CAT#####")
    print("###############################")

if(__name__ == "__main__"):
    decision_tree_cat()