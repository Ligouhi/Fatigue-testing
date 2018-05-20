#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 22:37:06 2018

@author: hui
"""

import tensorflow as tf
from net import keras_net
from data_gen import data_generation
import os
Model = tf.keras.models.Model
Input = tf.keras.layers.Input
l2 = tf.keras.regularizers.l2
keras = tf.keras
DataGenerator = keras.preprocessing.image.ImageDataGenerator
SGD = keras.optimizers.SGD
ada = keras.optimizers.Adam
target_size = (24,24)
weights = '../weights2.h5'
'''
def train():

    with tf.Graph().as_default():
        x = tf.placeholder(tf.float32,shape=(None,target_size[0],target_size[1],3),name = 'inputs')
        y = tf.placeholder(tf.int32,shape=(None,2),name = 'label')
    
        y_ = net(x,tf.nn.l2_normalize)
        loss = tf.losses.softmax_cross_entropy(y,y_)
        op = tf.train.AdamOptimizer().minimize(loss)
        correct_prediction = tf.equal(tf.argmax(y_,1), tf.argmax(y,1))
        acc = tf.reduce_mean(tf.cast(correct_prediction,'float'))
    
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            d = data_generation('../openANDclose/',target_size)
            dd = data_generation('../openANDcloseTest/',target_size)
            dd.batch_size = dd.n
            (val_image,val_label) = dd.next()
            for i in range(3000):
                (image,label) = d.next()
                sess.run(op,feed_dict = {x:image,y:label})
                if i % 10 == 0:
                    ls = sess.run(loss,feed_dict={x:image,y:label})
                    a = sess.run(acc,feed_dict={x:val_image,y:val_label})
                    print('%s epoch acc is %s'%(i,a))
                    print('%s epoch loss is %s'%(i,ls))

'''
def train_keras(weights,l2_rate = 0.0005,drop_rate = 0.5):
    
    inputs = Input(shape=(24,24,3),name = 'inputs')
    logit = keras_net(inputs,l2(l2_rate),drop_rate,True)
    
    model = Model(inputs = inputs,outputs = logit)
    
    if weights and os.path.exists(weights):
        model.load_weights(weights,by_name=True)
        for layer in model.layers[:-2]:
            layer.trainable = False
    model.compile(optimizer=ada(0.0001),loss = ['binary_crossentropy'],metrics=['binary_accuracy'])
    model.summary()
    train_gen = data_generation('../openANDclose/',target_size)
    model.fit_generator(train_gen,steps_per_epoch=int(train_gen.n/train_gen.batch_size)+1,
                        epochs=10)
    
    model.save_weights('../weights3.h5')
    