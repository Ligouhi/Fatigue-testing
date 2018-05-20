#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 11 00:14:45 2018

@author: hui
"""

import tensorflow as tf
from net import keras_net
import os
import cv2 as cv
import numpy as np
keras = tf.keras
Input = keras.layers.Input
regularzation = keras.regularizers.l2
Model = keras.models.Model
pp = []
def evalu():
    
    inputs = Input(shape=(24,24,3),name = 'inputs')
    logit = keras_net(inputs,regularzation(0.005),0.5,True)
    
    model = Model(inputs = inputs,outputs = logit)
    model.load_weights('../weights3.h5',by_name=True)
    dirs = [x[0] for x in os.walk('../openANDcloseTest/')]
    i = 2
    p = 0
    c = 0
    for l in dirs[1:]:
        i -= 1
        names = os.listdir(l)
        for name in names:
            path = os.path.join(l,name)
            image = cv.imread(path)
            image = np.expand_dims(image,0)
            sc = model.predict(image)
            sc = np.argmax(sc,1)
            c += 1
            if sc[0] == i:
                p += 1
            print('检测%s张图片,正确%s张，正确率为:%s'%(c,p,p/c))
    
    
evalu()