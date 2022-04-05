
## ==> GUI FILE
import datetime
from PyQt5 import QtCore
from PyQt5.QtCore import QPropertyAnimation, QThread, Qt, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QTableWidgetItem
from main import * 
import cv2 # OpenCV
import PyQt5.QtCore  
from PyQt5.QtWidgets import QMessageBox
import cv2
import os
from PIL import Image #pip install pillow
import numpy as np    # pip install numpy
from datetime import datetime
import mysql.connector
from cv2 import VideoCapture, VideoWriter
from cv2 import VideoWriter_fourcc

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="face_attendancesystem"
        )

class UIFunctions(MainWindow):
######################################### MESSAGE POPUP ########################################
    def trainingMessage():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("The Training is successful")
        msgBox.setWindowTitle("NOTIFICATION")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')

    def generateMessage():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("The datasets has been generated")
        msgBox.setWindowTitle("NOTIFICATION")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')


    def toggleMenu(self, maxWidth, enable):
        if enable:

            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            # SET MAX WIDTH
            if width == 70:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()



#######################################################################
####################### FACE RECOGNITION FUNCTION #####################
#######################################################################
class Face_recog(MainWindow):

 
####################### DATASETS GENERATION #####################
    def generate_dataset(self):

        print('Generating Datasets Started')
        name = self.ui.studentName.text()       
        S_birthdate = str(self.ui.studentBirth.date())
        S_gender = self.ui.studentGender.currentText()
        S_course = self.ui.studentCourse.currentText()
        userType = 'Student'

        if len(name)==0  or len(S_gender)==0 or len(S_course)==0 :
            self.ui.studentError.setText("Please fill in all inputs...")
        else:

            connection = mydb.cursor()
            
            connection.execute("SELECT * from known_faces")
            myresult = connection.fetchall()

            id=1
            for x in myresult :
                id+=1

            sql= "insert into known_faces (face_id,name,course,birthdate,sex,userType) values (%s,%s,%s,%s,%s,%s)"
            val = (id,name,S_course,S_birthdate,S_gender,userType)


            face_classifier = cv2.CascadeClassifier("haarcascades\haarcascade_frontalface_default.xml")
            #If face is detected on camera it will capture it then convert into GRAYSCALE then finally cropped the frontal face
            def face_cropped(img):
                gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.5, 5)
                # scaling factor = 1.5
                # minimum neighbor = 5
                
                if faces == ():
                    return None
                for (x,y,w,h) in faces:
                    cropped_face = img[y:y+h,x:x+w]
                return cropped_face

            #INSERT DATA IN DATABASE
            connection.execute(sql,val)
            mydb.commit()    
            #####
            cap = cv2.VideoCapture(0)
            img_id = 0
            folder_name= 'face.'+str(id)+"."+userType
            os.makedirs("datasets/"+folder_name)
            while True:
                ret, frame = cap.read()
                if face_cropped(frame) is not None:
                    img_id+=1
                    face = cv2.resize(face_cropped(frame), (300,300))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                    #create folder
                    file_name_path = "datasets/"+str(folder_name)+"/user."+str(id)+"."+str(img_id)+".jpg"
                    cv2.imwrite(file_name_path, face)
                    cv2.putText(face, str(img_id), (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (124,255,0), 2)
                    
                    print("Generated :" + file_name_path)
                    cv2.imshow("Cropped face", face)
                    
                #THE MAXIMUM VALUE OF DATASETS BEING GENERATE
                if cv2.waitKey(1)==13 or int(img_id)==350: #13 is the ASCII character of Enter
                    break
            
                
            cap.release()
            print("DONE DONE DONE")
            UIFunctions.generateMessage()

######################## EMPLOYEE DATASETS  #################################
    def employee_generate(self):

            print('Generating Datasets Started')
            name = self.ui.employeeName.text()    
            E_birthdate = str(self.ui.employeeBirthdate.date())
            E_gender = self.ui.employeeGender.currentText()
            E_department = self.ui.employeeDepartment.currentText()
            E_type = self.ui.employeeType.currentText()
            E_position = self.ui.employeePosition.currentText()
            userType= "Employee"

            if len(name)==0  or len(E_gender)==0 or len(E_position)==0 :
                self.ui.studentError.setText("Please fill in all inputs...")
            else:

                connection = mydb.cursor()
                
                connection.execute("SELECT * from known_faces")
                myresult = connection.fetchall()

                id=1
                for x in myresult :
                    id+=1

                sql= "insert into known_faces (face_id,name,sex,birthdate,Department,employeeType,position,userType) values (%s,%s,%s,%s,%s,%s,%s,%s)"
                val = (id,name,E_gender,E_birthdate,E_department,E_type,E_position,userType)


                face_classifier = cv2.CascadeClassifier("haarcascades\haarcascade_frontalface_default.xml")
                #If face is detected on camera it will capture it then convert into GRAYSCALE then finally cropped the frontal face
                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.5, 5)
                    # scaling factor = 1.5
                    # minimum neighbor = 5
                    
                    if faces == ():
                        return None
                    for (x,y,w,h) in faces:
                        cropped_face = img[y:y+h,x:x+w]
                    return cropped_face

                #INSERT DATA IN DATABASE
                connection.execute(sql,val)
                mydb.commit()    
                #####
                cap = cv2.VideoCapture(0)
                img_id = 0
                folder_name= 'face.'+str(id)+"."+userType
                os.makedirs("datasets/"+folder_name)
                while True:
                    ret, frame = cap.read()
                    if face_cropped(frame) is not None:
                        img_id+=1
                        face = cv2.resize(face_cropped(frame), (300,300))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        #create folder
                        file_name_path = "datasets/"+str(folder_name)+"/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (124,255,0), 2)
                        
                        print("Generated :" + file_name_path)
                        cv2.imshow("Cropped face", face)
                        
                    #THE MAXIMUM VALUE OF DATASETS BEING GENERATE
                    if cv2.waitKey(1)==13 or int(img_id)==350: #13 is the ASCII character of Enter
                        break
                
                    
                cap.release()
                print("DONE DONE DONE")
                UIFunctions.generateMessage()



   
####################### TRAINING CLASSIFIER #####################
    def train_classifier():
    
        data_dir="datasets"
        path = [os.path.join(data_dir, f) for f in os.listdir(data_dir)]
        faces = []
        ids = []

        for root, dirs, files in os.walk(data_dir):
            for file in files:
                if file.endswith("png") or file.endswith("jpg"):
                    path = os.path.join(root, file)
                    img = Image.open(path).convert('L')

                    #CONVERTING THE IMAGE INTO NUMPY ARRAY
                    imageNp = np.array(img, 'uint8')
                    #GETTING THE USER ID ON THE IMAGE
                    id = int(os.path.split(path)[1].split(".")[1])
            
                faces.append(imageNp)
                ids.append(id)
        print(faces+ids)
            
        ids = np.array(ids)
        
        # Train and save 
        #LBPH (Local Binary Pattern Histogram) is a Face-Recognition algorithm it is used to recognize the face of a person
        classifier = cv2.face.LBPHFaceRecognizer_create()
        classifier.train(faces,ids)
        classifier.write("classifier.xml")
        UIFunctions.trainingMessage()
        print("Training Done")







####################### FACE RECOGNITION FUNCTION #####################



    def start_faceRG(self,matchscore,scaleVal,neigh): 
        
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)
            
            for (x,y,w,h) in features:
                
                #DRAW A RECTANAGLE TO THE DETECTED FACE 
                cv2.rectangle(img, (x,y), (x+w,y+h), color, 2 )
                
                id, pred = clf.predict(gray_img[y:y+h,x:x+w])

                #FORMULA TO COMPUTE FOR CONFIDENCE
                confidence = int(100*(1-pred/300))






                cursor = mydb.cursor()     
                cursor.execute("select * from known_faces where face_id="+str(id))
                person = cursor.fetchall()
                #convert into string
            
                for row in person:
                    face_id= row[0]
                    name= row[1]
                    course = row[4]
                    userType = row[5]


                name = ''+''.join(name)
                #course = ''+''.join(course)
                # section = ''+''.join(section)     



                #Confidence likelihood of the results being true
                if confidence>matchscore :

                        cv2.putText(img, name+','+userType, (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
                        cv2.putText(img,"Confidence: " + str(confidence), (x,y+180), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
                        self.markAttendance(face_id,userType,name,confidence)
                
                else:
                    cv2.putText(img, "UNAUTHORIZED", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 1, cv2.LINE_AA)
            
            return img




  
    
    
    
        # loading classifier
        faceCascade = cv2.CascadeClassifier("haarcascades\haarcascade_frontalface_default.xml")

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        # now = datetime.now()
        # date = now.strftime('%Y-%m-%d')

        video_capture = cv2.VideoCapture(0)
        # video =  cv2.VideoWriter(date+'.avi',VideoWriter_fourcc(*'MP42'),50,(640,480))
  

        #This loop is for detecting and diplaying the object/face with rectangle 
        while True:
            stream_ok, img = video_capture.read() 
            img = draw_boundary(img, faceCascade,scaleVal,neigh, (255,255,255), "Face", clf)
            cv2.putText(img, datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                        (10, img.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
            cv2.imshow("WMSU FACE RECOGNITION SYSTEM", img)
            # video.write(img)

            if cv2.waitKey(1)==13:
                break
        video_capture.release()
        cv2.destroyAllWindows()
      

