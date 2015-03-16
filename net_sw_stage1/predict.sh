#!/bin/bash

rm -r features
extract_features.bin net_sw_stage1_lr0p00001_iter_5000.caffemodel deploy.prototxt fc6 features 10 lmdb GPU

