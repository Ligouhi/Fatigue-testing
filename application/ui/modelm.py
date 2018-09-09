# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 10:43:33 2018

@author: RenTeng
"""

import os
import numpy as np
from pandas.io.parsers import read_csv
from sklearn.utils import shuffle
from sklearn.cross_validation import train_test_split
from collections import OrderedDict
import cv2 as cv

import keras
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Activation, Convolution2D, MaxPooling2D, Flatten, Dropout
from keras.optimizers import SGD
from keras.models import model_from_json
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import LearningRateScheduler, EarlyStopping


#def models1():
#    weights_path = './mouth3.h5'
#    
#    
#    
#    model = Sequential()
#    
#    model.add(Convolution2D(32, 3, 3, input_shape=( 96, 96,1)))
#    model.add(Activation('relu'))
#    model.add(MaxPooling2D(pool_size=(2, 2)))
#    model.add(Dropout(0.1))
#    
#    model.add(Convolution2D(64, 2, 2))
#    model.add(Activation('relu'))
#    model.add(MaxPooling2D(pool_size=(2, 2)))
#    model.add(Dropout(0.2))
#    
#    model.add(Convolution2D(128, 2, 2))
#    model.add(Activation('relu'))
#    model.add(MaxPooling2D(pool_size=(2, 2)))
#    model.add(Dropout(0.3))
#    
#    model.add(Flatten())
#    model.add(Dense(1000))
#    model.add(Activation('relu'))
#    model.add(Dropout(0.5))
#    model.add(Dense(1000))
#    model.add(Activation('relu'))
#    model.add(Dense(2))
#    
#    keras.backend.get_session().run(tf.global_variables_initializer())
#    assert os.path.exists(weights_path), 'Model weights not found (see "weights_path" variable in script).'
#    model.load_weights(weights_path,by_name=True)
#    return model


def models2():
    weights_path = './weights-500.h5'
    
    
    
    model = Sequential()
    
    model.add(Convolution2D(32, 3, 3, input_shape=( 96, 96,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.1))
    
    model.add(Convolution2D(64, 2, 2))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.2))
    
    model.add(Convolution2D(128, 2, 2))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.3))
    
    model.add(Flatten())
    model.add(Dense(1000))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(1000))
    model.add(Activation('relu'))
    model.add(Dense(30))
    
    keras.backend.get_session().run(tf.global_variables_initializer())
    assert os.path.exists(weights_path), 'Model weights not found (see "weights_path" variable in script).'
    model.load_weights(weights_path,by_name=True)
    return model

        

