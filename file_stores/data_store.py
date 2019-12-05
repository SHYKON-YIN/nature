"""
This module simply sets up paths to data files for use by other module. 

Usefule attributes in this modules:
    * diff_filenames: dictionary of filename of RNA-seq results

    * bam_filenames: dictionary of BAM files for ChIP-seq data

    * bigwig_filenames: dictionay of bigwig files for ChIP-seq data

    * bed_filenames: dictionay of BED files for ChIP-seq data

    * dbfn: gffutils database filenames
    * GFF: filenames of the GFF file used for annotation

"""
import os
import configure as conf

#Absolute path to the directory where this data_store.py file lives.
HERE = os.path.abspath(os.path.dirname(__file__))

# Path to RNA-seq data files
def diff_fn(label):
    """
    Given a label of the form "celltype1(control)-vs-celltype2(experiment)", retuern the path to the RNA-seq data
    """
    celltype1, celltype2 = label.split('-vs-')
    return os.path.join(HERE, '..', 'rnaseq-analysis', celltype2, label + '.gfold_rpkm.diff')

# Creat the RNA-seq data path dictionary
diff_filenames = {
    'WT_S-vs-LSD2KO_S': diff_fn('WT_S-vs-LSD2KO_S'),
    'WT_S-vs-LSD1KO_S': diff_fn('WT_S-vs-LSD1KO_S'),
    'WT_T-vs-LSD1KO_T': diff_fn('WT_T-vs-LSD1KO_T'),
    'WT_T-vs-LSD2KO_T': diff_fn('WT_T-vs-LSD2KO_T'),
    'WT_R-vs-LSD1KO_R': diff_fn('WT_R-vs-LSD1KO_R'),
    'WT_R-vs-LSD2KO_R': diff_fn('WT_R-vs-LSD2KO_R')
}

# Path to ChIP-seq data
chipseq_dir = os.path.join(HERE, '..', 'chipseq-analysis')

def chip_ext(x, ext):
    """
    Return the file path for extension 'ext'
    """
    return os.path.join(chipseq_dir, conf.chipDir, x + ext)
def to_input(x):
    """
    Convert 'cell_ChIP' to 'cell_Input'
    """
    return '_'.join([x.split('_')[0], 'Input'])

# BAM file extension
bam_ext = '.bam'
bed_ext = '.bed'
txt_ext = '.txt'
#bigwig_ext = '.bw'

# File labels
LABELS = [y for x in conf.Signal for y in x]

bam_filenames = dict((i, chip_ext(i, bam_ext)) for i in LABELS)
#bw_filenames = dict((i, chip_ext(i, bigwig_ext)) for i in LABELS)
ip_bam_filenames = bam_filenames
#ip_bw_filenames = bw_filenames

"""
def peak_ext(x, ext):
    
    #Return a given label 'x' of the "cell_ChIP", return the peaks for a given extension.

    return os.path.join(chipseq_dir, 'ZQF/Bed', x + ext)

LABELS_no_Input = [i for i in LABELS if 'Input' not in i]

bed_filenames = dict((i, peak_ext(i, bed_ext)) for i in LABELS_no_Input)
"""

id_list = os.path.join(HERE, '..', 'rnaseq-analysis', 'GFF/mm', 'gene_ids.txt')
db_fn = os.path.join(HERE, '..', 'rnaseq-analysis', 'GFF/mm', 'Mus_musculus.GRCm38.90.gtf.db')
gnomeSize = os.path.join(HERE, '..', 'rnaseq-analysis', 'GFF/mm', 'genome.size')
GFF = db_fn.replace('.db', '')

############################################################
# This part is define the gene ID to use for specific use  #
############################################################

id_file_labels = conf.IDs

def id_ext(x, ext):
    """
    Return the file path for extension 'ext'
    """
    return os.path.join(chipseq_dir, conf.idDir, x + ext)

id_file_name = dict((i, id_ext(i, txt_ext)) for i in id_file_labels)


TEMP = '/scratch'
