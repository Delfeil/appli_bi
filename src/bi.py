#!/usr/bin/env python
# -*- coding: utf-8 -*-

from clean_data_mining_DB_clients_tbl import clean_client_tbl
from clean_data_mining_DB_clients_tbl_bis import clean_client_tbl_bis

from fusion import fusion_dem
from fusion_in_one_file import fusion_in_one_file

from metrics_tabs import metrics_tabs
from metrics_tabs_bis import metrics_tabs_bis
from metrics_cleaned_adh import metrics_cleaned_adh
from metrics_cleaned_dem import metrics_cleaned_dem

from decision_tree_num import decision_tree_num
from decision_tree_cat import decision_tree_cat
from decision_tree_cat_num import decision_tree_cat_num

from linear_regression_cat import linear_regression_cat

from acm import analyse_acm
from afc import analyse_afc

from validation_cat import validation_cat
from validation_cat_treevars import validation_cat_treevars
from validation_cat_lesstreevars import validation_cat_lesstreevars
from validation_num import validation_num

from acm_dem_cat import acp_dem_cat
from cah_dem_cat import cah_cat

metrics_tabs()
metrics_tabs_bis()

clean_client_tbl()
clean_client_tbl_bis()


fusion_dem()
fusion_in_one_file()


metrics_cleaned_adh("test_adh")
metrics_cleaned_dem("test_dem")


decision_tree_num()
decision_tree_cat()
decision_tree_cat_num()

linear_regression_cat()

analyse_acm()
analyse_afc()


validation_num()
validation_cat()
validation_cat_treevars()
validation_cat_lesstreevars()

acp_dem_cat()
cah_cat()
