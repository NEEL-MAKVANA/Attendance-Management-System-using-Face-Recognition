from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # importing pillow library
from student import Student
from time import strftime
from datetime import datetime
from tkinter import messagebox
from train import Train
from face_recognition import Face_Rec
import os
from attendence import Attendence
from developer import Developer
from help import Help

class Face_Recognition_Systen:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0") #setting window size
        self.root.title("Face Recognition System")

        # First image
        img=Image.open(r"C:\Users\DIYA\Desktop\ML Project\Images\img1.jpg")
        img=img.resize((500,130),Image.ANTIALIAS) #ANTILIAS - converts high level image to low level image
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        # Second image
        img1=Image.open(r"C:\Users\DIYA\Desktop\ML Project\Images\img2.png")
        img1=img1.resize((500,130),Image.ANTIALIAS) #ANTILIAS - converts high level image to low level image
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root, image=self.photoimg1)
        f_lbl.place(x=507,y=0,width=510,height=130)

        # Third image
        img2=Image.open(r"C:\Users\DIYA\Desktop\ML Project\Images\img3.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS) #ANTILIAS - converts high level image to low level image
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=530,height=130)

        # Title and bg
        img3=Image.open(r"C:\Users\DIYA\Desktop\ML Project\Images\bg.png")
        img3=img3.resize((1530,710),Image.ANTIALIAS) #ANTILIAS - converts high level image to low level image
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root, image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img, text="Face Recognition System",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=64)

        # ---------- time -------------
        def time():
            string = strftime('%H: %M : %S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(title_lbl,font=('times new roman',18,'bold'  ),background='white',foreground='blue')
        lbl.place(x=15,y=0,width=170,height=55)
        time()

        #student button
        img4=Image.open(r"C:\Users\DIYA\Desktop\ML Project\Images\student_details.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS) 
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details, cursor="hand2")
        b1.place(x=250, y=100,width=220,height=220)

        b1_1=Button(bg_img, text="Student Details",command=self.student_details, cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=250, y=300,width=220,height=40)

        #Detect face button
        img5=Image.open(r"C:\Users\DIYA\Desktop\ML Project\Images\face_detector.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS) 
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=650, y=100,width=220,height=220)

        b1_1=Button(bg_img, text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=650, y=300,width=220,height=40)

        #Attendence button
        img6=Image.open(r"C:\Users\DIYA\Desktop\ML Project\Images\attendece.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS) 
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=1050, y=100,width=220,height=220)

        b1_1=Button(bg_img, text="Attendence",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1050, y=300,width=220,height=40)

        #Help button
        # img7=Image.open(r"C:\Users\DIYA\Desktop\ML Project\Images\help_desk.jpg")
        # img7=img7.resize((220,220),Image.ANTIALIAS) 
        # self.photoimg7=ImageTk.PhotoImage(img7)

        # b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        # b1.place(x=1100, y=100,width=220,height=220)

        # b1_1=Button(bg_img, text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        # b1_1.place(x=1100, y=300,width=220,height=40)

        #train button
        img8=Image.open(r"C:\Users\DIYA\Desktop\ML Project\Images\train_data.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS) 
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=250, y=380,width=220,height=220)

        b1_1=Button(bg_img, text="Traing data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=250, y=580,width=220,height=40)

        #photos button
        img9=Image.open(r"C:\Users\DIYA\Desktop\ML Project\Images\new15.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS) 
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=650, y=380,width=220,height=220)

        b1_1=Button(bg_img, text="Photos",command=self.open_img,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=650, y=580,width=220,height=40)

        #developer button
        # img10=Image.open(r"C:\Users\DIYA\Desktop\ML Project\Images\developers.jpg")
        # img10=img10.resize((220,220),Image.ANTIALIAS) 
        # self.photoimg10=ImageTk.PhotoImage(img10)

        # b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.devloper_data)
        # b1.place(x=800, y=380,width=220,height=220)

        # b1_1=Button(bg_img, text="Developer",command=self.devloper_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        # b1_1.place(x=800, y=580,width=220,height=40)

        #Exit button
        img11=Image.open(r"C:\Users\DIYA\Desktop\ML Project\Images\exit.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS) 
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1050, y=380,width=220,height=220)

        b1_1=Button(bg_img, text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1050, y=580,width=220,height=40)

    # ----- Functions button ------------
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
    
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Rec(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendence(self.new_window)

    def devloper_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)
    
    def iExit(self):
        self.iExit=messagebox.askyesno("Face Recognition","Are you sure, you want to exit this project?",parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return

    # ---- for photos --------
    def open_img(self):
        os.startfile("data")


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_Systen(root)
    root.mainloop()