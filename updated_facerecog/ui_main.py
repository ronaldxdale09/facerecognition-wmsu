# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainksTpOV.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1533, 857)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 40))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.frame_toggle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color:rgb(43, 43, 43)")

        self.verticalLayout_2.addWidget(self.Btn_Toggle)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_top)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(570, 10, 401, 21))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"COLOR:WHITE;")

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setStyleSheet(u"background-color:white;")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(150, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_page_1 = QPushButton(self.frame_top_menus)
        self.btn_page_1.setObjectName(u"btn_page_1")
        self.btn_page_1.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(11)
        self.btn_page_1.setFont(font1)
        self.btn_page_1.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_1)

        self.btn_page_2 = QPushButton(self.frame_top_menus)
        self.btn_page_2.setObjectName(u"btn_page_2")
        self.btn_page_2.setMinimumSize(QSize(0, 40))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        self.btn_page_2.setFont(font2)
        self.btn_page_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_2)

        self.btn_page_3 = QPushButton(self.frame_top_menus)
        self.btn_page_3.setObjectName(u"btn_page_3")
        self.btn_page_3.setMinimumSize(QSize(0, 40))
        self.btn_page_3.setFont(font2)
        self.btn_page_3.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_3)

        self.btn_page_4 = QPushButton(self.frame_top_menus)
        self.btn_page_4.setObjectName(u"btn_page_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_page_4.sizePolicy().hasHeightForWidth())
        self.btn_page_4.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(14)
        self.btn_page_4.setFont(font3)
        self.btn_page_4.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_4)


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QCalendarWidget QAbstractItemView\n"
"{\n"
"background-color: rgb(192,192,192); /* \u0446\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u0442\u0435\u043a\u0443\u0449\u0435\u0433\u043e \u043c\u0435\u0441\u044f\u0446\u0430 */\n"
"selection-background-color: yellow; /* \u0446\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0433\u043e \u0434\u043d\u044f */\n"
"selection-color: black; /* \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0433\u043e \u0434\u043d\u044f */\n"
"}")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setMinimumSize(QSize(1240, 0))
        self.horizontalLayout_3 = QHBoxLayout(self.page_1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox = QGroupBox(self.page_1)
        self.groupBox.setObjectName(u"groupBox")
        self.calendarWidget = QCalendarWidget(self.groupBox)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(680, 220, 551, 231))
        font4 = QFont()
        font4.setPointSize(6)
        self.calendarWidget.setFont(font4)
        self.calendarWidget.setStyleSheet(u"\n"
"  /*Tool button styles */\n"
"QCalendarWidget QToolButton {\n"
"\n"
"\n"
"height:40px;\n"
"width:150px;\n"
"color:white;\n"
"font-size:10px;\n"
"icon-size:56px,56px;\n"
"background-color:rgb(204, 65, 68);\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"  /* header row */\n"
"QCalendarWidget  QWidget{\n"
"\n"
"alternate-background-color:rgb(128,128,128)\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"  /*normal days */\n"
"QCalendarWidget QAbstractItemView:enabled {\n"
"\n"
"\n"
"font-size:18px;\n"
"color:rgb(180,180,180);\n"
"background-color:white;\n"
"selection-background-color:rgb(255, 69, 87);\n"
"selection-color:white;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"  /*Tool button styles */\n"
"QCalendarWidget QToolButton {\n"
" \n"
" \n"
"height:25px;\n"
"width:150px;\n"
"color:white;\n"
"font-size:20px;\n"
"icon-size:20px,20px;\n"
" \n"
" \n"
" \n"
"}\n"
" \n"
" \n"
" \n"
"  /* header row */\n"
"QCalendarWidget  QWidget{\n"
" \n"
"alternate-background-color:rgb(128,128,128)\n"
" \n"
" \n"
" \n"
"}\n"
" \n"
" \n"
"  /*normal days */\n"
""
                        "QCalendarWidget QAbstractItemView:enabled {\n"
" \n"
" \n"
"font-size:14px;\n"
"color:rgb(180,180,180);\n"
"background-color:white;\n"
"\n"
" \n"
" }\n"
" ")
        self.btnFaceRec_2 = QPushButton(self.groupBox)
        self.btnFaceRec_2.setObjectName(u"btnFaceRec_2")
        self.btnFaceRec_2.setGeometry(QRect(160, 700, 291, 51))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(14)
        font5.setBold(True)
        font5.setWeight(75)
        self.btnFaceRec_2.setFont(font5)
        self.btnFaceRec_2.setStyleSheet(u"QPushButton{\n"
"color:White;\n"
"border-radius: 50px;\n"
"background-color:rgb(204, 65, 68);\n"
"}")
        self.tableWidget = QTableWidget(self.groupBox)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 140, 621, 541))
        self.tableWidget.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(247, 247, 247);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
""
                        "}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"	font: 75 10pt \"Segoe UI\";\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(204, 65, 68);\n"
"	padding: 3px;\n"
"	color:white;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.gridLayoutWidget_2 = QWidget(self.groupBox)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 20, 641, 125))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.knownFaceNo = QLabel(self.gridLayoutWidget_2)
        self.knownFaceNo.setObjectName(u"knownFaceNo")
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(36)
        font6.setBold(True)
        font6.setWeight(75)
        self.knownFaceNo.setFont(font6)
        self.knownFaceNo.setFrameShape(QFrame.Box)
        self.knownFaceNo.setFrameShadow(QFrame.Plain)
        self.knownFaceNo.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.knownFaceNo, 0, 0, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font5)
        self.label_7.setFrameShape(QFrame.Box)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)

        self.frame_6 = QFrame(self.groupBox)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(680, 20, 551, 191))
        self.frame_6.setFrameShape(QFrame.Box)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_6.setLineWidth(3)
        self.detectedFace = QLabel(self.frame_6)
        self.detectedFace.setObjectName(u"detectedFace")
        self.detectedFace.setGeometry(QRect(30, 30, 161, 141))
        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(200, 20, 51, 21))
        font7 = QFont()
        font7.setPointSize(12)
        self.label_8.setFont(font7)
        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(200, 50, 51, 21))
        self.label_9.setFont(font7)
        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(200, 80, 51, 21))
        self.label_11.setFont(font7)
        self.label_24 = QLabel(self.frame_6)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(200, 110, 51, 21))
        self.label_24.setFont(font7)
        self.detectedName = QLabel(self.frame_6)
        self.detectedName.setObjectName(u"detectedName")
        self.detectedName.setGeometry(QRect(260, 20, 271, 21))
        self.detectedName.setFont(font7)
        self.detectedTime = QLabel(self.frame_6)
        self.detectedTime.setObjectName(u"detectedTime")
        self.detectedTime.setGeometry(QRect(260, 50, 271, 21))
        self.detectedTime.setFont(font7)
        self.DetectedType = QLabel(self.frame_6)
        self.DetectedType.setObjectName(u"DetectedType")
        self.DetectedType.setGeometry(QRect(260, 80, 271, 21))
        self.DetectedType.setFont(font7)
        self.detectedDate = QLabel(self.frame_6)
        self.detectedDate.setObjectName(u"detectedDate")
        self.detectedDate.setGeometry(QRect(260, 110, 211, 21))
        self.detectedDate.setFont(font7)
        self.pointEntry = QLabel(self.frame_6)
        self.pointEntry.setObjectName(u"pointEntry")
        self.pointEntry.setGeometry(QRect(260, 150, 201, 21))
        self.pointEntry.setFont(font7)
        self.label_43 = QLabel(self.frame_6)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(200, 150, 51, 21))
        self.label_43.setFont(font7)
        self.frame_14 = QFrame(self.groupBox)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(680, 470, 561, 191))
        self.frame_14.setFrameShape(QFrame.Box)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.frame_14.setLineWidth(3)
        self.frame_5 = QFrame(self.frame_14)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(20, 30, 191, 41))
        self.frame_5.setStyleSheet(u"background-color:rgb(204, 65, 68);\n"
"border-radius:10px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.videorecord = QCheckBox(self.frame_5)
        self.videorecord.setObjectName(u"videorecord")
        self.videorecord.setGeometry(QRect(0, 10, 181, 21))
        self.videorecord.setFont(font)
        self.videorecord.setStyleSheet(u"QCheckBox{\n"
"color:white;}\n"
"QCheckBox::indicator{\n"
"                               width :30px;\n"
"                               height :30px;\n"
"\n"
"                               }\n"
"                               QCheckBox::indicator:unchecked:pressed\n"
"                               {\n"
"                               background-color : green;\n"
"                               }\n"
"")
        self.btnFaceRec = QPushButton(self.frame_14)
        self.btnFaceRec.setObjectName(u"btnFaceRec")
        self.btnFaceRec.setGeometry(QRect(130, 90, 321, 81))
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(18)
        font8.setBold(True)
        font8.setWeight(75)
        self.btnFaceRec.setFont(font8)
        self.btnFaceRec.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color:rgb(204, 65, 68);\n"
"	color:white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(204, 35, 72);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.frame_11 = QFrame(self.frame_14)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(220, 30, 331, 41))
        self.frame_11.setStyleSheet(u"background-color:rgb(204, 65, 68);\n"
"border-radius:10px;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.unauthorizedNotif = QCheckBox(self.frame_11)
        self.unauthorizedNotif.setObjectName(u"unauthorizedNotif")
        self.unauthorizedNotif.setGeometry(QRect(10, 10, 311, 21))
        font9 = QFont()
        font9.setFamily(u"Segoe UI")
        font9.setPointSize(11)
        font9.setBold(True)
        font9.setWeight(75)
        self.unauthorizedNotif.setFont(font9)
        self.unauthorizedNotif.setStyleSheet(u"QCheckBox{\n"
"color:white;}\n"
"QCheckBox::indicator{\n"
"                               width :30px;\n"
"                               height :30px;\n"
"\n"
"                               }\n"
"                               QCheckBox::indicator:unchecked:pressed\n"
"                               {\n"
"                               background-color : green;\n"
"                               }\n"
"")
        self.unauthorizedNotif.setChecked(False)
        self.label_35 = QLabel(self.groupBox)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(780, 750, 851, 21))
        self.label_35.setFont(font2)
        self.label_35.setStyleSheet(u"color: rgb(154, 154, 154)")
        self.frame_14.raise_()
        self.calendarWidget.raise_()
        self.btnFaceRec_2.raise_()
        self.tableWidget.raise_()
        self.gridLayoutWidget_2.raise_()
        self.frame_6.raise_()
        self.label_35.raise_()

        self.horizontalLayout_3.addWidget(self.groupBox)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tabWidget = QTabWidget(self.page_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setFont(font8)
        self.tabWidget.setStyleSheet(u"\n"
"QTabBar::tab {\n"
"	font: 75 15pt \"Segoe UI\";\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	padding: 3px;\n"
"	color:white;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"	margin-right:5px;\n"
"	\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"   background-color: rgb(204, 65, 68);\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background: rgb(204, 133, 134);\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    background: #999;\n"
"}\n"
"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.registerStudent = QPushButton(self.tab)
        self.registerStudent.setObjectName(u"registerStudent")
        self.registerStudent.setGeometry(QRect(110, 550, 251, 81))
        self.registerStudent.setMinimumSize(QSize(150, 30))
        font10 = QFont()
        font10.setFamily(u"Segoe UI")
        font10.setPointSize(18)
        self.registerStudent.setFont(font10)
        self.registerStudent.setStyleSheet(u"QPushButton {\n"
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
        self.frame_3 = QFrame(self.tab)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 0, 1221, 51))
        self.frame_3.setStyleSheet(u"background-color:rgb(204, 65, 68);\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(410, 10, 451, 31))
        font11 = QFont()
        font11.setFamily(u"Segoe UI")
        font11.setPointSize(20)
        font11.setBold(True)
        font11.setWeight(75)
        self.label_12.setFont(font11)
        self.label_12.setStyleSheet(u"background-color:rgb(204, 65, 68);\n"
"color:white;")
        self.trainStudent = QPushButton(self.tab)
        self.trainStudent.setObjectName(u"trainStudent")
        self.trainStudent.setGeometry(QRect(420, 550, 211, 81))
        self.trainStudent.setMinimumSize(QSize(150, 30))
        self.trainStudent.setFont(font10)
        self.trainStudent.setStyleSheet(u"QPushButton {\n"
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
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 100, 691, 381))
        self.label_2.setStyleSheet(u"border-width: 3;\n"
"border-top-left-radius : 20;\n"
"border-style: solid;\n"
"border-color: rgb(204, 65, 68);\n"
"color:black;")
        self.label_14 = QLabel(self.tab)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(770, 100, 291, 381))
        self.label_14.setStyleSheet(u"background-color:rgb(204, 65, 68);\n"
"border-top-right-radius : 50px;\n"
"")
        self.label_14.setPixmap(QPixmap(u":/image/resource/borderimage.png"))
        self.gridLayoutWidget_3 = QWidget(self.tab)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(130, 140, 581, 281))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.studentName = QLineEdit(self.gridLayoutWidget_3)
        self.studentName.setObjectName(u"studentName")
        self.studentName.setMinimumSize(QSize(0, 30))
        self.studentName.setFont(font2)
        self.studentName.setStyleSheet(u"QLineEdit {\n"
"	background-color: WHITE;\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.studentName, 0, 1, 1, 1)

        self.studentBirth = QDateEdit(self.gridLayoutWidget_3)
        self.studentBirth.setObjectName(u"studentBirth")
        self.studentBirth.setFont(font3)
        self.studentBirth.setStyleSheet(u"	background-color:white;\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"	color:black;\n"
"	border: 2px solid rgb(27, 29, 35);")

        self.gridLayout_3.addWidget(self.studentBirth, 1, 1, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font10)

        self.gridLayout_3.addWidget(self.label_15, 0, 0, 1, 1)

        self.label_17 = QLabel(self.gridLayoutWidget_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font10)

        self.gridLayout_3.addWidget(self.label_17, 2, 0, 1, 1)

        self.studentGender = QComboBox(self.gridLayoutWidget_3)
        self.studentGender.addItem("")
        self.studentGender.addItem("")
        self.studentGender.setObjectName(u"studentGender")
        self.studentGender.setFont(font3)
        self.studentGender.setStyleSheet(u"QComboBox{\n"
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
"}")

        self.gridLayout_3.addWidget(self.studentGender, 2, 1, 1, 1)

        self.studentCourse = QComboBox(self.gridLayoutWidget_3)
        self.studentCourse.addItem("")
        self.studentCourse.addItem("")
        self.studentCourse.addItem("")
        self.studentCourse.addItem("")
        self.studentCourse.setObjectName(u"studentCourse")
        self.studentCourse.setFont(font3)
        self.studentCourse.setStyleSheet(u"QComboBox{\n"
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
"}")

        self.gridLayout_3.addWidget(self.studentCourse, 5, 1, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font10)

        self.gridLayout_3.addWidget(self.label_16, 1, 0, 1, 1)

        self.studentCollege = QComboBox(self.gridLayoutWidget_3)
        self.studentCollege.addItem("")
        self.studentCollege.addItem("")
        self.studentCollege.addItem("")
        self.studentCollege.addItem("")
        self.studentCollege.setObjectName(u"studentCollege")
        self.studentCollege.setFont(font3)
        self.studentCollege.setStyleSheet(u"QComboBox{\n"
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
"}")

        self.gridLayout_3.addWidget(self.studentCollege, 4, 1, 1, 1)

        self.label_18 = QLabel(self.gridLayoutWidget_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font10)

        self.gridLayout_3.addWidget(self.label_18, 5, 0, 1, 1)

        self.label_41 = QLabel(self.gridLayoutWidget_3)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font10)

        self.gridLayout_3.addWidget(self.label_41, 4, 0, 1, 1)

        self.studentError = QLabel(self.tab)
        self.studentError.setObjectName(u"studentError")
        self.studentError.setGeometry(QRect(90, 490, 641, 41))
        self.studentError.setFont(font3)
        self.studentError.setStyleSheet(u"color: red;")
        self.imageLabel = QLabel(self.tab)
        self.imageLabel.setObjectName(u"imageLabel")
        self.imageLabel.setGeometry(QRect(820, 120, 191, 221))
        self.registeredName = QLabel(self.tab)
        self.registeredName.setObjectName(u"registeredName")
        self.registeredName.setGeometry(QRect(790, 360, 221, 21))
        self.registeredName.setFont(font7)
        self.registeredName.setStyleSheet(u"background-color:rgb(204, 65, 68);\n"
"color:white;")
        self.registeredGender = QLabel(self.tab)
        self.registeredGender.setObjectName(u"registeredGender")
        self.registeredGender.setGeometry(QRect(790, 390, 221, 21))
        self.registeredGender.setFont(font7)
        self.registeredGender.setStyleSheet(u"background-color:rgb(204, 65, 68);\n"
"color:white;")
        self.registeredCourse = QLabel(self.tab)
        self.registeredCourse.setObjectName(u"registeredCourse")
        self.registeredCourse.setGeometry(QRect(790, 420, 221, 21))
        self.registeredCourse.setFont(font7)
        self.registeredCourse.setStyleSheet(u"background-color:rgb(204, 65, 68);\n"
"color:white;")
        self.label_36 = QLabel(self.tab)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(10, 710, 851, 21))
        self.label_36.setFont(font2)
        self.label_36.setStyleSheet(u"color: rgb(154, 154, 154)")
        self.tabWidget.addTab(self.tab, "")
        self.label_2.raise_()
        self.registerStudent.raise_()
        self.frame_3.raise_()
        self.trainStudent.raise_()
        self.label_14.raise_()
        self.gridLayoutWidget_3.raise_()
        self.studentError.raise_()
        self.imageLabel.raise_()
        self.registeredName.raise_()
        self.registeredGender.raise_()
        self.registeredCourse.raise_()
        self.label_36.raise_()
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.frame_4 = QFrame(self.tab_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 0, 1221, 51))
        self.frame_4.setStyleSheet(u"background-color:rgb(204, 65, 68);\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_13 = QLabel(self.frame_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(370, 10, 511, 31))
        self.label_13.setFont(font11)
        self.label_13.setStyleSheet(u"background-color:rgb(204, 65, 68);\n"
"color:white;")
        self.label_19 = QLabel(self.tab_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(210, 100, 691, 381))
        self.label_19.setStyleSheet(u"border-width: 3;\n"
"border-top-left-radius : 20;\n"
"border-style: solid;\n"
"border-color: rgb(204, 65, 68);\n"
"color:black;")
        self.employeeRegister = QPushButton(self.tab_2)
        self.employeeRegister.setObjectName(u"employeeRegister")
        self.employeeRegister.setGeometry(QRect(280, 510, 251, 81))
        self.employeeRegister.setMinimumSize(QSize(150, 30))
        self.employeeRegister.setFont(font10)
        self.employeeRegister.setStyleSheet(u"QPushButton {\n"
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
        self.employeeTrain = QPushButton(self.tab_2)
        self.employeeTrain.setObjectName(u"employeeTrain")
        self.employeeTrain.setGeometry(QRect(550, 510, 211, 81))
        self.employeeTrain.setMinimumSize(QSize(150, 30))
        self.employeeTrain.setFont(font10)
        self.employeeTrain.setStyleSheet(u"QPushButton {\n"
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
        self.gridLayoutWidget_4 = QWidget(self.tab_2)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(270, 140, 590, 313))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.employeePosition = QComboBox(self.gridLayoutWidget_4)
        self.employeePosition.addItem("")
        self.employeePosition.addItem("")
        self.employeePosition.addItem("")
        self.employeePosition.setObjectName(u"employeePosition")
        self.employeePosition.setFont(font3)
        self.employeePosition.setStyleSheet(u"QComboBox{\n"
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
"}")

        self.gridLayout_4.addWidget(self.employeePosition, 5, 1, 1, 1)

        self.employeeName = QLineEdit(self.gridLayoutWidget_4)
        self.employeeName.setObjectName(u"employeeName")
        self.employeeName.setMinimumSize(QSize(0, 30))
        self.employeeName.setFont(font2)
        self.employeeName.setStyleSheet(u"QLineEdit {\n"
"	background-color: WHITE;\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.employeeName, 0, 1, 1, 1)

        self.label_21 = QLabel(self.gridLayoutWidget_4)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font10)

        self.gridLayout_4.addWidget(self.label_21, 1, 0, 1, 1)

        self.label_25 = QLabel(self.gridLayoutWidget_4)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font10)

        self.gridLayout_4.addWidget(self.label_25, 4, 0, 1, 1)

        self.label_26 = QLabel(self.gridLayoutWidget_4)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font10)

        self.gridLayout_4.addWidget(self.label_26, 5, 0, 1, 1)

        self.employeeType = QComboBox(self.gridLayoutWidget_4)
        self.employeeType.addItem("")
        self.employeeType.addItem("")
        self.employeeType.setObjectName(u"employeeType")
        self.employeeType.setFont(font3)
        self.employeeType.setStyleSheet(u"QComboBox{\n"
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
"}")

        self.gridLayout_4.addWidget(self.employeeType, 4, 1, 1, 1)

        self.label_20 = QLabel(self.gridLayoutWidget_4)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font10)

        self.gridLayout_4.addWidget(self.label_20, 0, 0, 1, 1)

        self.label_22 = QLabel(self.gridLayoutWidget_4)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font10)

        self.gridLayout_4.addWidget(self.label_22, 2, 0, 1, 1)

        self.employeeGender = QComboBox(self.gridLayoutWidget_4)
        self.employeeGender.addItem("")
        self.employeeGender.addItem("")
        self.employeeGender.setObjectName(u"employeeGender")
        self.employeeGender.setFont(font3)
        self.employeeGender.setStyleSheet(u"QComboBox{\n"
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
"}")

        self.gridLayout_4.addWidget(self.employeeGender, 2, 1, 1, 1)

        self.label_23 = QLabel(self.gridLayoutWidget_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font10)

        self.gridLayout_4.addWidget(self.label_23, 3, 0, 1, 1)

        self.employeeDepartment = QComboBox(self.gridLayoutWidget_4)
        self.employeeDepartment.addItem("")
        self.employeeDepartment.addItem("")
        self.employeeDepartment.addItem("")
        self.employeeDepartment.addItem("")
        self.employeeDepartment.setObjectName(u"employeeDepartment")
        self.employeeDepartment.setFont(font3)
        self.employeeDepartment.setStyleSheet(u"QComboBox{\n"
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
"}")

        self.gridLayout_4.addWidget(self.employeeDepartment, 3, 1, 1, 1)

        self.employeeBirthdate = QDateEdit(self.gridLayoutWidget_4)
        self.employeeBirthdate.setObjectName(u"employeeBirthdate")
        self.employeeBirthdate.setFont(font3)
        self.employeeBirthdate.setStyleSheet(u"	background-color:white;\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"	color:black;\n"
"	border: 2px solid rgb(27, 29, 35);")

        self.gridLayout_4.addWidget(self.employeeBirthdate, 1, 1, 1, 1)

        self.imageLabel_employee = QLabel(self.tab_2)
        self.imageLabel_employee.setObjectName(u"imageLabel_employee")
        self.imageLabel_employee.setGeometry(QRect(950, 120, 191, 221))
        self.label_38 = QLabel(self.tab_2)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(900, 100, 291, 381))
        self.label_38.setStyleSheet(u"background-color:rgb(204, 65, 68);\n"
"border-top-right-radius : 50px;\n"
"")
        self.label_38.setPixmap(QPixmap(u":/image/resource/borderimage.png"))
        self.tabWidget.addTab(self.tab_2, "")
        self.label_38.raise_()
        self.frame_4.raise_()
        self.label_19.raise_()
        self.employeeRegister.raise_()
        self.employeeTrain.raise_()
        self.gridLayoutWidget_4.raise_()
        self.imageLabel_employee.raise_()

        self.verticalLayout_6.addWidget(self.tabWidget)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_8 = QVBoxLayout(self.page_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_7 = QFrame(self.page_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.exportVisitor = QPushButton(self.frame_7)
        self.exportVisitor.setObjectName(u"exportVisitor")
        self.exportVisitor.setGeometry(QRect(500, 590, 291, 51))
        self.exportVisitor.setFont(font5)
        self.exportVisitor.setStyleSheet(u"QPushButton{\n"
"color:White;\n"
"border-radius: 50px;\n"
"background-color:rgb(204, 65, 68);\n"
"}")
        self.frame_15 = QFrame(self.frame_7)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(150, 40, 931, 41))
        self.frame_15.setStyleSheet(u"background-color:rgb(204, 65, 68);\n"
"border-radius:10px;")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.label_33 = QLabel(self.frame_15)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(380, 10, 351, 21))
        font12 = QFont()
        font12.setFamily(u"Segoe UI")
        font12.setPointSize(16)
        font12.setBold(True)
        font12.setWeight(75)
        self.label_33.setFont(font12)
        self.label_33.setStyleSheet(u"background-color:rgb(204, 65, 68);\n"
"color:white;")
        self.label_37 = QLabel(self.frame_7)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(10, 750, 851, 21))
        self.label_37.setFont(font2)
        self.label_37.setStyleSheet(u"color: rgb(154, 154, 154)")
        self.visitorTable = QTableWidget(self.frame_7)
        if (self.visitorTable.columnCount() < 4):
            self.visitorTable.setColumnCount(4)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.visitorTable.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.visitorTable.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.visitorTable.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.visitorTable.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        self.visitorTable.setObjectName(u"visitorTable")
        self.visitorTable.setGeometry(QRect(140, 90, 951, 471))
        self.visitorTable.setLayoutDirection(Qt.LeftToRight)
        self.visitorTable.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(247, 247, 247);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
""
                        "}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"	font: 75 10pt \"Segoe UI\";\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(204, 65, 68);\n"
"	padding: 3px;\n"
"	color:white;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")

        self.verticalLayout_8.addWidget(self.frame_7)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.frame_2 = QFrame(self.page_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 30, 571, 41))
        self.frame_2.setStyleSheet(u"background-color:rgb(204, 65, 68);\n"
"border-radius:10px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(120, 10, 421, 21))
        self.label_10.setFont(font12)
        self.label_10.setStyleSheet(u"background-color:rgb(204, 65, 68);\n"
"color:white;")
        self.defaultFaceSettings = QPushButton(self.page_4)
        self.defaultFaceSettings.setObjectName(u"defaultFaceSettings")
        self.defaultFaceSettings.setGeometry(QRect(580, 640, 201, 61))
        self.defaultFaceSettings.setFont(font1)
        self.defaultFaceSettings.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color:rgb(204, 65, 68);\n"
"	color:white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(204, 35, 72);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.frame = QFrame(self.page_4)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 70, 571, 151))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(3)
        self.gridLayoutWidget = QWidget(self.frame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 20, 521, 121))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color:black;")

        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: black;")

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.confidence = QLineEdit(self.gridLayoutWidget)
        self.confidence.setObjectName(u"confidence")
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.confidence.sizePolicy().hasHeightForWidth())
        self.confidence.setSizePolicy(sizePolicy2)
        self.confidence.setMinimumSize(QSize(0, 30))
        font13 = QFont()
        font13.setFamily(u"Segoe UI")
        font13.setPointSize(16)
        self.confidence.setFont(font13)
        self.confidence.setStyleSheet(u"	background-color:rgb(204, 65, 68);\n"
"	border-radius: 5px;\n"
"	color:white;")

        self.gridLayout.addWidget(self.confidence, 0, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: black;")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.scale = QLineEdit(self.gridLayoutWidget)
        self.scale.setObjectName(u"scale")
        sizePolicy2.setHeightForWidth(self.scale.sizePolicy().hasHeightForWidth())
        self.scale.setSizePolicy(sizePolicy2)
        self.scale.setMinimumSize(QSize(0, 30))
        self.scale.setFont(font13)
        self.scale.setStyleSheet(u"	background-color:rgb(204, 65, 68);\n"
"	border-radius: 5px;\n"
"	color:white;")

        self.gridLayout.addWidget(self.scale, 0, 3, 1, 1)

        self.neigh = QLineEdit(self.gridLayoutWidget)
        self.neigh.setObjectName(u"neigh")
        sizePolicy2.setHeightForWidth(self.neigh.sizePolicy().hasHeightForWidth())
        self.neigh.setSizePolicy(sizePolicy2)
        self.neigh.setMinimumSize(QSize(0, 30))
        self.neigh.setFont(font13)
        self.neigh.setStyleSheet(u"	background-color:rgb(204, 65, 68);\n"
"	border-radius: 5px;\n"
"	color:white;")

        self.gridLayout.addWidget(self.neigh, 1, 1, 1, 1)

        self.frame_8 = QFrame(self.page_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(630, 30, 561, 41))
        self.frame_8.setStyleSheet(u"background-color:rgb(204, 65, 68);\n"
"border-radius:10px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.label_27 = QLabel(self.frame_8)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(120, 10, 421, 21))
        self.label_27.setFont(font12)
        self.label_27.setStyleSheet(u"background-color:rgb(204, 65, 68);\n"
"color:white;")
        self.frame_9 = QFrame(self.page_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(630, 70, 561, 191))
        self.frame_9.setFrameShape(QFrame.Box)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.frame_9.setLineWidth(3)
        self.gridLayoutWidget_5 = QWidget(self.frame_9)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(20, 20, 521, 121))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_5.setVerticalSpacing(5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_30 = QLabel(self.gridLayoutWidget_5)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font2)
        self.label_30.setStyleSheet(u"color: black;")

        self.gridLayout_5.addWidget(self.label_30, 0, 0, 1, 1)

        self.reg_scale = QLineEdit(self.gridLayoutWidget_5)
        self.reg_scale.setObjectName(u"reg_scale")
        sizePolicy2.setHeightForWidth(self.reg_scale.sizePolicy().hasHeightForWidth())
        self.reg_scale.setSizePolicy(sizePolicy2)
        self.reg_scale.setMinimumSize(QSize(0, 30))
        self.reg_scale.setFont(font13)
        self.reg_scale.setStyleSheet(u"	background-color:rgb(204, 65, 68);\n"
"	border-radius: 5px;\n"
"	color:white;")

        self.gridLayout_5.addWidget(self.reg_scale, 0, 3, 1, 1)

        self.label_29 = QLabel(self.gridLayoutWidget_5)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font2)
        self.label_29.setStyleSheet(u"color:black;")

        self.gridLayout_5.addWidget(self.label_29, 0, 2, 1, 1)

        self.reg_neigh = QLineEdit(self.gridLayoutWidget_5)
        self.reg_neigh.setObjectName(u"reg_neigh")
        sizePolicy2.setHeightForWidth(self.reg_neigh.sizePolicy().hasHeightForWidth())
        self.reg_neigh.setSizePolicy(sizePolicy2)
        self.reg_neigh.setMinimumSize(QSize(0, 30))
        self.reg_neigh.setFont(font13)
        self.reg_neigh.setStyleSheet(u"	background-color:rgb(204, 65, 68);\n"
"	border-radius: 5px;\n"
"	color:white;")

        self.gridLayout_5.addWidget(self.reg_neigh, 0, 1, 1, 1)

        self.label_40 = QLabel(self.gridLayoutWidget_5)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font2)
        self.label_40.setStyleSheet(u"color: black;")

        self.gridLayout_5.addWidget(self.label_40, 1, 0, 1, 1)

        self.registrationCamera_2 = QComboBox(self.gridLayoutWidget_5)
        self.registrationCamera_2.addItem("")
        self.registrationCamera_2.addItem("")
        self.registrationCamera_2.addItem("")
        self.registrationCamera_2.addItem("")
        self.registrationCamera_2.setObjectName(u"registrationCamera_2")
        self.registrationCamera_2.setFont(font7)
        self.registrationCamera_2.setStyleSheet(u"	background-color:rgb(204, 65, 68);\n"
"	border-radius: 5px;\n"
"	color:white;")

        self.gridLayout_5.addWidget(self.registrationCamera_2, 1, 1, 1, 1)

        self.frame_10 = QFrame(self.page_4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(20, 250, 561, 41))
        self.frame_10.setStyleSheet(u"background-color:rgb(204, 65, 68);\n"
"border-radius:10px;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.label_28 = QLabel(self.frame_10)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(200, 10, 111, 21))
        self.label_28.setFont(font12)
        self.label_28.setStyleSheet(u"background-color:rgb(204, 65, 68);\n"
"color:white;")
        self.frame_12 = QFrame(self.page_4)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(20, 300, 561, 181))
        self.frame_12.setFrameShape(QFrame.Box)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.frame_12.setLineWidth(3)
        self.enabledCamera = QComboBox(self.frame_12)
        self.enabledCamera.addItem("")
        self.enabledCamera.addItem("")
        self.enabledCamera.addItem("")
        self.enabledCamera.setObjectName(u"enabledCamera")
        self.enabledCamera.setGeometry(QRect(220, 20, 171, 31))
        self.enabledCamera.setFont(font7)
        self.enabledCamera.setStyleSheet(u"	background-color:rgb(204, 65, 68);\n"
"	border-radius: 5px;\n"
"	color:white;")
        self.label_31 = QLabel(self.frame_12)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(30, 20, 161, 32))
        self.label_31.setFont(font3)
        self.label_31.setStyleSheet(u"color: black;")
        self.label_39 = QLabel(self.frame_12)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(30, 70, 201, 32))
        self.label_39.setFont(font3)
        self.label_39.setStyleSheet(u"color: black;")
        self.registrationCamera = QComboBox(self.frame_12)
        self.registrationCamera.addItem("")
        self.registrationCamera.addItem("")
        self.registrationCamera.setObjectName(u"registrationCamera")
        self.registrationCamera.setGeometry(QRect(220, 70, 181, 31))
        self.registrationCamera.setFont(font7)
        self.registrationCamera.setStyleSheet(u"	background-color:rgb(204, 65, 68);\n"
"	border-radius: 5px;\n"
"	color:white;")
        self.label_42 = QLabel(self.frame_12)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(30, 120, 161, 32))
        self.label_42.setFont(font3)
        self.label_42.setStyleSheet(u"color: black;")
        self.entry = QComboBox(self.frame_12)
        self.entry.addItem("")
        self.entry.addItem("")
        self.entry.setObjectName(u"entry")
        self.entry.setGeometry(QRect(220, 120, 251, 31))
        self.entry.setFont(font7)
        self.entry.setStyleSheet(u"	background-color:rgb(204, 65, 68);\n"
"	border-radius: 5px;\n"
"	color:white;")
        self.frame_13 = QFrame(self.page_4)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(30, 510, 1301, 121))
        self.frame_13.setFrameShape(QFrame.Box)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.frame_13.setLineWidth(3)
        self.label = QLabel(self.frame_13)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 851, 21))
        self.label.setFont(font2)
        self.label_32 = QLabel(self.frame_13)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(20, 50, 881, 21))
        self.label_32.setFont(font2)
        self.label_34 = QLabel(self.page_4)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(0, 780, 851, 21))
        self.label_34.setFont(font2)
        self.label_34.setStyleSheet(u"color: rgb(154, 154, 154)")
        self.stackedWidget.addWidget(self.page_4)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WMSU Face Recognition System", None))
        self.Btn_Toggle.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"WMSU FACE RECOGNITION SYSTEM", None))
        self.btn_page_1.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_page_2.setText(QCoreApplication.translate("MainWindow", u"Register Face", None))
        self.btn_page_3.setText(QCoreApplication.translate("MainWindow", u"Visitors Log", None))
        self.btn_page_4.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.groupBox.setTitle("")
        self.btnFaceRec_2.setText(QCoreApplication.translate("MainWindow", u"VIEW ALL", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Time", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Match Score", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Entry", None));
        self.knownFaceNo.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"KNOWN FACE DETECTED", None))
        self.detectedFace.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Name: ", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Time :", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Type :", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Date :", None))
        self.detectedName.setText("")
        self.detectedTime.setText("")
        self.DetectedType.setText("")
        self.detectedDate.setText("")
        self.pointEntry.setText("")
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Entry:", None))
        self.videorecord.setText(QCoreApplication.translate("MainWindow", u"VIDEO RECORD", None))
        self.btnFaceRec.setText(QCoreApplication.translate("MainWindow", u"START RECOGNITION", None))
        self.unauthorizedNotif.setText(QCoreApplication.translate("MainWindow", u"ALERT UNAUTHORIZED ENTRY", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Developed by : Ronald Dale Fuentebella & Joshua Z. Habil", None))
        self.registerStudent.setText(QCoreApplication.translate("MainWindow", u"REGISTER", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"STUDENT FACE REGISTER", None))
        self.trainStudent.setText(QCoreApplication.translate("MainWindow", u"TRAIN", None))
        self.label_2.setText("")
        self.label_14.setText("")
        self.studentName.setText("")
        self.studentName.setPlaceholderText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Name : ", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Gender:", None))
        self.studentGender.setItemText(0, QCoreApplication.translate("MainWindow", u"Male", None))
        self.studentGender.setItemText(1, QCoreApplication.translate("MainWindow", u"Female", None))

        self.studentCourse.setItemText(0, QCoreApplication.translate("MainWindow", u"Computer Science", None))
        self.studentCourse.setItemText(1, QCoreApplication.translate("MainWindow", u"Information Technology", None))
        self.studentCourse.setItemText(2, QCoreApplication.translate("MainWindow", u"Accountancy", None))
        self.studentCourse.setItemText(3, QCoreApplication.translate("MainWindow", u"Education", None))

        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Birthdate:", None))
        self.studentCollege.setItemText(0, QCoreApplication.translate("MainWindow", u"Institute of Computer Studies", None))
        self.studentCollege.setItemText(1, QCoreApplication.translate("MainWindow", u"College of Engineering", None))
        self.studentCollege.setItemText(2, QCoreApplication.translate("MainWindow", u"College of Education", None))
        self.studentCollege.setItemText(3, QCoreApplication.translate("MainWindow", u"College of Nursing", None))

        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Course", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"College", None))
        self.studentError.setText("")
        self.imageLabel.setText("")
        self.registeredName.setText("")
        self.registeredGender.setText("")
        self.registeredCourse.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Developed by : Ronald Dale Fuentebella & Joshua Z. Habil", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"STUDENT", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"EMPLOYEE FACE REGISTER", None))
        self.label_19.setText("")
        self.employeeRegister.setText(QCoreApplication.translate("MainWindow", u"REGISTER", None))
        self.employeeTrain.setText(QCoreApplication.translate("MainWindow", u"TRAIN", None))
        self.employeePosition.setItemText(0, QCoreApplication.translate("MainWindow", u"Dean", None))
        self.employeePosition.setItemText(1, QCoreApplication.translate("MainWindow", u"Teacher", None))
        self.employeePosition.setItemText(2, QCoreApplication.translate("MainWindow", u"Janitor", None))

        self.employeeName.setText("")
        self.employeeName.setPlaceholderText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Birthdate:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Employee Type", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Position", None))
        self.employeeType.setItemText(0, QCoreApplication.translate("MainWindow", u"Faculty", None))
        self.employeeType.setItemText(1, QCoreApplication.translate("MainWindow", u"Staff", None))

        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Name : ", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Gender:", None))
        self.employeeGender.setItemText(0, QCoreApplication.translate("MainWindow", u"Male", None))
        self.employeeGender.setItemText(1, QCoreApplication.translate("MainWindow", u"Female", None))

        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Department", None))
        self.employeeDepartment.setItemText(0, QCoreApplication.translate("MainWindow", u"Institute of Computer Studies", None))
        self.employeeDepartment.setItemText(1, QCoreApplication.translate("MainWindow", u"College of Engineering", None))
        self.employeeDepartment.setItemText(2, QCoreApplication.translate("MainWindow", u"College of Education", None))
        self.employeeDepartment.setItemText(3, "")

        self.imageLabel_employee.setText("")
        self.label_38.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"EMPLOYEE", None))
        self.exportVisitor.setText(QCoreApplication.translate("MainWindow", u"EXPORT CSV", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"VISITORS LOG", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Developed by : Ronald Dale Fuentebella & Joshua Z. Habil", None))
        ___qtablewidgetitem6 = self.visitorTable.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem7 = self.visitorTable.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Time", None));
        ___qtablewidgetitem8 = self.visitorTable.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem9 = self.visitorTable.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Purpose", None));
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"FACE RECOGNITION SETTING", None))
        self.defaultFaceSettings.setText(QCoreApplication.translate("MainWindow", u"DEFAULT SETTINGS", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Scaling Factor", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Minimum Neighbor", None))
        self.confidence.setText(QCoreApplication.translate("MainWindow", u"75", None))
        self.confidence.setPlaceholderText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Minimum Confidence", None))
        self.scale.setText(QCoreApplication.translate("MainWindow", u"1.2", None))
        self.scale.setPlaceholderText("")
        self.neigh.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.neigh.setPlaceholderText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"FACE REGISTRATION SETTINGS", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Minimum Neighbor", None))
        self.reg_scale.setText(QCoreApplication.translate("MainWindow", u"1.2", None))
        self.reg_scale.setPlaceholderText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Scale Value", None))
        self.reg_neigh.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.reg_neigh.setPlaceholderText("")
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Training Image", None))
        self.registrationCamera_2.setItemText(0, QCoreApplication.translate("MainWindow", u"250", None))
        self.registrationCamera_2.setItemText(1, QCoreApplication.translate("MainWindow", u"200", None))
        self.registrationCamera_2.setItemText(2, QCoreApplication.translate("MainWindow", u"150", None))
        self.registrationCamera_2.setItemText(3, QCoreApplication.translate("MainWindow", u"100", None))

        self.label_28.setText(QCoreApplication.translate("MainWindow", u"CAMERA ", None))
        self.enabledCamera.setItemText(0, QCoreApplication.translate("MainWindow", u"Camera 1", None))
        self.enabledCamera.setItemText(1, QCoreApplication.translate("MainWindow", u"Camera 2", None))
        self.enabledCamera.setItemText(2, QCoreApplication.translate("MainWindow", u"Camera 1 & 2", None))

        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Face Recognition", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Registration Camera", None))
        self.registrationCamera.setItemText(0, QCoreApplication.translate("MainWindow", u"Camera 1", None))
        self.registrationCamera.setItemText(1, QCoreApplication.translate("MainWindow", u"Camera 2", None))

        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Entry Method", None))
        self.entry.setItemText(0, QCoreApplication.translate("MainWindow", u"Entrance Only", None))
        self.entry.setItemText(1, QCoreApplication.translate("MainWindow", u"Entrance & Exit", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"\u2666 Minimum Neighbor  :    Parameter specifying how many neighbors each candidate rectangle should have to retain it.", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u2666 Scaling Factor            :    Parameter specifying how much the image size is reduced  at each image scale.  ", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Developed by : Ronald Dale Fuentebella & Joshua Z. Habil", None))
    # retranslateUi

