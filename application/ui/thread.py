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
<<<<<<< HEAD
from modelm import models2
=======
>>>>>>> eeefcbf2b85cd27b19bae65ac760281ee8694b23

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
<<<<<<< HEAD
      
=======
    
>>>>>>> eeefcbf2b85cd27b19bae65ac760281ee8694b23
    def __build__(self):
        
        if not self.model:
            self.model = build()
<<<<<<< HEAD
    
=======
>>>>>>> eeefcbf2b85cd27b19bae65ac760281ee8694b23
        
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
            
<<<<<<< HEAD
  

class Thread_mou(QThread):
    
    signal = pyqtSignal(list)
    
    def __init__(self,parent = None):
        
        super(Thread_mou,self).__init__(parent)
#        self.mmodel1 = None
        self.mmodel2 = None
        self.__build__()
    def __build__(self):
        
#        if not self.mmodel1:
#            self.mmodel1 = models1()
        if not self.mmodel2:
            self.mmodel2 = models2()   
    def getmouth(self,image):    
    
        b_h,b_w = image.shape[0:2]
        image_ = cv.resize(image,(96,96),interpolation=cv.INTER_CUBIC)
        image_g = cv.cvtColor(image_, cv.COLOR_BGR2GRAY)
        image_gray = np.expand_dims(image_g,2)
        
        img = np.expand_dims(image_gray,0)
       
        # mouth l,r,t
        mouths = self.mmodel2.predict(img)
        mou = []
        for i in range(0,29,2):
            mou.append([int(mouths[:,i]),int(mouths[:,i+1])])
#        mou_l = mouth[:,0:2]
#        mou_r = mouth[:,2:4]
#        mou_top = mouth[:,4:6]
#        mou_bottom = mouth[:,6:8]
#        
#        #mouth bottom
##        b_mou = self.mmodel2.predict(img)
##        
##        mou_bottom = b_mou[:,0:2]
#        
#        
#        x_ch = b_w/96
#        y_ch = b_h/96
#        
#        w = int(abs(abs(mou_l[:,0])-abs(mou_r[:,0]))*x_ch)
#        h = int(abs(abs(mou_top[:,1])-abs(mou_bottom[:,1]))*y_ch)
#        
#        y = int(abs(mou_top[:,1])*y_ch)
#        x = int(abs(mou_l[:,0])*x_ch)
#        
#        res = [x,y,w,h]
        
        self.signal.emit(mou)
=======
>>>>>>> eeefcbf2b85cd27b19bae65ac760281ee8694b23
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