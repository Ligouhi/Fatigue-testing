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
<<<<<<< HEAD
    
#    #嘴巴
#    mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')
#    mouth_cascade.load('d:/github/Facial-Features-Detection/haarcascade_smile.xml') 
#   
#    
#    detector.set_min_face_size(40)
    image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#    mouth = mouth_cascade.detectMultiScale(image_gray, 1.5,5)
#    mouth = mouth[-1]

=======
    detector.set_min_face_size(40)
    image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
>>>>>>> eeefcbf2b85cd27b19bae65ac760281ee8694b23

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
<<<<<<< HEAD
        mouth = landmarks[-2:]
        
        mouths = [(mouth[0][0]+mouth[1][0])/2-0.5*w*0.32,abs(mouth[0][1]-0.5*h*0.2),abs(mouth[0][0]-mouth[1][0]),h*0.2]
        mouths = list(map(lambda x:int(x),mouths))
=======
>>>>>>> eeefcbf2b85cd27b19bae65ac760281ee8694b23
        
        eyel = [abs(eye[0][0]-0.5*w*0.32),abs(eye[0][1]-0.5*h*0.3),w*0.32,h*0.3]
        eyel = list(map(lambda x:int(x),eyel))
        eyer = [abs(eye[1][0]-0.5*w*0.32),abs(eye[1][1]-0.5*h*0.3),w*0.32,h*0.3]
        eyer = list(map(lambda x:int(x),eyer))
<<<<<<< HEAD
    
#    mouths = getmouth(img)
#        mouth = 
    return [face,eyel,eyer,mouths]
=======
    return [face,eyel,eyer]
>>>>>>> eeefcbf2b85cd27b19bae65ac760281ee8694b23
