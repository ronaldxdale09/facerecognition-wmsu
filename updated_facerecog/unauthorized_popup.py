# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'unauthorized_uifVifwE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(770, 388)
        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 0, 771, 51))
        self.frame_3.setStyleSheet(u"background-color:rgb(204, 65, 68);\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(210, 10, 451, 31))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"background-color:rgb(204, 65, 68);\n"
"color:white;")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 90, 191, 171))
        self.label.setStyleSheet(u"background:rgb(255, 255, 255)")
        self.label.setFrameShape(QFrame.Box)
        self.label.setFrameShadow(QFrame.Sunken)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(220, 90, 521, 171))
        self.frame.setStyleSheet(u"background-color:rgb(204, 65, 68);\n"
"border-top-right-radius : 50px;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 71, 21))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color:white;")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(220, 10, 71, 21))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color:white;")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 60, 71, 31))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color:white;")
        self.visitorName = QLineEdit(self.frame)
        self.visitorName.setObjectName(u"visitorName")
        self.visitorName.setGeometry(QRect(110, 60, 261, 31))
        self.visitorName.setMinimumSize(QSize(0, 30))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(12)
        self.visitorName.setFont(font3)
        self.visitorName.setStyleSheet(u"QLineEdit {\n"
"	background-color: WHITE;\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 100, 101, 31))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color:white;")
        self.visitorPurpose = QLineEdit(self.frame)
        self.visitorPurpose.setObjectName(u"visitorPurpose")
        self.visitorPurpose.setGeometry(QRect(110, 100, 261, 31))
        self.visitorPurpose.setMinimumSize(QSize(0, 30))
        self.visitorPurpose.setFont(font3)
        self.visitorPurpose.setStyleSheet(u"QLineEdit {\n"
"	background-color: WHITE;\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"")
        self.visitorTime = QLabel(self.frame)
        self.visitorTime.setObjectName(u"visitorTime")
        self.visitorTime.setGeometry(QRect(80, 10, 121, 21))
        self.visitorTime.setFont(font1)
        self.visitorTime.setStyleSheet(u"color:white;")
        self.visitorDate = QLabel(self.frame)
        self.visitorDate.setObjectName(u"visitorDate")
        self.visitorDate.setGeometry(QRect(270, 10, 141, 21))
        self.visitorDate.setFont(font1)
        self.visitorDate.setStyleSheet(u"color:white;")
        self.recordVisitor = QPushButton(Form)
        self.recordVisitor.setObjectName(u"recordVisitor")
        self.recordVisitor.setGeometry(QRect(180, 310, 181, 51))
        self.recordVisitor.setMinimumSize(QSize(150, 30))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(18)
        self.recordVisitor.setFont(font4)
        self.recordVisitor.setStyleSheet(u"QPushButton {\n"
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
        self.ignoreVisitor = QPushButton(Form)
        self.ignoreVisitor.setObjectName(u"ignoreVisitor")
        self.ignoreVisitor.setGeometry(QRect(410, 310, 181, 51))
        self.ignoreVisitor.setMinimumSize(QSize(150, 30))
        self.ignoreVisitor.setFont(font4)
        self.ignoreVisitor.setStyleSheet(u"QPushButton {\n"
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

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"UNAUTHORIZED DETECTED", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"Time :", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Date:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Name : ", None))
        self.visitorName.setText("")
        self.visitorName.setPlaceholderText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"Purpose", None))
        self.visitorPurpose.setText("")
        self.visitorPurpose.setPlaceholderText("")
        self.visitorTime.setText("")
        self.visitorDate.setText("")
        self.recordVisitor.setText(QCoreApplication.translate("Form", u"RECORD", None))
        self.ignoreVisitor.setText(QCoreApplication.translate("Form", u"IGNORE", None))
    # retranslateUi

