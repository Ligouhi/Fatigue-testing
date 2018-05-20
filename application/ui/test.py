#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 17:22:22 2018

@author: hui
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import cv2 as cv
import sys
from cls_utils import build
import numpy as np

class Thread(QThread):
    
    singout = pyqtSignal(str)
    def __init__(self,parent = None):
        
        super(Thread,self).__init__(parent)
        self.model = None
    def build_(self):
        if not self.model:
            self.model = build()
    def run(self,images):
        if self.model:
            images = np.resize(images,(24,24,3))
            images = np.expand_dims(images,0)
            res = self.model.predict(images)
            self.singout.emit(str(res[0]))

class test(QMainWindow):
    
    def __init__(self,parent = None):
        
        super(test,self).__init__(parent)
        self.thread = Thread()
        self.thread.build_()
        self.thread.singout.connect(self.out_text)
        self.label = QLabel(self)
        self.timer_camera = QTimer(self)
        self.cap = cv.VideoCapture(0)
        self.timer_camera.timeout.connect(self.show_pic)
        self.timer_camera.start(10)
        self.setGeometry(300,300,500,500)
        
    def show_pic(self):
        
        ret,frame = self.cap.read()
        if ret:
            show = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
            self.thread.run(show)
            showImage = QImage(show.data,show.shape[1],show.shape[0],
                               QImage.Format_RGB888)
            self.label.setPixmap(QPixmap.fromImage(showImage))
            print(self.text)
            
    def out_text(self,text):
        self.text = text
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    t = test()
    t.show()
    sys.exit(app.exec_())
    t.cap.release()
    cv.destroyAllWindows()
    