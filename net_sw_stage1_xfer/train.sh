#!/bin/bash

# ROUND A
# all frozen except myfc6
# starting with net trained on galzoo morphology, where targets
# where 20 kmeans classes derived from 37-dim morphology vector.
# accuracy = 0.849375, loss = 0.322444
# 5k iters, base_lr: 0.00001
#caffe train --solver=solver.prototxt --weights=netgalzoo_lr0p0001_iter_20000.caffemodel

# ROUND B
# all frozen except myfc6, fc5
# 5k iters, base_lr: 0.00001
# accuracy = 0.880417, loss = 0.265242
#caffe train --solver=solver.prototxt --weights=net_sw_stage1_xfer_A_iter_5000.caffemodel

# ROUND C
# all frozen except myfc6, fc5, fc4
# 5k iters, base_lr: 0.0001 *Note that I changed lr here.
# accuracy = 0.95, loss = 0.123419
#caffe train --solver=solver.prototxt --weights=net_sw_stage1_xfer_B_iter_5000.caffemodel

# ROUND D
# all frozen except myfc6, fc5, fc4, conv3
# 5k iters, base_lr: 0.0001
# accuracy = 0.963125, loss = 0.0900938
#caffe train --solver=solver.prototxt --weights=net_sw_stage1_xfer_C_iter_5000.caffemodel

# ROUND E
# all frozen except myfc6, fc5, fc4, conv3, conv2
# 10k iters, base_lr: 0.0001
# accuracy = 0.969375, loss = 0.0737014
#caffe train --solver=solver.prototxt --weights=net_sw_stage1_xfer_D_iter_5000.caffemodel

# ROUND F
# all free
# 5k iters, base_lr: 0.0001
# accuracy = 0.969583, loss = 0.075845
#caffe train --solver=solver.prototxt --weights=net_sw_stage1_xfer_E_iter_10000.caffemodel

# ROUND G
# all free
# 10k iters, base_lr: 0.00001 *lowered it
# accuracy = 0.97125, loss = 0.0698651
#caffe train --solver=solver.prototxt --weights=net_sw_stage1_xfer_F_iter_5000.caffemodel
