from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import student
import os


class Face_Recognition:
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

        #bgimage
        img3=Image.open(r"college_images\bg.jpg")
        img3=img3.resize((1300,700),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1400,height=700) 

        title_lbl=Label(bg_img,text="Student Attendance Monitoring System",font=("times new roman",30,"bold"),bg="grey",fg="black")
        title_lbl.place(x=0,y=0,width=1400,height=45)

        #student button
        img4=Image.open(r"college_images\face.jpg")
        img4=img4.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=50,width=200,height=180)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=100,y=230,width=200,height=35)

        #detect face button
        img5=Image.open(r"college_images\detection.jpg")
        img5=img5.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=350,y=50,width=200,height=180)

        b1_1=Button(bg_img,text="Face Dectector",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=350,y=230,width=200,height=35)

        #Attendance
        img6=Image.open(r"college_images\attendance.jpg")
        img6=img6.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=600,y=50,width=200,height=180)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=600,y=230,width=200,height=35)
    
        #Help Desk
        img7=Image.open(r"college_images\help.jpg")
        img7=img7.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=850,y=50,width=200,height=180)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=850,y=230,width=200,height=35)

        #Train Data
        img8=Image.open(r"college_images\training.jpg")
        img8=img8.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=100,y=280,width=200,height=180)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=100,y=460,width=200,height=35)

        #Photos
        img9=Image.open(r"college_images\image.jpg")
        img9=img9.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=350,y=280,width=200,height=180)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=350,y=460,width=200,height=35)
      
        #Exit
        img11=Image.open(r"college_images\exit.jpg")
        img11=img11.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=600,y=280,width=200,height=180)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=600,y=460,width=200,height=35)

    def open_img(self):
        os.startfile("data")


    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)   
        
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
       
