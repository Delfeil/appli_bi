#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

def discretize_histogram(data, col, data_origine):
    print(data)
    print(col)
    fig = plt.figure()
    plt.subplot(211)
    matplotlib.pyplot.xticks(fontsize=6)
    pd.cut(data[col],10).value_counts(sort=False).plot.bar()
    plt.xticks(rotation=25)
    # discretize with equal-sized bins
    plt.subplot(212)
    matplotlib.pyplot.xticks(fontsize=6)
    # TODO: plot with qcut
    pd.qcut(data[col],10, duplicates='drop').value_counts(sort=False).plot.bar()
    plt.xticks(rotation=25)
    plt.suptitle('Histogram for '+col+' discretized with equal-intervaled and equal-sized bins ' + data_origine)
    plt.savefig('../fig/'+col+'_histogram_discretization_'+ data_origine)
    plt.close(fig)

def histogram_cat(data, col, data_origine):
    fig = plt.figure()
    data[col].value_counts().plot(kind='bar')
    plt.suptitle('Histogram for '+col + ' ' + data_origine)
    plt.savefig('../fig/data_histogram_'+col + '_' + data_origine)
    plt.close(fig)