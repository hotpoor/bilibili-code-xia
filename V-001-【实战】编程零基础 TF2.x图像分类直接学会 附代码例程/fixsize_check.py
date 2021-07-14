#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pathlib
from PIL import Image
import cv2 as cv
import os
data_dir = pathlib.Path("dataset_check")
image_count = len(list(data_dir.glob('*.jpg')))
print(image_count)

for image_addr in list(data_dir.glob('*.jpg')):
    print(image_addr)
    print("saving",image_addr)
    a = cv.imread("./%s"%image_addr,0)
    res = cv.resize(a,(int(100), int(100)), interpolation = cv.INTER_CUBIC)
    print(a)
    try:
        cv.imwrite("./%s"%image_addr,res)
        print("saved")
    except:
        print("error")
        os.remove(image_addr)
    