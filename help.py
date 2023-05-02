from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # importing pillow library
from tkinter import messagebox
import mysql.connector
import os
import cv2
from time import strftime
from datetime import datetime
import webbrowser

class Help:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0") #setting window size
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root, text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"C:\Users\DIYA\Desktop\ML Project\Images\new9.jpg")
        img_top=img_top.resize((1530,720)) #ANTILIAS - converts high level image to low level image
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        dev_lbl=Label(f_lbl, text="vdn@gmail.com",font=("times new roman",20,"bold"),bg="white",fg="blue")
        dev_lbl.place(x=20, y=20)

        

if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()