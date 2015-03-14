#!/bin/bash

# ROUND 1
# 35k iters, [0k to 35k], base_lr: 0.001
# accuracy = 0.9725, loss = 0.119544
#caffe train --solver=solver.prototxt

# ROUND 2
# 5k iters, [35k to 40k], base_lr: 0.0001
# accuracy = 0.975417, loss = 0.136706
#caffe train --solver=solver.prototxt --weights=net_sw_stage1_lr0p001_iter_35000.caffemodel

# ROUND 3
# 5k iters, [40k to 45k], base_lr: 0.00001
# accuracy = 0.975, loss = 0.13179
#caffe train --solver=solver.prototxt --weights=net_sw_stage1_lr0p0001_iter_5000.caffemodel
