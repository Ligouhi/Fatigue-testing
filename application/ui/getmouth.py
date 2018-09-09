# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 11:13:32 2018

@author: RenTeng
"""

from modelm import models
import cv2
import numpy as np



def getmouth(image):    
    
    model = models()
    b_h,b_w = image.shape[0:2]
    image_ = cv2.resize(image,(96,96),interpolation=cv2.INTER_CUBIC)
    image_g = cv2.cvtColor(image_, cv2.COLOR_BGR2GRAY)
    image_gray = np.zeros([96,96,1])
    image_gray[:,:,0] = image_g
    
    

    img = np.expand_dims(image_gray,0)
   
    
    mouth = model.predict(img)
    
    mou_l = mouth[0:2]
    mou_bottom = mouth[:,6:8]
    mou_r = mouth[:,2:4]
    mou_top = mouth[:,4:6]
    
    y_ch = b_h/96
    x_ch = b_w/96
    

    
    h = int(abs(abs(mou_top[:,1])-abs(mou_bottom[:,1]))*y_ch)
    w = int(abs(abs(mou_l[:,0])-abs(mou_r[:,0]))*x_ch)
    
    
    y = int(abs(mou_top[:,1])*y_ch)
    x = int(abs(mou_l[:,0])*x_ch)
    
    res = [x,y,w,h]
    
    return res
