from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # importing pillow library
from tkinter import messagebox
import mysql.connector
import os
import cv2
import numpy as np

class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0") #setting window size
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root, text="Train Dataset",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"C:\Users\DIYA\Desktop\ML Project\Images\new11.jpg")
        img_top=img_top.resize((1530,850)) #ANTILIAS - converts high level image to low level image
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0,y=45,width=1530,height=850)

        # button
        b1_1=Button(f_lbl, text="Train Data",command=self.train_classifier ,cursor="hand2",font=("times new roman",30,"bold"),fg="white",bg="darkblue")
        b1_1.place(x=200, y=500,width=400,height=100)

        # img_bottom=Image.open(r"C:\Users\DIYA\Desktop\ML Project\Images\photos.jpg")
        # img_bottom=img_bottom.resize((1530,325)) #ANTILIAS - converts high level image to low level image
        # self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        # f_lbl=Label(self.root, image=self.photoimg_bottom)
        # f_lbl.place(x=0,y=440,width=1530,height=325)

    def train_classifier(self):
        data_dir = (r"C:\Users\DIYA\Desktop\ML Project\data")
        path = [ os.path.join(data_dir, file) for file in os.listdir(data_dir)] # listdir is used to get all the files in that directories
        faces = []
        ids = []
        # print(path)
        for image in path:
            img = Image.open(image).convert('L') # gray scale image
            imageNp = np.array(img,'uint8') # converting image into numpy array
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1)==13
        # print(ids)
        ids=np.array(ids) # numpy increases performance


        # -------- Traing the classifier and save -----------
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write(r"C:\Users\DIYA\Desktop\ML Project\classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Trainging datasets completed!!")

if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()