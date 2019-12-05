import file_stores as fs

idDir = ''
chipDir = ''

IDs = ['']
Signal = [
    ('',''),
    ('',''),
    ('',''),
    ('','')
    ]

lables = ['']

CPU = 60
fragment_size = 300
stranded = True

#RNA-seq data
#control = fs.diff_data['WT_R-vs-LSD1KO_R']['WT_R_RPKM']

#Figure settings
ylim = [0.9,1.1]
Figure_font_size = 12
Figure_font_family = ''
Figure_Title = IDs[0]
Figure_y_name = 'Avarage reads Density'
Figure_x_name = ''
Figure_save_name = IDs[0]
