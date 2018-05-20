#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 16:45:52 2018

@author: hui
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from view import Ui_view
import cv2 as cv
import sys
import numpy as np
from cls_utils import *
from thread import Thread_cls,Thread_reg,voice
import matplotlib.pyplot as plt

class MyFrame(QFrame,Ui_view):
    
    def __init__(self,parent = None):
        
        QFrame.__init__(self,parent)
        self.setupUi(self)
        self.status1 = 0
        self.status2 = 0
        self.model = None
        self.items = {0:'睁眼',1:'闭眼'}
        self.cls = Thread_cls()
        self.reg = Thread_reg()
        self.spk = voice()
        self.close_time = 0
        self.open_time = 0
        self.start = 0
        self.reg.signal.connect(self.eye_list)
        self.cls.signalOut.connect(self.cls_result)
        self.spk.run('您好！欢迎使用疲劳驾驶检测系统！')
        self.initUi()
        
    def initUi(self):
        self.timer_camera = QTimer(self)
        self.cap = cv.VideoCapture(0)
        self.timer_camera.timeout.connect(self.show_pic)
        self.play1.clicked.connect(self.cliked_play1)
        self.play2.clicked.connect(self.cliked_play2)
        self.exit.clicked.connect(self.clicked_exit)
        self.timer_camera.start(10)
    
    def show_pic(self):
        
        ret,frame = self.cap.read()
        if ret:
            show = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
            show = self.modeFunc(show)
            showImage = QImage(show.data,show.shape[1],show.shape[0],
                               QImage.Format_RGB888)
#            showImage = QImage(show1.data,show1.shape[1],show1.shape[0],
#                               QImage.Format_RGB888)
            if self.status1 == 1:
                self.label.setPixmap(QPixmap.fromImage(showImage))
            showgray = cv.cvtColor(show,cv.COLOR_RGB2GRAY)
            showgray = QImage(showgray.data,showgray.shape[1],showgray.shape[0],
                              QImage.Format_Grayscale8)
            if self.status2 == 1:
                self.label2.setPixmap(QPixmap.fromImage(showgray))
            
    def cliked_play1(self):
        
        if self.status1 == 0:
            self.status1 = 1
        else:
            self.status1 =0
        
            
    def cliked_play2(self):
        
        if self.status2 == 0:
            self.status2 = 1
        else:
            self.status2 =0
        

    def clicked_exit(self):
        
        self.cap.release()
        cv.destroyAllWindows()
        self.close()
    def modeFunc(self,image):
        if self.b1.isChecked():
            '''
            用户反馈
            '''
            return image
        
        if self.b2.isChecked():
            '''
            检测加预测
            '''
            if self.status1 == 1:
                self.reg.run(image)
                if len(self.boxs) == 3: 
#                    boxs = self.boxs
#                    face = image[boxs[0][0]:boxs[0][0]+boxs[0][2],boxs[0][1]:boxs[0][1]+boxs[0][3]]
#                    left_eye = image[boxs[1][0]:boxs[1][0]+boxs[1][2],boxs[1][1]:boxs[1][1]+boxs[1][3],:]
#                    right_eye = face[boxs[1][0]:boxs[1][0]+boxs[1][2],boxs[1][1]:boxs[1][1]+boxs[1][3]]
                    #画图
                    for i,[bx,by,bw,bh] in enumerate(self.boxs):
                        if i == 1:
                            left_eye = image[by:by+bh,bx:bx+bw]
                        cv.rectangle(image,(bx,by),(bx+bw,by+bh),(254,0,255),1)
                    self.cls.run([left_eye])
                if self.results[0] == 1:
                    self.open_time += 1
                    self.eye_label.setText("睁眼")
##                    print('睁眼')
                if self.results[0] == 0:
                    self.close_time += 1
                    self.eye_label.setText("闭眼")
#                    print('闭眼')
                self.start += 1
                if self.start%30 == 0:
                    self.convert_result()
                if self.start == 210:
                    self.close_time = 0
                    self.open_time = 0
                    self.start = 0
            return image
        
        if self.b3.isChecked():
            return image
        
    def eye_list(self,boxs):
        '''
        box:[face_box,left_eye_box,right_eye_box]
        '''
        self.boxs = boxs
    
    def cls_result(self,results):
        self.results = results
        
        
    def convert_result(self):
        '''
        判断疲劳函数
        '''
        if self.open_time != 0:
            if self.close_time/self.open_time >= 2:
                self.result.setText('重度疲劳')
                self.spk.run('警告！处于重度疲劳状态')
#            QMessageBox.Warning(self,'警告','检测到疲劳驾驶')
            if self.close_time/self.open_time >= 1.5:
                self.result.setText('中度疲劳')
            if self.close_time/self.open_time >= 0.8:
                self.result.setText('轻度疲劳')
            if self.close_time/self.open_time <0.8:
                self.result.setText('正常驾驶')
        else:
#             self.result.setText('重度疲劳')
             self.spk.run('危险！  目前十分疲劳')

if __name__ == '__main__':
    ap = QApplication(sys.argv)
    m = MyFrame()
    m.show()
    sys.exit(ap.exec_())