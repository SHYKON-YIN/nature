import matplotlib
matplotlib.use('Agg')
import file_stores as fs
import os
from metaseq import plotutils, colormap_adjust
import pandas
import numpy as np
from make_array_multi import make_arrays
from scipy.stats import scoreatpercentile
from features_multi import features
from matplotlib import pyplot as plt
import configure as conf 

import random

figdir = fs.figure_dir()
logger = fs.get_logger()

#To avoid 0 in divition

def add1(array):
    return array + 1

#set varies used in ploting
IDs = conf.IDs
signals_label = conf.Signal
y_name = conf.Figure_y_name
title = conf.Figure_Title
figure_save_name = conf.Figure_save_name
plt.rcParams['font.size'] = conf.Figure_font_size
plt.rcParams['font.family'] = 'Times New Roman'


file_dic = {}
for ip_label, input_label in signals_label:
    arrays = make_arrays([ip_label, input_label])
    logger.info('Concatenating %s arrays' % ip_label)

    def get_arrays_stack(id, ip_label_copy = ip_label, input_label_copy = input_label):
        blocks = [
            id + '_' + 'upstream_gene_2kb',
            id + '_' + 'full_genes',
            id + '_' + 'downstream_gene_2kb'
        ]
        array = [
            np.column_stack([arrays[id + '_' + ip_label_copy][1][i] for i in blocks]),
            np.column_stack([arrays[id + '_' + input_label_copy][1][i] for i in blocks])]
        return array
    for i,j in enumerate(IDs):
        file_dic[ip_label + IDs[i]] = get_arrays_stack(IDs[i])[0]
        file_dic[input_label + IDs[i]] = get_arrays_stack(IDs[i])[1]

#### ChIP / Input [Input replaced 0 as mean]
arr_1 = add1(file_dic[signals_label[0][0] + IDs[0]]) / add1(file_dic[signals_label[0][1] + IDs[0]])
arr_2 = add1(file_dic[signals_label[1][0] + IDs[0]]) / add1(file_dic[signals_label[1][1] + IDs[0]])
arr_3 = add1(file_dic[signals_label[2][0] + IDs[0]]) / add1(file_dic[signals_label[2][1] + IDs[0]])
arr_4 = add1(file_dic[signals_label[3][0] + IDs[0]]) / add1(file_dic[signals_label[3][1] + IDs[0]])
#arr_5 = add1(file_dic[signals_label[1][0] + IDs[1]]) / add1(file_dic[signals_label[1][1] + IDs[1]])
#arr_6 = add1(file_dic[signals_label[1][0] + IDs[2]]) / add1(file_dic[signals_label[1][1] + IDs[2]])

"""
### Only use ChIP
arr_1 = add1(file_dic[signals_label[0][0] + IDs[0]])
arr_2 = add1(file_dic[signals_label[1][0] + IDs[0]])
arr_3 = add1(file_dic[signals_label[2][0] + IDs[0]])
#arr_4 = file_dic[signals_label[3][0] + IDs[0]]
"""


"""
### Use ChIP - Input
arr_1 = file_dic[signals_label[0][0] + IDs[0]] - file_dic[signals_label[0][1] + IDs[0]]
arr_2 = file_dic[signals_label[1][0] + IDs[0]] - file_dic[signals_label[1][1] + IDs[0]]
arr_3 = file_dic[signals_label[2][0] + IDs[0]] - file_dic[signals_label[2][1] + IDs[0]]
arr_4 = file_dic[signals_label[3][0] + IDs[0]] - file_dic[signals_label[3][1] + IDs[0]]
"""

fig = plt.figure()
ax = fig.add_subplot(111)
x = np.linspace(0, 700, 700)


#plot the IP and Input signal
ax.plot(x, arr_1.mean(axis = 0), color = 'r',label = conf.lables[0], ls='-',alpha=1, lw=3)
ax.plot(x, arr_2.mean(axis = 0), color = 'b',label = conf.lables[1], ls='-',alpha=1, lw=3)
ax.plot(x, arr_3.mean(axis = 0), color = 'g',label = conf.lables[2], ls='-',alpha=1, lw=3)
ax.plot(x, arr_4.mean(axis = 0), color = 'y',label = conf.lables[3], ls='-',alpha=1, lw=3)
#ax.plot(x, arr_5.mean(axis = 0), color = 'b',label = conf.lables[1] + '-jian', ls='-.',alpha=1, lw=3)
#ax.plot(x, arr_6.mean(axis = 0), color = 'g',label = conf.lables[2] + '-jian', ls='-.',alpha=1, lw=3)



border_style = dict(color='k', linestyle=":")

ticks, ticklabels, alignment = zip(*[
    (0, '-2kb', 'right'),
    (200, 'TSS', 'center'),
    (350, 'gene body', 'center'),
    (500, 'TTS', 'center'),
    (700, '+2kb', 'left'),
    ])

ax.set_title(title)
ax.set_ylabel(y_name)
ax.axvline(200, **border_style)
ax.axvline(500, **border_style)
ax.set_xticklabels([])
ax.set_xticks(ticks)
ax.set_xticklabels(ticklabels)
ax.legend(loc='best', fontsize = 'x-small')
filename = os.path.join(figdir, figure_save_name + '.pdf')
    
#plt.ylim(conf.ylim[0],conf.ylim[1])
fig.savefig(filename, dpi=300, format='pdf')
logger.info('saved %s' % filename)
