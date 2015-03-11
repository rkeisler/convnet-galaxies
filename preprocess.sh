#!/bin/bash
#python galzoo.py
convert_imageset data/newtrain/ data/train_listfile data/train_lmdb
convert_imageset data/newtrain/ data/val_listfile data/val_lmdb
compute_image_mean data/train_lmdb data/train_mean_image -backend "lmdb"

