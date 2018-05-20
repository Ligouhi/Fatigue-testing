#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 11 16:11:29 2018

@author: hui
"""

import tensorflow as tf
import os
base = os.path.dirname(os.getcwd())
keras = tf.keras
conv2d = keras.layers.Conv2D
flatten = keras.layers.Flatten
dense = keras.layers.Dense
norm = keras.layers.BatchNormalization
l2 = keras.regularizers.l2
pool = keras.layers.AveragePooling2D
drop = keras.layers.Dropout
Input = keras.layers.Input
Model = keras.models.Model

def build(regularzation = l2(0.0005),dropout_rate = 0.5,bn=True):
    tf.reset_default_graph()
    inp = Input(shape = (24,24,3))
    x = conv2d(32,(2,2),activation='relu',kernel_initializer='he_uniform',kernel_regularizer=regularzation,padding='same',name = 'conv1')(inp)
    x = pool(strides=[1,1],name = 'pool1')(x)
    if bn:
        x = norm(name = 'bn1')(x)
    x = conv2d(96,(2,2),activation='relu',kernel_initializer='he_uniform',kernel_regularizer=regularzation,padding='same',name = 'conv2')(x)
    x = pool(strides=[1,1],name = 'pool2')(x)
    if bn:
        x = norm(name = 'bn2')(x)
    x = conv2d(192,(2,2),activation='relu',padding='same',kernel_initializer='he_uniform',kernel_regularizer=regularzation,name = 'conv3')(x)
    x = pool(name = 'pool3')(x)
    x = flatten(name = 'flatten')(x)
    if dropout_rate:
        x = drop(dropout_rate,seed = 2233,name = 'drop')(x)
    x = dense(2,activation='softmax',kernel_regularizer= regularzation,name = 'out')(x)
    
    model = Model(inputs = inp,outputs = x)
    model.load_weights(os.path.join(base,'model','weights3.h5'),by_name=True)
    return model