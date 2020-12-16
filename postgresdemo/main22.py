import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
from template import Ui_MainWindow
from Attendencecopy import Attendance
from db import InsertStaffData,staffauthenication,viewORremovestaff,insertQuery,Display,removestaffdb,getStudentAttendance,studentdb,removestudents


class Mainwindow():
    def __init__(self):
        self.main_window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)

        self.ui.stackedWidget.setCurrentWidget(self.ui.Login)
        self.ui.login_btn_2.clicked.connect(self.Login_Check)                 # staff login button press
        self.ui.Attendance_btn.clicked.connect(self.Attendancelist)           # calling Attendance
        self.ui.Profile_btn.clicked.connect(self.Profile)                     # To open Profile UI
        self.ui.Settings_btn.clicked.connect(self.Settings)                # To open Settings UI

    def show(self):
        self.main_window.show()

    def removestudent(self):
        usn = self.ui.USN_Delete.text()
        removestudents(usn)
        msg = QMessageBox()
        #msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("success")
        msg.setText('deleted successfully!')
        msg.exec_()   
        self.ui.USN_Delete.clear()


    def registerstudent(self):
        stuname = self.ui.Student_Name.text()
        usn = self.ui.USN.text()
        course = self.ui.Course.text()
        studentdb(stuname,usn,course)
        self.ui.Student_Name.clear()
        self.ui.USN.clear()
        self.ui.Course.clear()
        msg = QMessageBox()
        #msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("success")
        msg.setText('Added successfully!')
        msg.exec_()   


    def studentphoto(self):
        name = self.ui.Student_Name.text()
        import cv2
        videoCaptureObject = cv2.VideoCapture(0)
        result = True
        while(result):
            ret,frame = videoCaptureObject.read()
            cv2.imwrite("images/"+name+".jpg",frame)
            result = False
        videoCaptureObject.release()
        cv2.destroyAllWindows()

    def updateAttendance1(self):     # to update the attendance to the database 
        subcode = self.ui.lineedit341.text()
        a = insertQuery(subcode)    
        msg = QMessageBox()
        #msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("success")
        msg.setText('Attendance uploaded successfully!')
        msg.exec_()    

    def updateAttendance(self):     # to update the attendance to the database 
        subcode = self.ui.lineedit34.text()
        a = insertQuery(subcode)    
        msg = QMessageBox()
        #msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("success")
        msg.setText('Attendance uploaded successfully!')
        msg.exec_()    

    def addstaffdb(self):
        staffname = self.ui.staffname.text()
        staffphone = self.ui.staffphone.text()
        staffemail = self.ui.staffemail.text()
        staffusername = self.ui.staffusername.text()
        staffpassword = self.ui.staffpassword.text()
        InsertStaffData(staffname,staffphone,staffemail,staffusername,staffpassword)
        self.ui.staffname.clear()
        self.ui.staffphone.clear()
        self.ui.staffemail.clear()
        self.ui.staffusername.clear()
        self.ui.staffpassword.clear()
        msg = QMessageBox()
        #msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("success")
        msg.setText('Added successfully!')
        msg.exec_()  
        
    
    def removestaff(self):
        name = self.ui.ID_Delete.text()
        removestaffdb(name)
        msg = QMessageBox()
        #msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Login Error")
        msg.setText('Please enter valid username and password!')
        msg.exec_()
        self.ui.ID_Delete.clear()

    def getAttandance(self):
        date = self.ui.lineEdit.text()
        rows = getStudentAttendance(date)
        print(rows)
        self.ui.tableWidget.clear()
        self.ui.tabledata(rows)
    def getAttandance1(self):
        date = self.ui.lineEdit12.text()
        rows = getStudentAttendance(date)
        self.ui.tableWidget1.clear()
        self.ui.tabledata1(rows)



    def Login_Check(self):
        if self.ui.user_name.text() =="admin" and self.ui.pwd.text() =="1234":
            self.Admin_UI()
    
        elif self.ui.user_name.text() =="" and self.ui.pwd.text() =="":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Login Error")
            msg.setText('Please enter valid username and password!')
            msg.exec_()
        else:    
            username = self.ui.user_name.text()
            password = self.ui.pwd.text()
            result = staffauthenication(username,password)
            #print(result)
            if(result[0]):
                print("login success")
                self.currentfaculityname = result[1]          # name of the logged faculity
                self.facultyemail = result[2]
                self.facultyphone =result[3]
                self.stafflogin()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle("Login Error")
                msg.setText('Please enter valid username and password!')
                msg.exec_()

    def stafflogin(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Front)
        self.ui.Camera_btn.clicked.connect(self.opencamera)             # To start the camera to take attendance
        self.ui.Profile_btn.clicked.connect(self.Profile)               # To open Profile UI
        self.ui.Settings_btn.clicked.connect(self.Settings)   
        self.ui.buttonUpload.clicked.connect(self.updateAttendance)      # To open Settings UI

    def opencamera(self):
        attend = Attendance()
        attend.main()
    def Attendancelist(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Attendance_List)
        self.ui.check.clicked.connect(self.getAttandance)
        self.ui.back_btn_2.clicked.connect(self.stafflogin)

    def Profile(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Profile)
        self.ui.Faculty_Name_2.setText(self.currentfaculityname)
        self.ui.Facultye.setText(self.facultyemail)
        self.ui.Facultyph.setText(self.facultyphone)
        
        self.ui.Settings_btn_4.clicked.connect(self.Settings)                  #To open Settings UI from Profile UI
        self.ui.back_btn_3.clicked.connect(self.stafflogin)                    # To open StaffLogin UI by clicking back button

    def Settings(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Settings)
        self.ui.Profile_btn_6.clicked.connect(self.Profile)                   #To open Profile UI from Settings UI
        self.ui.back_btn_7.clicked.connect(self.stafflogin)                   # To open StaffLogin UI by clicking back button
        # self.ui.Camera_Settings_btn.clicked.connect(self)
        # self.ui.Security_btn.clicked.connect(self)

    def Admin_UI(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Admin_Front)
        self.ui.Profile_btn_7.clicked.connect(self.Ad_Profile)
        self.ui.Attendance_btn_2.clicked.connect(self.Ad_Attendance)
        self.ui.Camera_btn_2.clicked.connect(self.opencamera)
        self.ui.Add_Faculty_btn.clicked.connect(self.Add_Staff)
        self.ui.Add_Stud_btn.clicked.connect(self.Add_Stud)
        self.ui.Remove_Faculty_btn_1.clicked.connect(self.Remove_Staff)
        self.ui.Remove_Stud_btn.clicked.connect(self.Remove_Stud)
        self.ui.Settings_btn_7.clicked.connect(self.Ad_Settings)
        self.ui.UploadAttendance.clicked.connect(self.updateAttendance1)

    def Ad_Attendance(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Admin_Attendance)
        self.ui.Add_Faculty_btn_3.clicked.connect(self.Add_Staff)
        self.ui.Add_Stud_btn_3.clicked.connect(self.Add_Stud)
        self.ui.Remove_Faculty_btn_8.clicked.connect(self.Remove_Staff)
        self.ui.Remove_Stud_btn_3.clicked.connect(self.Remove_Stud)
        self.ui.Settings_btn_10.clicked.connect(self.Ad_Settings)
        self.ui.Profile_btn_12.clicked.connect(self.Ad_Profile)
        self.ui.back_btn_12.clicked.connect(self.Admin_UI)
        self.ui.check1.clicked.connect(self.getAttandance1)

    def Add_Stud(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Add_Student)
        self.ui.Add_Faculty_btn_2.clicked.connect(self.Add_Staff)
        self.ui.Remove_Faculty_btn_2.clicked.connect(self.Remove_Staff)
        self.ui.Remove_Stud_btn_2.clicked.connect(self.Remove_Stud)
        self.ui.Settings_btn_9.clicked.connect(self.Ad_Settings)
        self.ui.Profile_btn_10.clicked.connect(self.Ad_Profile)
        self.ui.back_btn_5.clicked.connect(self.Admin_UI)
        self.ui.Enroll_btn.clicked.connect(self.registerstudent)
        #self.ui.Upload_btn.clicked.connect(self.studentphoto)
        self.ui.Photo_Loc.clicked.connect(self.studentphoto)
        #self.ui.Photo_Search_btn.clicked.connect(self)
    def Remove_Stud(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Remove_Student)
        self.ui.Profile_btn_16.clicked.connect(self.Ad_Profile)
        self.ui.Attendance_btn_2.clicked.connect(self.Attendancelist)
        self.ui.Camera_btn_2.clicked.connect(self.opencamera)
        self.ui.Add_Faculty_btn_5.clicked.connect(self.Add_Staff)
        self.ui.Add_Stud_btn_5.clicked.connect(self.Add_Stud)
        self.ui.Remove_Faculty_btn_3.clicked.connect(self.Remove_Staff)
        self.ui.Settings_btn_12.clicked.connect(self.Ad_Settings)
        self.ui.back_btn_9.clicked.connect(self.Admin_UI)
        self.ui.Remove_Student_2.clicked.connect(self.removestudent)
        # self.ui.USN_Search_btn.clicked.connect(self)
        # self.ui.USN_Delete.clicked.connect(self)
    def Add_Staff(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Add_Faculty)
        self.ui.Add_Stud_btn_6.clicked.connect(self.Add_Stud)
        self.ui.Remove_Faculty_btn_4.clicked.connect(self.Remove_Staff)
        self.ui.Remove_Stud_btn_6.clicked.connect(self.Remove_Stud)
        self.ui.Settings_btn_13.clicked.connect(self.Ad_Settings)
        self.ui.Profile_btn_18.clicked.connect(self.Ad_Profile)
        self.ui.back_btn_10.clicked.connect(self.Admin_UI)
        self.ui.Enroll_btn_2.clicked.connect(self.addstaffdb)
    def Remove_Staff(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Remove_Faculty_2)
        self.ui.Profile_btn_20.clicked.connect(self.Ad_Profile)
        self.ui.Add_Faculty_btn_7.clicked.connect(self.Add_Staff)
        self.ui.Add_Stud_btn_7.clicked.connect(self.Add_Stud)
        self.ui.Settings_btn_14.clicked.connect(self.Ad_Settings)
        self.ui.Remove_Stud_btn_7.clicked.connect(self.Remove_Stud)
        self.ui.back_btn_11.clicked.connect(self.Admin_UI)
        #self.ui.ID_Search.clicked.connect(self)
        #self.ui.ID_Delete.clicked.connect(self.remove_Staff)
        self.ui.Remove_Faculty.clicked.connect(self.removestaff)
    def Ad_Profile(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Admin_Profile)
        self.ui.Settings_btn_15.clicked.connect(self.Ad_Settings)
        self.ui.back_btn_6.clicked.connect(self.Admin_UI)
        self.ui.Add_Faculty_btn_8.clicked.connect(self.Add_Staff)
        self.ui.Add_Stud_btn_8.clicked.connect(self.Add_Stud)
        self.ui.Remove_Faculty_btn_5.clicked.connect(self.Remove_Staff)
        self.ui.Remove_Stud_btn_8.clicked.connect(self.Remove_Staff)
        self.ui.back_btn_6.clicked.connect(self.Admin_UI)

    def Ad_Settings(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Admin_Settings)
        self.ui.Profile_btn_11.clicked.connect(self.Ad_Profile)
        self.ui.Add_Faculty_btn_9.clicked.connect(self.Add_Staff)
        self.ui.Add_Stud_btn_9.clicked.connect(self.Add_Stud)
        self.ui.Remove_Faculty_btn_6.clicked.connect(self.Remove_Staff)
        self.ui.Remove_Stud_btn_9.clicked.connect(self.Remove_Stud)
        self.ui.back_btn_8.clicked.connect(self.Admin_UI)
        # self.ui.Camera_Security_btn_2.clicked.connect(self)
        # self.ui.Security_btn_2.clicked.connect(self)

    def back_btn_1(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Front)
    def back_btn_2 (self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Front)
    def back_btn_3(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Front)
    def back_btn_5(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Admin_Front)
    def back_btn_6(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Admin_Front)
    def back_btn_7(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Front)
    def back_btn_8(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Admin_Front)
    def back_btn_9(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Admin_Front)
    def back_btn_10(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Admin_Front)
    def back_btn_11(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Admin_Front)
    def back_btn_12(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Front)

if __name__=='__main__':
    app = QApplication(sys.argv)
    windowmain = Mainwindow()
    windowmain.show()
    sys.exit(app.exec_())


'''
# data added in table ...... code 
        self.tableWidget.setItem(0,0, QTableWidgetItem("NAME"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("TIME")
        self.tableWidget.setItem(0,2, QTableWidgetItem("DATE"))

        rows = getdata()
        for i,r in enumerate(rows):
                self.tableWidget.setItem(i+1,0, QTableWidgetItem(r[0]))
                self.tableWidget.setItem(i+1,1, QTableWidgetItem(r[1]))
                self.tableWidget.setItem(i+1,2, QTableWidgetItem(r[2]))


        #
'''
