# -*- coding: utf-8 -*-
"""
Created on Sun May 13 19:11:25 2018

@author: jhdn
"""
from pyseeta import Detector
from pyseeta import Aligner


try:
    import cv2

except ImportError:
    raise ImportError('opencv can not be found!')


def get_point(img,detector,aligner):
    detector.set_min_face_size(40)
    image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = detector.detect(image_gray)
    #获取人脸坐标，以list形式储存
    face = faces[0]
    face=[face.left-10, face.top-10, face.right-face.left+10, face.bottom-face.top+10]
        


    #获取眼镜坐标，list储存
    w = face[2]
    h = face[3]
    for faceq in faces:
        landmarks = aligner.align(image_gray, faceq)
        eye=landmarks[:2]
        
        eyel = [abs(eye[0][0]-0.5*w*0.32),abs(eye[0][1]-0.5*h*0.3),w*0.32,h*0.3]
        eyel = list(map(lambda x:int(x),eyel))
        eyer = [abs(eye[1][0]-0.5*w*0.32),abs(eye[1][1]-0.5*h*0.3),w*0.32,h*0.3]
        eyer = list(map(lambda x:int(x),eyer))
    return [face,eyel,eyer]
