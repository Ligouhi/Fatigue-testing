#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 21:36:31 2018

@author: hui
"""

import tensorflow as tf
layers = tf.layers
keras = tf.keras
conv2d = keras.layers.Conv2D
flatten = keras.layers.Flatten
dense = keras.layers.Dense
norm = keras.layers.BatchNormalization
l2 = keras.regularizers.l2
pool = keras.layers.AveragePooling2D
drop = keras.layers.Dropout

'''
def net(inputs,regularization,bn = False):
    #block1
    x = layers.conv2d(inputs,32,(3,3),activation=tf.nn.relu,padding='same',kernel_regularizer=regularization,bias_regularizer=regularization,name = 'conv1')
    if bn:
        x = layers.batch_normalization(x)
    x = layers.average_pooling2d(x,(2,2),(1,1),name='pool1')
    x = layers.conv2d(x,64,(3,3),activation=tf.nn.relu,padding='same',kernel_regularizer=regularization,bias_regularizer=regularization,name = 'conv2')
    if bn:
        x = layers.batch_normalization(x)
    x = layers.average_pooling2d(x,(2,2),(1,1),name='pool2')
    x = layers.conv2d(x,128,(3,3),activation=tf.nn.relu,kernel_regularizer=regularization,bias_regularizer=regularization,name = 'conv3')
    if bn:
        x = layers.batch_normalization(x)
    x = layers.max_pooling2d(x,(1,1),(1,1),name = 'pool3')
    x = layers.flatten(x,name = 'flatten')
    x = layers.dense(x,32,activation=tf.nn.relu,name='f1')
    if bn:
        x = layers.batch_normalization(x)
    out = layers.dense(x,2,activation=tf.nn.softmax,name='out')
    tf.Summary()
    return out
'''

def keras_net(inputs,regularzation,dropout_rate = None,bn=False):
    
    x = conv2d(32,(2,2),activation='relu',kernel_initializer='he_uniform',kernel_regularizer=regularzation,padding='same',name = 'conv1')(inputs)
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
    return x

