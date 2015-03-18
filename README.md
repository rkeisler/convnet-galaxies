# Overview

This repo contains code for studying images of galaxies with convolutional neural networks.  We use [caffe](caffe.berkeleyvision.org) for all of the training and prediction.  I used a [terminal.com snap](https://www.terminal.com/snapshot/4c3277602398f199c39133d2dcc9a0cb61a5547e31f3f46d5cb3055108214cf0) to do the training (careful - $1 per hour!).


## the different convnets

All of these nets share the same architecture (3 conv layers + 2 fully-connected layers + 1 fully-connected output layer), except that the dimension of the last FC layer changes between the GalaxyZoo and SpaceWarps datasets.   The nets are trained using [caffe](caffe.berkeleyvision.org).

 - `net_sw_stage1` - I trained a net from scratch using only the SpaceWarps stage 1 data provided by Chris/Phil.  The details of training are in `net_sw_stage1/train.sh`.  I get accuracy = 0.975 (loss = 0.132) on the validation set.

 - `net_sw_stage1_xfer` - Same as above, but instead of training from scratch I fine-tuned a net that had already been trained on the GalaxyZoo morphology data (see more below).  The details of training are in `net_sw_stage1_xfer/train.sh`.  I get accuracy = 0.971 (loss = 0.070) on the validation set.

 - `netgalzoo` - I trained a net from scratch on the GalaxyZoo morphology data.  The training and test data are from the related [kaggle competition](https://www.kaggle.com/c/galaxy-zoo-the-galaxy-challenge/data).  Because of some annoying feature of the `caffe` data layer, I formulated this as a classification problem rather than the original regression problem in the kaggle competition.  Specifically, I used kmeans to define 20 morphology types, and tried to classify into those 20 types.


## To Do
 - Generate ROC curves.
 - Fine-tune the best Stage 1 net on Stage 2.


## some notes on SpaceWarps data

I'm a bit confused about the labels.

category:
training    26053
test         9030

OK, there are 26053 training images and 9030 test images.

kind:
sim     16562
dud      9491
test     9030

Of those training images, 16562 (63%) are presumably simulated images of lenses, and the remaining 37% are not lenses.

truth:
LENS       16562
NOT         9491
UNKNOWN     9030

OK, yes, this continues to make sense, except that I don't know if the test images are lenses or not...

flavor:
dud                9491
test               9030
lensed galaxy      5983
lensing cluster    5308
lensed quasar      5271

This breaks the truth type down further, and it'd be interesting to train a classifier on these categories, but still, how am I supposed to see how well I'm performing on the test images if I don't know their truth value?  Are the truth values of the test images supposed to be truly hidden, known only to the SW organizers, so that they can evaluate the performance of various lens-finding algorithms?

### STAGE 1
There are 
24177 (d.stage==1)
8362  (d.stage==1)&(d.truth=='NOT')
10656 (d.stage==1)&(d.truth=='LENS')&(d.alpha==0)
5159  (d.stage==1)&(d.truth=='LENS')&(d.alpha==1)
I.e 
(8362 + 10656) = 19018 = 79% are not images of lenses.
(5159) = 21% are images of lenses.

### STAGE 2
There are 
10906 (d.stage==2)
1129  (d.stage==2)&(d.truth=='NOT')
596   (d.stage==2)&(d.truth=='LENS')&(d.alpha==0)
151   (d.stage==2)&(d.truth=='LENS')&(d.alpha==1)
9030  (d.stage==2)&(d.truth=='UNKNOWN')
So the majority (~90%) of these are data and we literally don't know if they are lenses are not.
Of the remaining ~10% Stage 2 where we know what they are, 
  (1129 + 596) = 1725 = 92% are not images of lenses.
  151 = 8% are images of lenses.
