#!/bin/bash

# ROUND 1
# 60k iters, [0k to 60k], base_lr: 0.001
# accuracy = 0.43669, loss = 1.56687
#caffe train --solver=solver.prototxt

# ROUND 2
# 20k iters, [60k to 80k], base_lr: 0.0001
# accuracy = 0.446729, loss = 1.58194
#caffe train --solver=solver.prototxt --weights=netgalzoo_iter_60000_lr0p001.caffemodel

# ROUND 3
# 20k iters, [80k to 100k], base_lr: 0.00001
caffe train --solver=solver.prototxt --weights=netgalzoo_iter_20000_lr0p0001.caffemodel
