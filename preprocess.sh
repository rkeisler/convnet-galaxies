#!/bin/bash

# GALZOO
#python galzoo.py
#convert_imageset data/newtrain/ data/train_listfile data/train_lmdb
#convert_imageset data/newtrain/ data/val_listfile data/val_lmdb
#compute_image_mean data/train_lmdb data/train_mean_image -backend "lmdb"

# SPACEWARPS STAGE 1
convert_imageset data/cutouts_good/ data/sw_stage1_train_listfile data/sw_stage1_train_lmdb
convert_imageset data/cutouts_good/ data/sw_stage1_val_listfile data/sw_stage1_val_lmdb
compute_image_mean data/sw_stage1_train_lmdb data/sw_stage1_train_mean_image -backend "lmdb"
