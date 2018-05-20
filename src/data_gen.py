#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 22:07:48 2018

@author: hui
"""

import tensorflow as tf
keras = tf.keras

DataGenerator = keras.preprocessing.image.ImageDataGenerator

def data_generation(Dir,target_size,prov_params = None,train = True):
    '''
    数据生成器
    arg:
        Dir:存放数据根目录
    '''
    if prov_params:
        d = DataGenerator()
        
    d = DataGenerator()
    d = d.flow_from_directory(Dir,target_size=target_size,seed=1123,save_to_dir='../prov/',save_format='jpeg')
    return d

