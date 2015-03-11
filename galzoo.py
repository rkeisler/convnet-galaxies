import numpy as np
np.random.seed(0)
import ipdb


def main():
    preprocess_training_images()
    make_train_and_val_listfiles()

def make_train_and_val_listfiles(frac_val=0.2):
    from glob import glob
    filenames = glob('data/newtrain/*.jpg')
    np.random.shuffle(filenames)
    label_dict = get_kmeans_labels()
    f_train = open('data/train_listfile','w')
    f_val = open('data/val_listfile','w')
    for filename in filenames:
        tmp = filename.split('/')
        this_id = tmp[-1].split('.jpg')[0]
        this_label = label_dict[this_id]
        this_name = tmp[-1]
        # format is subfolder1/file1.JPEG 7
        if (np.random.random()<frac_val):
            f_val.write('%s %i\n'%(this_name, this_label))
        else:
            f_train.write('%s %i\n'%(this_name, this_label))            
    f_train.close()
    f_val.close()


def get_kmeans_labels(n_clusters=20):
    # The labels are actually 37-dimensional vectors,
    # and thus naturally suited to a regression problem.
    # While caffe is capable of regression, it will be slightly
    # easier for us to read the data in if we recast this as
    # a classification problem.
    f = open('data/training_solutions_rev1.csv')
    f.next()
    ids=[]
    scores = []
    for line in f:
        tmp = line.split(',')
        ids.append(tmp[0])
        scores.append(np.array(tmp[1:],dtype=np.float))
    f.close()
    scores = np.array(scores)
    from sklearn.cluster import KMeans
    km = KMeans(n_clusters=n_clusters)
    labels = km.fit_predict(scores)
    output=dict(zip(ids, labels))
    return output

def get_mode_labels():
    # The labels are actually 37-dimensional vectors,
    # and thus naturally suited to a regression problem.
    # While caffe is capable of regression, it will be slightly
    # easier for us to read the data in if we recast this as
    # a classification problem.  For each galaxy, we will 
    # try to predict the morphology dimension with the highest score.
    # Since they're pretty sparse, this isn't too different from the 
    # original regression problem.
    f = open('data/training_solutions_rev1.csv')
    f.next()
    output = {}
    for line in f:
        tmp = line.split(',')
        id = tmp[0]
        vals = np.array([np.float(thing) for thing in tmp[1:]])
        this_label = vals.argmax()
        output[id] = this_label
    f.close()
    uniq_labels = set(output.values())
    return output



def preprocess_training_images(savedir='data/newtrain/'):
    import os
    from scipy.misc import imsave
    from glob import glob
    filenames = glob('data/images_training_rev1/*.jpg')
    if not os.path.exists(savedir):
            os.makedirs(savedir)
    nfilenames = len(filenames)
    for ifilename,filename in enumerate(filenames):
        if (ifilename % 100)==0: print '%i/%i'%(ifilename, nfilenames)
        x = preprocess3band(filename)
        savename = savedir + '/' + filename.split('/')[-1]
        imsave(savename, x)


def preprocess3band(filename, ds=4., mask_strength=None):
    from scipy.misc import imread
    from scipy.ndimage.filters import gaussian_filter
    # Open image file.
    x = imread(filename).astype(np.float)
    # Gaussian smooth with FWHM = DS pixels.
    for i in range(3):
        x[:,:,i] = gaussian_filter(x[:,:,i], 1.*ds/2.355)
    # Subsample by DS.
    x = x[0::int(ds), 0::int(ds), :]
    # take inner 96x96.
    ntmp = x.shape[0]-96
    if (ntmp % 2)==0:
        nside=ntmp/2
        x = x[nside:-nside, nside:-nside, :]
    else:
        nside=(ntmp-1)/2
        x = x[nside+1:-nside, nside+1:-nside, :]
    # If desired, apply mask.
    if (mask_strength!=None) & (mask_strength!='none'):
        if (mask_strength=='weak'): mask_thresh = 15.
        if (mask_strength=='strong'): mask_thresh = 30.
        avg = np.mean(x,axis=-1)
        mask = get_mask(avg, thresh=mask_thresh)
        x *= mask[:,:,np.newaxis]
    x = x.astype(np.uint8)
    return x


def get_mask(img, thresh=25):
    from skimage.filter import gaussian_filter
    from scipy import ndimage
    (nx,ny)=img.shape
    sm = gaussian_filter(img, 4.0)
    notdark = sm>thresh
    label_objects, nb_labels = ndimage.label(notdark)
    mask = label_objects == label_objects[np.round(nx/2.), np.round(ny/2.)]
    return mask


if __name__ == '__main__':
    main()
