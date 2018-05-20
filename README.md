# readme #
##项目依赖 ##
1. Anaconda 3.6
1. opencv 
1. numpy 
1. pyseeta 
1. PyQt5
1. tensorflow 1.7
1. win32com.client


如已下载3.5版本anaconda,其中内置Qt版本为PyQt4,需在anaconda navigator中的environment中下载PyQt5
## 如何使用 ##
在命令行中输入如下:


    python frame.py

## 配置环境 ##
### 安装第三方库pyseeta ###

详见 [https://github.com/TuXiaokang/pyseeta](https://github.com/TuXiaokang/pyseeta)
#### Download pyseeta ####
    git clone https://github.com/TuXiaokang/pyseeta.git
#### Download SeetaFaceEngine ####
    git submodule update --init --recursive
    Build SeetaFaceEngine dynamic library.
#### on unix  ####
    cd SeetaFaceEngine/
    mkdir Release; cd Release
    cmake ..
    make  
#### on windows  ####
    cd SeetaFaceEngine/
    mkdir Release; cd Release
    cmake -G "Visual Studio 14 2015 Win64" ..
    cmake --build . --config Release
### 其他依赖 ###
其他依赖可利用pip命令，如：
    pip install tensorflow == 1.7

## 实现功能 ##
1. 基于图像，利用眼部变化实时监测驾驶人员疲劳情况
1. 对疲劳分级，实行不同措施
1. 实现语音提醒


## 更新日志 ##
### v1.1 ###
实现语音接入
