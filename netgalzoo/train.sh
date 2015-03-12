#!/bin/bash

# ROUND 1
# 60k iters, [0k to 60k], base_lr: 0.001
# accuracy = 0.43669, loss = 1.56687
#caffe train --solver=solver.prototxt

# ROUND 2
# 20k iters, [60k to 80k], base_lr: 0.0001
# accuracy = 0.446729, loss = 1.58194
#caffe train --solver=solver.prototxt --weights=netgalzoo_lr0p001_iter_60000.caffemodel

# ROUND 3
# 10k iters, [80k to 90k], base_lr: 0.00001
# accuracy = 0.448187, loss = 1.59942
# didn't help much, actually slightly worse.
#caffe train --solver=solver.prototxt --weights=netgalzoo_lr0p0001_iter_20000.caffemodel
