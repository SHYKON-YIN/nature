import yaml
import os
import inspect
import logging

def whoami(offset=0):
    """
    Returns the filename where this function was called.

    Increase `offset` to move up the stack.
    """
    return os.path.splitext(inspect.stack()[1 + offset][1])[0]


def write_readme(text):
    """
    Writes the module-level docstring to a README.txt file in the figure
    directory for the calling script.
    """
    caller = whoami(offset=1)
    figdir = figure_dir(caller=caller)
    fout = open(os.path.join(figdir, 'README.txt'), 'w')
    fout.write(text)
    fout.close()


def get_logger():
    """
    Return a logger named for the calling script with nice formatting
    """
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(name)s] [%(asctime)s]: %(message)s')
    caller = whoami(offset=1)
    name = os.path.basename(caller)
    logger = logging.getLogger(name)
    return logger


def figure_dir(caller=None):
    """
    Return a figure dir named for the calling script, creating it if necessary
    """
    if caller is None:
        caller = whoami(offset=1)
    fig_dir = os.path.join(
        os.path.dirname(caller),
        'figures',
        os.path.basename(caller))
    if not os.path.exists(fig_dir):
        os.makedirs(fig_dir)
    return fig_dir


def make_data_dir(topdir, fn):
    """
    data dir for script.

    data_dir('intermediate_data', __file__)
    """
    d = os.path.join(topdir,
                     os.path.splitext(
                         os.path.basename(fn))[0])
    if not os.path.exists(d):
        os.makedirs(d)
    return d
