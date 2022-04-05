# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gateNyXXtX.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class gate_select(object):
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
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(100, 70, 521, 171))
        self.frame.setStyleSheet(u"background-color:rgb(204, 65, 68);\n"
"border-top-right-radius : 50px;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(180, 30, 201, 51))
        font1 = QFont()
        font1.setPointSize(26)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color:white;")
        self.selectGate = QComboBox(self.frame)
        self.selectGate.addItem("")
        self.selectGate.addItem("")
        self.selectGate.addItem("")
        self.selectGate.addItem("")
        self.selectGate.addItem("")
        self.selectGate.addItem("")
        self.selectGate.setObjectName(u"selectGate")
        self.selectGate.setGeometry(QRect(130, 90, 241, 41))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(14)
        self.selectGate.setFont(font2)
        self.selectGate.setStyleSheet(u"QComboBox{\n"
"	background-color:white;\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"	color:black;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: white;\n"
"	background-color:rgb(204, 65, 68);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"	text-align: center;\n"
"}")
        self.startRec = QPushButton(Form)
        self.startRec.setObjectName(u"startRec")
        self.startRec.setGeometry(QRect(190, 260, 181, 51))
        self.startRec.setMinimumSize(QSize(150, 30))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(18)
        self.startRec.setFont(font3)
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
        self.cancelRec = QPushButton(Form)
        self.cancelRec.setObjectName(u"cancelRec")
        self.cancelRec.setGeometry(QRect(400, 260, 181, 51))
        self.cancelRec.setMinimumSize(QSize(150, 30))
        self.cancelRec.setFont(font3)
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

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"FACE RECOGNITION", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"GATE", None))
        self.selectGate.setItemText(0, QCoreApplication.translate("Form", u"Gate 1", None))
        self.selectGate.setItemText(1, QCoreApplication.translate("Form", u"Gate 2", None))
        self.selectGate.setItemText(2, QCoreApplication.translate("Form", u"Gate 3", None))
        self.selectGate.setItemText(3, QCoreApplication.translate("Form", u"Gate 4", None))
        self.selectGate.setItemText(4, QCoreApplication.translate("Form", u"Gate 5", None))
        self.selectGate.setItemText(5, QCoreApplication.translate("Form", u"Gate 6", None))

        self.startRec.setText(QCoreApplication.translate("Form", u"START", None))
        self.cancelRec.setText(QCoreApplication.translate("Form", u"CANCEL", None))
    # retranslateUi

