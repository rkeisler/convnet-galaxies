#!/bin/bash
apt-get update
apt-get install emacs
git config --global core.editor emacs
cp .bashrc /root/
sudo pip install Pillow==2.6.0
