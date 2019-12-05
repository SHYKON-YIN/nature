"""
Make file types for other modules
"""
import os
import logging
import numpy as np
import pandas
import pybedtools
import gffutils
import metaseq
import data_store
from metaseq.results_table import ResultsTable
import helpers
import sys
sys.path.append("..")
import configure as conf


logger = helpers.get_logger()

# Creat annotation database, if there is a TEMP directory specified in data_store, then 
# copy the db there for much faster query performance
if os.path.exists(data_store.TEMP):
    cached = os.path.join(data_store.TEMP, os.path.basename(data_store.dbfn))
    if not os.path.exists(cached):
        cmds = ['cp', data_store.dbfn, data_store.TEMP]
        logger.info(' '.join(cmds))
        os.system(' '.join(cmds))
    else:
        logger.info('Using database %s' % cached)
else:
    cached = data_store.db_fn
    logger.info('Using database %s' % cached)
db = gffutils.FeatureDB(cached)


def signalfy(d, kind):
    new_d = {}
    for k, v in d.items():
        new_d[k] = metaseq.genomic_signal(v, kind)
    return new_d
ip_bams = signalfy(data_store.ip_bam_filenames, 'bam')


"""
def chiPeaks(d):
    new_d = {}
    for k, v in d.items():
        new_d[k] = pybedtools.BedTool(v)
    return new_d
chip_peaks = chiPeaks(data_store.bed_filenames)
"""

# RNA-seq diff files
"""
def deseq(d):
    new_d = {}
    for k, v in d.items():
        new_d[k] = ResultsTable(v, import_kwargs = dict(index_col = 0))
    return new_d
diff_data = deseq(data_store.diff_filenames)
"""
