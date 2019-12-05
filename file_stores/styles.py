def labels(s):
    """
    Creat nice labels
    """
    labels = {
        'WT-S-H3K4me3_ChIP':            'ChIP, 3D7C8 H3K4me3 Late Stage',
        'LSD2KO-S-H3K4me3_ChIP':        'ChIp, LSD2KO H3K4me3 Late Stage',
        'WT-S-H3K4me3_Input':           'Input, 3D7C8 H3K4me3 Late Stage',
        'LSD2KO-S-H3K4me3_Input':       'Input, LSD2KO H3K4me3 Late Stage'
    }
    try:
        return labels[s]
    except KeyError:
        print 'no key for', s
        return s
    
    # Colors used for plotting
    colors = {
        'both':          '#cc0000',
        'suhw':          '#669900',
        'shep':          '#007acc',
        'input':         '#888888',
        'kc_suhw':       '#88cc00',
        #'kc_shep':       '#0066cc',
        'kc_shep':       '#2EAEEE',
        'bg3_suhw':      '#446600',
        'bg3_shep':      '#005c99',
        'kc_input':      '#888888',
        'bg3_input':     '#888888',
    }