# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_design.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 382)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.kwangwoon_btn = QtWidgets.QPushButton(self.centralwidget)
        self.kwangwoon_btn.setGeometry(QtCore.QRect(0, -10, 170, 170))
        self.kwangwoon_btn.setMaximumSize(QtCore.QSize(500, 500))
        self.kwangwoon_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/kwangwoon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kwangwoon_btn.setIcon(icon)
        self.kwangwoon_btn.setIconSize(QtCore.QSize(170, 170))
        self.kwangwoon_btn.setObjectName("kwangwoon_btn")
        self.google_btn = QtWidgets.QPushButton(self.centralwidget)
        self.google_btn.setGeometry(QtCore.QRect(170, 0, 170, 170))
        self.google_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/google.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.google_btn.setIcon(icon1)
        self.google_btn.setIconSize(QtCore.QSize(170, 170))
        self.google_btn.setObjectName("google_btn")
        self.naver_btn = QtWidgets.QPushButton(self.centralwidget)
        self.naver_btn.setGeometry(QtCore.QRect(0, 150, 170, 170))
        self.naver_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/naver.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.naver_btn.setIcon(icon2)
        self.naver_btn.setIconSize(QtCore.QSize(170, 170))
        self.naver_btn.setObjectName("naver_btn")
        self.youtube_btn = QtWidgets.QPushButton(self.centralwidget)
        self.youtube_btn.setGeometry(QtCore.QRect(170, 170, 170, 170))
        self.youtube_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/youtube.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.youtube_btn.setIcon(icon3)
        self.youtube_btn.setIconSize(QtCore.QSize(170, 170))
        self.youtube_btn.setObjectName("youtube_btn")
        self.excel_btn = QtWidgets.QPushButton(self.centralwidget)
        self.excel_btn.setGeometry(QtCore.QRect(0, 320, 131, 28))
        self.excel_btn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.excel_btn.setObjectName("excel_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.excel_btn.setText(_translate("MainWindow", "엑셀 파일 생성"))
import icon_rc
