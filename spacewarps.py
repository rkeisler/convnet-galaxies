import numpy as np
import ipdb


def make_stage1_train_and_val_listfiles(frac_val=0.2):
    #from glob import glob
    #filenames = glob('data/cutouts_good/*.png')
    #np.random.shuffle(filenames)
    df = load_labels()
    df_not = df[(df.stage==1) & ( (df.truth=='NOT') | ((df.truth=='LENS')&(df.alpha==0)) )]
    df_lens = df[(df.stage==1) & ((df.truth=='LENS')&(df.alpha==1))]
    filenames_not = df_not.cutoutname.values
    filenames_lens = df_lens.cutoutname.values
    filenames = np.concatenate([filenames_not, filenames_lens])
    labels = np.concatenate([np.zeros(len(filenames_not)), np.ones(len(filenames_lens))])
    ind = np.arange(len(filenames))
    np.random.shuffle(ind)
    filenames = filenames[ind]
    labels = labels[ind]
    f_train = open('data/sw_stage1_train_listfile','w')
    f_val = open('data/sw_stage1_val_listfile','w')
    for this_filename, this_label in zip(filenames, labels):
        
        if (np.random.random()<frac_val):
            f_val.write('%s %i\n'%(this_filename, this_label))
        else:
            f_train.write('%s %i\n'%(this_filename, this_label))
    f_train.close()
    f_val.close()


def load_labels():
    from pandas.io.parsers import read_csv
    df = read_csv('data/cluster_catalog.csv') #, index_col='cutoutname')
    return df


def make_jpg_copies():
    pass
    '''
    from scipy.misc import imread, imsave
    from glob import glob
    filenames = glob('data/cutouts_good/*.png')
    for filename in filenames:
        x = imread(filename)
        savename = filename.split('.png')[0] + '.jpg'
        imsave(x, savename)
    '''
