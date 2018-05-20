#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 09:19:14 2018
线程类
@author: hui
"""
#from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from cls_utils import build
import numpy as np
#import imutils
import cv2 as cv
from pyseeta import Detector
from pyseeta import Aligner
from get_point import get_point
import os
import win32com.client

def get_model(mod):
    base = os.path.dirname(os.getcwd())
    if mod == 'face':
        return os.path.join(base,'model','seeta_fd_frontal_v1.0.bin')
    else:
        return os.path.join(base,'model','seeta_fa_v1.1.bin')
class voice(QThread):
     def __init__(self,parent = None):
        
        super(voice,self).__init__(parent)
        self.spk = win32com.client.Dispatch("SAPI.SpVoice")
     def run(self,a):
         self.spk.Speak(a)
class Thread_cls(QThread):
    '''
    判断线程
    '''
    signalOut = pyqtSignal(list)
    
    def __init__(self,parent = None):
        
        super(Thread_cls,self).__init__(parent)
        self.model = None
        self.__build__()
    
    def __build__(self):
        
        if not self.model:
            self.model = build()
        
    def run(self,images):
        '''
        images 包含两个眼睛的灰度图
        return :检测结果
        '''
        if self.model:
            results = []
            for image in images:
                image = cv.cvtColor(image,cv.COLOR_RGB2GRAY)
                image_ = np.zeros(image.shape + (3,))
                image_[:,:,0] = image[:,:]
                image_[:,:,1] = image[:,:]
                image_[:,:,2] = image[:,:]
                img = cv.resize(image_,(24,24),cv.INTER_AREA)
#                a=1.2
#                b=50
#                for i in range(24):
#                    for j in range(24):
#                        for c in range(3):
#                            color=image_[i,j][c]*a+b
#                            if color>255:
#                                image_[i,j][c]=255
#                            elif color<0:
#                                image_[i,j][c]=0
#                
                image_ = np.expand_dims(img,0)
                res = self.model.predict(image_)
                results.append(np.argmax(res,1)[0])
                
            self.signalOut.emit(results)
            
class Thread_reg(QThread):
    '''
    检测线程
    '''
    signal = pyqtSignal(list)
    def __init__(self,parent = None):
        
        super(Thread_reg,self).__init__(parent)
        self.aligner = None
        self.detector = None
        self.__build__()
        
    def __build__(self):
        '''
        检测模型加载
        '''
        self.detector = Detector(get_model('face')) 
        self.aligner = Aligner(get_model('aligner'))
        
    def run(self,image):
        '''
        执行检测任务,发出一个list，存储各处坐标信息
        [box_face,box_eye_left,box_eye_right]
        '''
        
        point = get_point(image,self.detector,self.aligner)
        
        self.signal.emit(point)