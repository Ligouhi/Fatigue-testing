#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 08:42:49 2018

@author: hui
"""

from PyQt5.QtWidgets import *
from ui.frame import *
from cls_utils import *

class MainWindow(QMainWindow):
    
    def __init__(self,parent = None):
        
        super(MainWindow,self).__init__(parent)
        self.initUI()
        
    def initUI(self):
        
        self.frame = MyFrame()
        self.setCentralWidget(self.frame)
        self.__screen__()
        self.center()
    
    def __screen__(self):
        
        screen = QDesktopWidget().screenGeometry()
        self.resize(screen.width(),screen.height())
        
    def center(self):
        
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width())/2,
                  (screen.height() - size.height())/2)
    
    
    
if __name__ == '__main__':
    
    ap = QApplication(sys.argv)
    m = MainWindow()
    m.show()
    sys.exit(ap.exec_()) 
        