
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
from PyQt5.QtGui import QPixmap
import matplotlib.pyplot as plt


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

    def videoRecordAlert():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("The Video has been saved in Recorded folder")
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
    def generate_dataset(self,scale,neigh,selected_camera):

        print('Generating Datasets Started')
        print("Min Neigbor:"+ str(neigh)+" Min Scale: "+ str(scale))
        print('Selected Camera = ' + str(selected_camera))

        now = datetime.now()
        registrationDate = now.strftime('%Y-%m-%d')
        name = self.ui.studentName.text()       
        birthdate = str(self.ui.studentBirth.date())
        # S_birthdate = birthdate.toString("MM/dd/yyyy")
        S_birthdate =  str(self.ui.studentBirth.date())


        S_gender = self.ui.studentGender.currentText()
        S_course = self.ui.studentCourse.currentText()
        userType = 'Student'
        status = 'ACTIVE'

        if len(name)==0  or len(S_gender)==0 or len(S_course)==0 :
            self.ui.studentError.setText("Please fill in all inputs...")
        else:

            connection = mydb.cursor()
            
            connection.execute("SELECT * from known_faces")
            myresult = connection.fetchall()

            id=1
            for x in myresult :
                id+=1

            sql= "insert into known_faces (face_id,name,course,birthdate,sex,userType,registrationDate,status) values (%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (id,name,S_course,S_birthdate,S_gender,userType,registrationDate,status)


            face_classifier = cv2.CascadeClassifier("haarcascades\haarcascade_frontalface_default.xml")
            #If face is detected on camera it will capture it then convert into GRAYSCALE then finally cropped the frontal face
            def face_cropped(img):
                gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.2, 10)
                # scaling factor = 1.5
                # minimum neighbor = 5
                
                if faces == ():
                    return None
                for (x,y,w,h) in faces:
                    cropped_face = img[y:y+h,
                    x:x+w]
                return cropped_face

            #INSERT DATA IN DATABASE
            connection.execute(sql,val)
            mydb.commit()    
            #####
            cap = cv2.VideoCapture(selected_camera)
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
                    cv2.putText(face, str(img_id), (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,0), 2)
                    
                    cv2.imshow("Cropped face", face)
                    
                #THE MAXIMUM VALUE OF DATASETS BEING GENERATE
                if cv2.waitKey(1)==13 or int(img_id)==300: #13 is the ASCII character of Enter
            
            #Display image
                    break
            
                
            cap.release()
            print("DONE DONE DONE")

            ######################## DISPLAY INFORMATION AFTER REGISTRATION ####################
            profile = "datasets/"+str(folder_name)+"/user."+str(id)+"."+str(2)+".jpg"
            pixmap = QtGui.QPixmap(profile)
            self.ui.imageLabel.setPixmap(pixmap)
            self.ui.imageLabel.resize(200,200)
            self.ui.imageLabel.setScaledContents(True)

            self.ui.registeredName.setText(name)
            self.ui.registeredGender.setText(S_gender)
            self.ui.registeredCourse.setText(S_course)
            UIFunctions.generateMessage()

######################## EMPLOYEE DATASETS  #################################
    def employee_generate(self,scale,neigh,selected_camera):

            print('Generating Datasets Started')
            print("Min Neigbor:"+ str(neigh)+" Min Scale: "+ str(scale))
            print('Selected Camera = ' + str(selected_camera))


            name = self.ui.employeeName.text()    
            E_birthdate = self.ui.employeeBirthdate.date()
            E_birthdate = E_birthdate.toString("MM/dd/yyyy")



            E_gender = self.ui.employeeGender.currentText()
            E_department = self.ui.employeeDepartment.currentText()
            E_type = self.ui.employeeType.currentText()
            E_position = self.ui.employeePosition.currentText()
            userType= "Employee"
            status = "ACTIVE"

            if len(name)==0  or len(E_gender)==0 or len(E_position)==0 :
                self.ui.studentError.setText("Please fill in all inputs...")
            else:

                connection = mydb.cursor()
                
                connection.execute("SELECT * from known_faces")
                myresult = connection.fetchall()

                id=1
                for x in myresult :
                    id+=1

                sql= "insert into known_faces (face_id,name,sex,birthdate,college,employeeType,position,userType,status) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = (id,name,E_gender,E_birthdate,E_department,E_type,E_position,userType,status)


                face_classifier = cv2.CascadeClassifier("haarcascades\haarcascade_frontalface_default.xml")
                #If face is detected on camera it will capture it then convert into GRAYSCALE then finally cropped the frontal face
                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, scale, neigh)

                    
                    if faces == ():
                        return None
                    for (x,y,w,h) in faces:
                        cropped_face = img[y:y+h,x:x+w]
                    return cropped_face

                #INSERT DATA IN DATABASE
                connection.execute(sql,val)
                mydb.commit()    
                #####
                cap = cv2.VideoCapture(selected_camera)
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
                        cv2.putText(face, str(img_id), (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,0), 2)
                        
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



    def start_faceRG(self,matchscore,scaleVal,neigh,selected_camera,video_rec,notif,selected_entry,gate): 
        print("Face Recogniction is starting")
        print("Min Neigbor:"+ str(neigh)+" Min Scale: "+ str(scaleVal)+" Confidence: "+ str(matchscore))
        print('Video Record = ' + str(video_rec))
        print('Selected Camera = ' + str(selected_camera))
        print('Unauthorized Alert = ' + str(notif))
        print('selected_entry = ' + str(selected_entry))


        acc= []
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf,entrance):
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors, flags=cv2.CASCADE_SCALE_IMAGE,minSize=(64, 64))
            
            for (x,y,w,h) in features:
                
                #DRAW A RECTANAGLE TO THE DETECTED FACE 
                cv2.rectangle(img, (x,y), (x+w,y+h), color, 2 )
                
                id, pred = clf.predict(gray_img[y:y+h,x:x+w])

                #FORMULA TO COMPUTE FOR CONFIDENCE
                confidence = int(100*(1-pred/300))


                now = datetime.now()
                time = now.strftime('%I:%M:%S %p')
                date = now.strftime('%Y-%m-%d')
                

                # get academic year
                academic = mydb.cursor()     
                academic.execute("select * from settings")
                year = academic.fetchall()
                for row in year:
                    acadYear= row[1]
                

                # get user info in database
                cursor = mydb.cursor()     
                cursor.execute("select * from known_faces where face_id="+str(id))
                person = cursor.fetchall()
                #convert into string
            
                for row in person:
                    face_id= row[0]
                    name= row[1]
                    course = row[4]
                    userType = row[5]
                    status = row[10]
                    college = row[9]


                name = ''+''.join(name)
                status = ''+''.join(status)

                academic = ''+''.join(acadYear)
                #course = ''+''.join(course)
                # section = ''+''.join(section)     

                now = datetime.now()
                #Confidence likelihood of the results being true
              
                if confidence>matchscore :
                    if(status =='ACTIVE'):
                        cv2.putText(img, name+','+userType, (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
                        cv2.putText(img,"Confidence: " + str(confidence), (x,y+180), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
                        self.markAttendance(face_id,userType,name,confidence,college,academic,entrance,gate)
                    else:
                        break
                    
                else:
                    if notif == 1 :
                        self.unauthorizedDialog(time,date)
                        cv2.putText(img, "UNAUTHORIZED", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 1, cv2.LINE_AA)
            return img



  
    
    
    
        # loading classifier
        faceCascade = cv2.CascadeClassifier("haarcascades\haarcascade_frontalface_default.xml")

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        now = datetime.now()
        date = now.strftime('%Y-%m-%d')
        if video_rec == 1:
            video =  cv2.VideoWriter('recorded/'+date+'.mp4',VideoWriter_fourcc(*'MP42'),15,(640,480))

          #ENTRY [ENTRANCE AND EXIT]
        Entrance = 'Entrance'
        if selected_entry==1:
            entry = 'Exit'
        else:
            entry = 'Entrance'

        if selected_camera == 2 :
            video_capture1 = cv2.VideoCapture(0)
            video_capture2 = cv2.VideoCapture(1)

        
        
    
            #This loop is for detecting and diplaying the object/face with rectangle 
            while True:
                stream_ok, img1 = video_capture1.read() 
                stream_ok, img2 = video_capture2.read() 



                img1 = draw_boundary(img1, faceCascade,scaleVal,neigh, (0,255,0), "Face", clf,Entrance)
                cv2.putText(img1, datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                            (10, img1.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
                cv2.putText(img1,'Entrance',(10, img1.shape[0] - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
                cv2.putText(img1,gate,(500, img1.shape[0] - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                cv2.imshow("WMSU FACE RECOGNITION SYSTEM VIDEO #1", img1)

                #VIDEO FEED #2

                img2 = draw_boundary(img2, faceCascade,scaleVal,neigh, (0,255,0), "Face", clf,entry)
                cv2.putText(img2, datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                            (10, img2.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)

                cv2.putText(img2,gate,(500, img2.shape[0] - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                cv2.putText(img2,entry,(10, img2.shape[0] - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3)
                cv2.imshow("WMSU FACE RECOGNITION SYSTEM VIDEO #2", img2)                

                if video_rec == 1:
                    video.write(img1)

                if cv2.waitKey(1)==13:
                    break

            video_capture1.release()
            video_capture2.release()

            cv2.destroyAllWindows()
            if video_rec == 1 :
                UIFunctions.videoRecordAlert()
                
        else:

            video_capture1 = cv2.VideoCapture(selected_camera)
             #This loop is for detecting and diplaying the object/face with rectangle 
            while True:
                stream_ok, img1 = video_capture1.read() 

                img1 = draw_boundary(img1, faceCascade,scaleVal,neigh, (0,255,0), "Face", clf,Entrance)
                cv2.putText(img1, datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                            (10, img1.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)
                            
                cv2.putText(img1,'Entrance',(10, img1.shape[0] - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)  
                cv2.putText(img1,gate,(500, img1.shape[0] - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)



                cv2.imshow("WMSU FACE RECOGNITION SYSTEM VIDEO #1", img1)
    

                if video_rec == 1:
                    video.write(img1)

                if cv2.waitKey(1)==13:
                    break
            video_capture1.release()

            cv2.destroyAllWindows()


        if video_rec == 1 :
            UIFunctions.videoRecordAlert()    

