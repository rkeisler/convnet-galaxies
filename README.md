# convnet-galaxies
code for studying images of galaxies with convolutional neural networks

## Get the galzoo data.

Download training images (``images_training_rev1.zip``) and labels (``training_solutions_rev1.zip``) from [here](https://www.kaggle.com/c/galaxy-zoo-the-galaxy-challenge/data) (must be logged in to kaggle).  Put them into ``data/`` and unzip them.

## notes on SpaceWarps data

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

### Plan
I will train a net from scratch on Stage 1.
Then I will fine-tune that net on Stage 2.

Then I may go back and try this again, where I start with a net trained on GalaxyZoo morphology data.
