import cv2
import face_recognition
import numpy as np
import os
from datetime import datetime,date

class Attendance:
    def __init__(self):
        #print("constructor")
        path = "images"
        steps = ''' 1.import the images and convert it into RGB 
                    2. encode the image
                    3.compare the image, using camera to validate '''
        self.images = []
        self.label = []
        mylist = os.listdir(path)
        print(mylist)
        for item in mylist:
            currentImage = cv2.imread(f'{path}/{item}')     # getting the current image, it is matrix.
            self.images.append(currentImage)                     # appending the matrix in images list.
            self.label.append(os.path.splitext(item)[0])         # names are append in the label list.
        print(self.label)
        self.file = date.today()
        self.file = self.file.strftime('%d-%m-%y')
        with open(self.file+".csv",'w') as f:
            f.write("NAME, TIME, DATE")



        # mark attendance function()
    def MarkAttendance(self,name):
        with open(self.file+".csv",'r+') as f:
            DataList = f.readlines()            # ['NAME,TIME']
            nameList = []
            for line in DataList:
                entry = line.split(',')     # split like ['NAME', 'TIME']
                nameList.append(entry[0])
            if name not in nameList:
                now = datetime.now()
                today = date.today()
                dtString = now.strftime('%H:%M:%S')
                todaydate = today.strftime('%Y/%m/%d')
                f.writelines(f'\n{name}, {dtString}, {todaydate}')
                




    # create function to find all encoding.
    def findencoding(self,images):
        print("find encondings")
        self.encodeList = []                                # create a list to store all encode matrix value
        for image in images:                          # loop to iterate through the images
            self.image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            self.encode = face_recognition.face_encodings(image)[0]              # encoding each images.
            self.encodeList.append(self.encode)                                       # encode is append to encode List.
        return self.encodeList






    def main(self):
        print("main function")
        encodeListKnown = self.findencoding(self.images)       # calling the encoding function
        self.encodeListKnown = encodeListKnown
        print("encoding complete")


        # capture images from camera

        c = True
        cap = cv2.VideoCapture(0)
        #success, img = cap.read()
        while (c == True):
            success, img = cap.read()
            imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
            currentFrameFace = face_recognition.face_locations(imgS)       # find face of current frame
            encodesCurrentFrame = face_recognition.face_encodings(imgS, currentFrameFace,)

            for encodeFace, faceLoc in zip(encodesCurrentFrame, currentFrameFace):
                matches = face_recognition.compare_faces(self.encodeListKnown, encodeFace)           # passes the list of encode faces and current encode face as args.
                faceDistance = face_recognition.face_distance(self.encodeListKnown, encodeFace)      # min value for match faces, otherwise large value
                #print(faceDistance)
                #print(matches)
                matchIndex = np.argmin(faceDistance)       # it print the index.

                if matches[matchIndex]:             # here we give the true value index
                    self.name = self.label[matchIndex].upper()
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 2)
                    cv2.rectangle(img, (x1,y2-35), (x2,y2), (0, 255, 0),cv2.FILLED)
                    cv2.putText(img,self.name,(x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255), 2)
                    self.MarkAttendance(self.name)        #calling the function markAttendance()

                    cv2.imshow("webcam", img)
                    if(cv2.waitKey(1) & 0xFF == ord('q')):
                        c = False
                        











