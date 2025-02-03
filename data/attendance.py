from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class attendance:
    def __init__(self,root): 
        self.root=root
        self.root.geometry("1530x790+0+0") 
        self.root.title("STUDENT ATTENDANCE MONITORING SYSTEM")

        #First Image
        img=Image.open(r"college_images\mctrgitofficial_cover.jpg")
        img=img.resize((1400,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1400,height=130)

        img3=Image.open(r"college_images\bg.jpg")
        img3=img3.resize((1300,700),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1400,height=700) 

        title_lbl=Label(bg_img,text="Student Management System",font=("times new roman",30,"bold"),bg="grey",fg="black")
        title_lbl.place(x=0,y=0,width=1400,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=45,width=1250,height=500)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=610,height=450)

        img_left=Image.open(r"college_images\group.jpg")
        img_left=img_left.resize((595,130),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        main_frame.place(x=0,y=45,width=1250,height=500)


    
        #Right label frame
        Right_frame=LabelFrame(main_frame,bd=5,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=630,y=10,width=600,height=450)

        img_right=Image.open(r"college_images\group.jpg")
        img_right=img_right.resize((595,130),Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=580,height=100)




if __name__ == "__main__":
    root=Tk()
    obj=attendance(root)
    root.mainloop()
