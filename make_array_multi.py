 # coding: utf-8
import os
import numpy as np
from features_multi import features
from metaseq import persistence
import file_stores as fs
import configure as conf 

logger = fs.get_logger()
figdir = fs.figure_dir()
IDs = conf.IDs
CPU = conf.CPU

print os.path.abspath(figdir)

def filter_array(array):
    return np.array([list(reversed(x)) for x in array])

def make_arrays(labels):
    #this is stored and returned the mapped arrays 
    arrays = {}
    # judge whether input parameter is a string or unicode
    if isinstance(labels, basestring):
        labels = [labels]
    for id in IDs:
    #keys into the 'features' dic, and bins number
        blocks = [
        (id + '_' + 'upstream_gene_2kb', 200),
        (id + '_' + 'full_genes', 300),
        (id + '_' + 'downstream_gene_2kb', 200)
        ]

        for label in labels:
            #get the bam files
            gs = fs.ip_bams[label]

            #Only do the time-consuming part if the file does not exist.
            prefix = os.path.join(figdir, id + '_' + label)
            if not os.path.exists(prefix + '.npz'):
                array_dict = {}
                for features_label, bins in blocks:
                    features_file = features[features_label]
                    logger.info('Generating array for %s, %s' % (label, features_label))
                   
                    kwargs = dict(
                        features = features_file,
                        processes = CPU,
                        bins = bins,
                        stranded = True,
			fragment_size = conf.fragment_size
                    )
                    
                    arr = gs.array(**kwargs) / (gs.mapped_read_count() / 1e6)
                    array_dict[features_label] = arr
                logger.info('saving to %s' % prefix)
                persistence.save_features_and_arrays(
                    features = features[id + '_' + 'full_genes'],
                    arrays = array_dict,
                    prefix = prefix,
                    link_features = True,
                    overwrite = True
                    )
                del array_dict
            logger.info('loading %s' % prefix)
            arrays[id + '_' + label] = persistence.load_features_and_arrays(prefix)
    return arrays



