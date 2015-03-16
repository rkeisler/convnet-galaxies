import numpy as np

caffe_root = '/root/caffe/'
import sys
sys.path.insert(0, caffe_root + 'python')

import caffe
caffe.set_mode_cpu()
net = caffe.Net('deploy.prototxt','net_sw_stage1_lr0p00001_iter_5000.caffemodel',caffe.TEST)


transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_transpose('data', (2,0,1))
#transformer.set_mean('data', np.load(caffe_root + 'python/caffe/imagenet/ilsvrc_2012_mean.npy').mean(1).mean(1)) # mean pixel
transformer.set_raw_scale('data', 255)  # the reference model operates on images in [0,255] range instead of [0,1]
transformer.set_channel_swap('data', (2,1,0))  # the reference model has channels in BGR order instead of RGB

net.blobs['data'].reshape(1,3,86,86)
net.blobs['data'].data[...] = transformer.preprocess('data', caffe.io.load_image('../data/cutouts_good/23523_ASW0007mfp.png'))
out = net.forward()
probs = np.exp(out['fc6']) / np.exp(out['fc6']).sum() # correct?

