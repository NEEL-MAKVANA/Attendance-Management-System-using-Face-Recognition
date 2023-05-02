from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # importing pillow library
from tkinter import messagebox
import mysql.connector
import os
import cv2
from time import strftime
from datetime import datetime

class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0") #setting window size
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root, text="DEVELOPERS",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"C:\Users\DIYA\Desktop\ML Project\Images\developer.jpg")
        img_top=img_top.resize((1530,720)) #ANTILIAS - converts high level image to low level image
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        # Frame
        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=1000, y=0, width=500, height=600)

        img_top1=Image.open(r"C:\Users\DIYA\Desktop\ML Project\Images\developer.jpg")
        img_top1=img_top1.resize((1530,720)) #ANTILIAS - converts high level image to low level image
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(main_frame, image=self.photoimg_top)
        f_lbl.place(x=300,y=0,width=200,height=200)

        # Devloper info
        dev_label = Label(main_frame, text="Hello my name, Diya",font=("times new roman",20,"bold"),bg="white")
        dev_label.grid(x=0,y=5)

        dev_label = Label(main_frame, text="Hello my name, Diya",font=("times new roman",20,"bold"),bg="white")
        dev_label.grid(x=0,y=5)

if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()