#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tkinter import *


# In[3]:


import os
import cv2
import threading


# In[4]:


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import random
import win32com.client


# In[5]:


import pyautogui
import time


# In[6]:


#while True:
#    print("Current Mouse Position : ", pyautogui.position())
#   time.sleep(0.1)


# In[6]:


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    
    def initUI(self):
        self.setGeometry(50, 50, 1500, 900) #윈도우 창 크기 조절 setGeometry(x, y, width, height) 
        
        self.btnList= []
        self.btnTop = 100
        self.cnt = 0
        
        self.lbl = QLabel("버튼의 수 : ", self) #QLineEdit은 한 줄의 문자열을 입력하고 수정할 수 있도록 하는 위젯
        self.lbl.move(10, 10)
        
        self.txt = QLineEdit("", self)
        self.txt.move(10, self.lbl.height())
        
        self.btn = QPushButton("버튼 생성", self) #버튼 클릭에 따른 반응
        self.btn.resize(QSize(80, 25)) #버튼의 크기
        self.btn.move(0, self.lbl.height() + self.txt.height()) #버튼의 위치
        
        self.btn.clicked.connect(self.createBtn)
        
        self.btn1 = QPushButton("Clear", self)
        self.btn1.resize(QSize(80, 25))
        self.btn1.move(0, self.lbl.height() + self.txt.height() + 20)
        self.btn1.clicked.connect(self.btn1_clicked)
        
        self.show()
 
    def btn1_clicked(self):
        global running
        running = False
        os.system('cls')
        del self.btnList[:]
        
    def ClickMethod(self):
        excel = win32com.client.Dispatch("Excel.Application")
        excel.Visible = True
        wb = excel.Workbooks.Add()
        ws = wb.Worksheets("Sheet1")
        p=1
        q=1
        x_data = [[0 for j in range(100)] for i in range(self.cnt*self.cnt)]
        y_data = [[0 for j in range(100)] for i in range(self.cnt*self.cnt)]
        while True:
            x,y=pyautogui.position()
            for i in range(self.cnt*self.cnt):
                line1 = []
                line2 = []# 안쪽 리스트로 사용할 빈 리스트 생성
                for j in range(100):
                    line1.append(x)
                    line2.append(y)# 안쪽 리스트에 0 추가
                x_data.append(line1)
                y_data.append(line2)
            print(x_data)
            print(y_data)
            time.sleep(0.1)
            ws.Cells(p, 1).Value = x
            ws.Cells(q, 2).Value = y
            time.sleep(0.1)
            p += 1
            q += 1
        print(x_data)
        print(y_data)
        
        wb.SaveAs('C:\\Users\\이원빈\\Desktop\\test.xlsx')
        excel.Quit()
        
    def createBtn(self): #버튼 생성 함수
        del self.btnList[:]
        self.cnt = int(self.txt.text())
        Num = []
        for i in range(self.cnt*self.cnt):
            while True:
                num = random.randint(1, self.cnt*self.cnt)
                if(num in Num):
                    continue
                break
            Num.append(num)
            self.btnList.append(QPushButton(str(Num[i]), self))
            self.btnList[i].resize(QSize(1000/(self.cnt*self.cnt), 1000/(self.cnt*self.cnt))) #버튼 크기 조절하기
            self.btnList[i].move((i%self.cnt)*(500/self.cnt)+100, (i/self.cnt)*(500/self.cnt)+100) #버튼 위치 조정하기
            self.btnList[i].show() #버튼보여주는 함수
            self.btnList[i].clicked.connect(self.ClickMethod)
        
app = QApplication([])
ex = Example()
sys.exit(app.exec_())


# ### 3### 

# In[ ]:


def ClickMethod(self):
    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible = True
    wb = excel.Workbooks.Add()
    ws = wb.Worksheets("Sheet1")
    while True:
        ws.Cells(i, i).Value = pyautogui.position()
        time.sleep(0.1)


# In[ ]:


while True:
    print("Current Mouse Position : ", pyautogui.position())
time.sleep(0.1)


# In[ ]:


for i in range(self.cnt*self.cnt):
               while num in Num:
                   num = random.randint(1, self.cnt*self.cnt)
               if num not in Num:
                    Num.append(num)
               self.btnList.append(QPushButton(str(Num[i]), self))
               self.btnList[i].resize(QSize(1000/(self.cnt*self.cnt), 1000/(self.cnt*self.cnt))) #버튼 크기 조절하기
               self.btnList[i].move((i%self.cnt)*(500/self.cnt)+100, (i/self.cnt)*(500/self.cnt)+100) #버튼 위치 조정하기
               self.btnList[i].show() #버튼보여주는 함수


# In[7]:


#버튼 출력 윈도우창   

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    
    def initUI(self):
        self.setGeometry(50, 50, 1500, 900) #윈도우 창 크기 조절 setGeometry(x, y, width, height) 
        
        self.btnList= []
        self.btnTop = 100
        self.cnt = 0
        
        self.x_data = [[0 for j in range(10)] for i in range(0,(self.cnt*self.cnt)-1)] #x와 y 좌표값 저장하는 리스트
        self.y_data = [[0 for j in range(10)] for i in range(0,(self.cnt*self.cnt)-1)] 
        self.n = 0
        
        self.lbl = QLabel("버튼의 수 : ", self) #QLineEdit은 한 줄의 문자열을 입력하고 수정할 수 있도록 하는 위젯
        self.lbl.move(10, 10)
        
        self.txt = QLineEdit("", self)
        self.txt.move(10, self.lbl.height())
        
        self.btn = QPushButton("버튼 생성", self) #버튼 클릭에 따른 반응
        self.btn.resize(QSize(80, 25)) #버튼의 크기
        self.btn.move(0, self.lbl.height() + self.txt.height()) #버튼의 위치
        
        self.btn.clicked.connect(self.createBtn)
        
        self.show()
        
    def ClickMethod(self):
       
        for j in range(10):
            x,y=pyautogui.position()
            self.x_data[self.n][j]=x
            self.y_data[self.n][j]=y
            time.sleep(0.1)
    
        f=open('./Documents/mouse_data_test.csv','w',newline='')
        wr = csv.writer(f)
        for value in self.x_data:
            wr.writerow(value)#x좌표 저장
        self.n+=1
        
    def createBtn(self): #버튼 생성 함수
        self.cnt = int(self.txt.text())
        del self.btnList[:]
        Num = []
        for i in range(self.cnt*self.cnt):
            while True:
                num = random.randint(1, self.cnt*self.cnt)
                if(num in Num):
                    continue
                break
            Num.append(num)
            self.btnList.append(QPushButton(str(Num[i]), self))
            self.btnList[i].resize(QSize(1000/(self.cnt*self.cnt), 1000/(self.cnt*self.cnt))) #버튼 크기 조절하기
            self.btnList[i].move((i%self.cnt)*(500/self.cnt)+100, (i/self.cnt)*(500/self.cnt)+100) #버튼 위치 조정하기
            self.btnList[i].show() #버튼보여주는 함수
            self.btnList[i].clicked.connect(self.ClickMethod)
        
app = QApplication([])
ex = Example()
sys.exit(app.exec_())
f.close()


# In[ ]:




