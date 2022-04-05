# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'generatePGavzQ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class generate (object):
    def setupUi(self, generateNotice):
        if not generateNotice.objectName():
            generateNotice.setObjectName(u"generateNotice")
        generateNotice.resize(770, 433)
        self.frame_3 = QFrame(generateNotice)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 0, 771, 51))
        self.frame_3.setStyleSheet(u"background-color:rgb(204, 65, 68);\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(210, 0, 451, 41))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"background-color:rgb(204, 65, 68);\n"
"color:white;")
        self.startRec = QPushButton(generateNotice)
        self.startRec.setObjectName(u"startRec")
        self.startRec.setGeometry(QRect(150, 370, 181, 51))
        self.startRec.setMinimumSize(QSize(150, 30))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(18)
        self.startRec.setFont(font1)
        self.startRec.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(204, 65, 68);\n"
"	color:white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 52, 56);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.cancelRec = QPushButton(generateNotice)
        self.cancelRec.setObjectName(u"cancelRec")
        self.cancelRec.setGeometry(QRect(390, 370, 181, 51))
        self.cancelRec.setMinimumSize(QSize(150, 30))
        self.cancelRec.setFont(font1)
        self.cancelRec.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(204, 65, 68);\n"
"	color:white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(166, 52, 56);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"	color:white;\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.label = QLabel(generateNotice)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-110, -20, 951, 441))
        self.label.setStyleSheet(u"image: url(:/images/generate.png);\n"
"background-color:white;")
        self.label.raise_()
        self.frame_3.raise_()
        self.startRec.raise_()
        self.cancelRec.raise_()

        self.retranslateUi(generateNotice)

        QMetaObject.connectSlotsByName(generateNotice)
    # setupUi

    def retranslateUi(self, generateNotice):
        generateNotice.setWindowTitle(QCoreApplication.translate("generateNotice", u"Face Registration", None))
        self.label_12.setText(QCoreApplication.translate("generateNotice", u"FACE REGISTRATION", None))
        self.startRec.setText(QCoreApplication.translate("generateNotice", u"START", None))
        self.cancelRec.setText(QCoreApplication.translate("generateNotice", u"CANCEL", None))
        self.label.setText("")
    # retranslateUi

