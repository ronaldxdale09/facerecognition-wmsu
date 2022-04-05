
import datetime
from os import name
import sys
import platform
from PyQt5.QtCore import QTimer, pyqtSlot
from PyQt5.QtWidgets import QApplication, QFileDialog, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap, QImage
import cv2
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import pandas as pd
from PyQt5.QtGui import QPixmap
from os.path import exists

import csv

# GUI FILE
from ui_main import Ui_MainWindow



# IMPORT FUNCTIONS
from ui_functions import *
from unauthorized_popup import Ui_Form

from gateSelect import gate_select
from popup_generate import generate



class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tableWidget.setColumnWidth(0,160)
        self.ui.visitorTable.setColumnWidth(0,160)



        # select Gate 
        self.window1 = QtWidgets.QMainWindow()
        self.gateselect =gate_select()
        self.gateselect.setupUi(self.window1)

        # REMINDER FOR GENERATE OF DATASET
        self.generate = QtWidgets.QMainWindow()
        self.generateNotice =generate()
        self.generateNotice.setupUi(self.generate)
       

        #UNAUTHORIZED 
        self.window = QtWidgets.QMainWindow()
        self.popup =Ui_Form()
        self.popup.setupUi(self.window)
        now = datetime.now()
        time = now.strftime('%I:%M:%S %p')
        date = now.strftime('%Y-%m-%d')





        #CREATE EXCEL FOR ATTENDANCE
        morningOrAfternoon = ''.join(x for x in time if x.isalpha())
        if morningOrAfternoon== 'AM':
             morningOrAfternoon ='MORNING'
        elif morningOrAfternoon =='PM':
            morningOrAfternoon ='AFTERNOON'


        CSV_PATH_ENTRANCE = 'csv_record/'+date+'-'+ morningOrAfternoon+'-Entrance.csv'
        CSV_PATH_EXIT = 'csv_record/'+date+'-'+ morningOrAfternoon+'-Exit.csv'
        file_exists1 = exists(CSV_PATH_ENTRANCE)
        file_exists2 = exists(CSV_PATH_EXIT)

        #THIS IS TO CREATE TWO SEPARATE CSV (1 FOR MORNING AND AFTERNOON)
        if file_exists1 == True and file_exists2== True:
            print('already Exist')
        else: 
            if morningOrAfternoon== 'AM':
                morningOrAfternoon ='MORNING'
            elif morningOrAfternoon =='PM':
                morningOrAfternoon ='AFTERNOON'
            with open(CSV_PATH_ENTRANCE, 'w', newline='') as file:
                writer = csv.writer(file)
            with open(CSV_PATH_EXIT, 'w', newline='') as file:
                writer = csv.writer(file)
        ###############################



        self.popup.recordVisitor.clicked.connect(lambda : self.recordUnauthorized(time,date))
        ######################
        pixmap = QtGui.QPixmap('avatar.png')
        self.ui.imageLabel.setPixmap(pixmap)
        self.ui.imageLabel.setScaledContents(True)

        #STUDENT REGISTRATION DATA
 
        self.loaddata()
        self.visitor_loadtable()
        #FUCNTION



        self.ui.registerStudent.clicked.connect(lambda: self.openStudentGenerate())
        self.ui.employeeRegister.clicked.connect(lambda: self.registerEmployee())
        self.ui.trainStudent.clicked.connect(lambda: Face_recog.train_classifier())
        self.ui.btnFaceRec.clicked.connect(lambda: self.openGatePrompt())
        self.ui.defaultFaceSettings.clicked.connect(lambda: self.facerecog_defaultSetting())
        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))

        ## PAGES
        ########################################################################

        # PAGE 1
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))

        # PAGE 2
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))

        # PAGE 3
        self.ui.btn_page_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))

        # PAGE 4
        self.ui.btn_page_4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##



     # TO BE USED LATER ON FOR CLEARING THE DATA ON WINDOWS AFTER TRAINING IS COMPLETE
    # def trainingStudent(self): 
    #     Face_recog.train_classifier(self)
    #     self.ui.studentName.setText("")       
    #     str(self.ui.studentBirth.date())

    def openGatePrompt(self):
        self.selectGate()
        self.gateselect.startRec.clicked.connect(lambda : self.LaunchFaceRecog())

    def openStudentGenerate(self):
        # self.generate.show()
        self.registerStudent()


    def LaunchFaceRecog(self): 
        self.window1.close()
        gate = self.gateselect.selectGate.currentText()
        print(gate)
        # FACE RECOGNITION SETTINGS
        scaleVal = float(self.ui.scale.text())
        neigh =  int(self.ui.neigh.text())
        confidence = int(self.ui.confidence.text())
        camera = self.ui.enabledCamera.currentText()

        entry = self.ui.entry.currentText()
        # check form of entry
        if entry == 'Entrance Only':
            selected_entry = 0
        if entry == 'Entrance & Exit':
            selected_entry = 1



        # check what camera to use
        if camera == 'Camera 1':
           selected_camera = 0
        if camera == 'Camera 2':
            selected_camera = 1
        if camera == 'Camera 1 & 2':
            selected_camera = 2

        #THIS CODE WILL ENABLE AND DISABLE VIDEO RECORD
        if self.ui.videorecord.isChecked():
            video_rec = 1
        else :
            video_rec = 0
        #THIS CODE WILL ENABLE AND DISABLE UNAUTHORIZED NOFICATION
        if self.ui.unauthorizedNotif.isChecked():
            notif = 1
        else :
            notif = 0
        
        Face_recog.start_faceRG(self,confidence,scaleVal,neigh,selected_camera,video_rec,notif,selected_entry,gate)
    
    def registerStudent(self): 
        # STUDENT REGISTRATION SETTINGS
        # self.generate.close()
        scaleVal = float(self.ui.reg_scale.text())
        neigh =  int(self.ui.reg_neigh.text())
        camera = self.ui.registrationCamera.currentText()
        if camera == 'Camera 1':
           selected_camera = 0
        if camera == 'Camera 2':
            selected_camera = 1
        Face_recog.generate_dataset(self,scaleVal,neigh,selected_camera)

    def registerEmployee(self): 
        # EMPLOYEE REGISTRATION SETTINGS
        scaleVal = float(self.ui.reg_scale.text())
        neigh =  int(self.ui.reg_neigh.text())
        camera = self.ui.registrationCamera.currentText()

        if camera == 'Camera 1':
           selected_camera = 0
        if camera == 'Camera 2':
            selected_camera = 1

        Face_recog.employee_generate(self,scaleVal,neigh,selected_camera)



    def facerecog_defaultSetting(self):
        self.ui.scale.setText("1.2")
        self.ui.neigh.setText("10")
        self.ui.confidence.setText("70")

    def loaddata(self):
        
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="face_attendancesystem"
        )

        cursor = mydb.cursor()    
        now = datetime.now()
        date = now.strftime('%Y-%m-%d') 
        cursor.execute("select * from attendance where date='"+str(date)+"'")
        person = cursor.fetchall()
        tablerow=0
        
       
      

        self.ui.tableWidget.setRowCount(40)
        for row in person:
            self.ui.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[3]))
            self.ui.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[4]))
            self.ui.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[5]))
            self.ui.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[6]))
            tablerow+=1
            self.ui.knownFaceNo.setText(str(tablerow))


    def visitor_loadtable(self):
        
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="face_attendancesystem"
        )

        cursor = mydb.cursor()    
        now = datetime.now()
        date = now.strftime('%Y-%m-%d') 
        cursor.execute("select * from unauthorized_detected")
        person = cursor.fetchall()
        tablerow=0
        
        self.ui.visitorTable.setWordWrap(True)

        self.ui.visitorTable.setRowCount(40)
        for row in person:
            self.ui.visitorTable.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.visitorTable.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.visitorTable.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[3]))
            self.ui.visitorTable.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[4]))
            tablerow+=1
# main
    def markAttendance(self,face_id,userType,name,confidence,college,academic,entrance,gate):
        # RECORD AM AND PM
        now = datetime.now()
        time = now.strftime('%I:%M %p')
        date = now.strftime('%Y-%m-%d')

        morningOrAfternoon = ''.join(x for x in time if x.isalpha())
        if morningOrAfternoon== 'AM':
             morningOrAfternoon ='MORNING'
        elif morningOrAfternoon =='PM':
            morningOrAfternoon ='AFTERNOON'


       
        CSV_PATH_ENTRANCE = 'csv_record/'+date+'-'+ morningOrAfternoon+'-Entrance.csv'
        CSV_PATH_EXIT = 'csv_record/'+date+'-'+ morningOrAfternoon+'-Exit.csv'

        if entrance=='Entrance':
            with open(CSV_PATH_ENTRANCE,'r+') as f:
                myDataList = f.readlines()
                nameList = []
                dateList = []
                for line in myDataList:
                    entry = line.split(',')
                    nameList.append(entry[0])
                    #dateList.append(entry[2])
                if name not in nameList :
                    f.writelines(f'{name},{time},{date},{userType},{confidence},{college}\n')
                    self.addAttendance(name,face_id,time,date,confidence,userType,college,academic,entrance,gate)
                    self.displayDetected(name,time,date,face_id,userType,entrance)
                    self.loaddata()
        elif entrance=='Exit':
            with open(CSV_PATH_EXIT,'r+') as f:
                myDataList = f.readlines()
                nameList = []
                dateList = []
                for line in myDataList:
                    entry = line.split(',')
                    nameList.append(entry[0])
                    #dateList.append(entry[2])
                if name not in nameList :
                    f.writelines(f'{name},{time},{date},{userType},{confidence},{college}\n')
                    self.addAttendance(name,face_id,time,date,confidence,userType,college,academic,entrance,gate)
                    self.displayDetected(name,time,date,face_id,userType,entrance)
                    self.loaddata()            
        

    def addAttendance(self,name,face_id,time,date,confidence,userType,college,acadYear,entry,gate):
        
        cursor = mydb.cursor()  
        sql= "insert into attendance (face_id,name,time,date,match_score,personType,college,academicYear,entry,gate) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (face_id,name,time,date,confidence,userType,college,acadYear,entry,gate)
        cursor.execute(sql,val)
        mydb.commit()  



    def displayDetected(self,name,time,date,face_id,userType,entrance):
        folder_name= 'face.'+str(face_id)+"."+userType
        profile = "datasets/"+str(folder_name)+"/user."+str(face_id)+"."+str(1)+".jpg"
        pixmap = QtGui.QPixmap(profile)
        self.ui.detectedFace.setPixmap(pixmap)
        self.ui.detectedFace.setScaledContents(True)
        ### information
        self.ui.detectedName.setText(name)
        self.ui.detectedTime.setText(time)
        self.ui.detectedDate.setText(date)
        self.ui.DetectedType.setText(userType)
        self.ui.pointEntry.setText(entrance)
        
    def unauthorizedDialog(self,time,date):
        self.window.show()
        self.popup.visitorTime.setText(time)
        self.popup.visitorDate.setText(date)
        self.popup.ignoreVisitor.clicked.connect(lambda: self.window.show())
    

    
    def selectGate(self):
        self.window1.show()



    def recordUnauthorized(self,time,date):
        cursor = mydb.cursor()  

        name = self.popup.visitorName.text()
        purpose = self.popup.visitorPurpose.text()
        sql= "insert into unauthorized_detected (name,time,date,purpose) values (%s,%s,%s,%s)"
        val = (name,time,date,purpose)
        cursor.execute(sql,val)
        mydb.commit()

        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("The Visitor info has been recorded")
        msgBox.setWindowTitle("NOTIFICATION")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')
            self.window.show()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
