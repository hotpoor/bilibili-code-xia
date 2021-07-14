from PIL import Image, ImageGrab
import mss
import mss.tools
import time
import cv2 as cv
import pyautogui


import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

import pathlib

model = tf.keras.models.load_model('saved_model/my_model')

batch_size = 32
img_height = 100
img_width = 100

class_names=['class_luoxiang', 'class_luoyonghao', 'class_luozhengyu']
check_img_dir = pathlib.Path("dataset_check")
for image_addr in list(check_img_dir.glob('*.jpg')):
    check_path = image_addr
    img = keras.preprocessing.image.load_img(
        check_path, target_size=(img_height, img_width)
    )
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])
    k = class_names[np.argmax(score)]
    print("---")
    print(k,score)
    print(image_addr)
    print("---")






