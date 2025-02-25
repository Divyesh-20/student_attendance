import cv2
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import mysql.connector
import numpy as np

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0") 
        self.root.title("STUDENT ATTENDANCE MONITORING SYSTEM")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 30, "bold"), bg="grey", fg="black")
        title_lbl.place(x=0, y=0, width=1400, height=45)

        # Top Image
        img_top = Image.open(r"college_images\fd.jpg")
        img_top = img_top.resize((650, 700), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)

        # Bottom Image
        img_bottom = Image.open(r"college_images\fd.jpg")
        img_bottom = img_bottom.resize((950, 700), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55, width=950, height=700)

        # Face Recognition Button
        b1_1 = Button(self.root, text="Face recognition", cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="black", command=self.face_recog)
        b1_1.place(x=900, y=620, width=200, height=40)
        
        #*******Attendance*********#
    def mark_attendance(self, i, r, n, d):
         with open("hars.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            entry_list = []

        # Collect existing entries in the file to compare with
            for line in myDataList:
                entry = line.split(",")  # Assuming CSV is comma separated
                entry_list.append(entry)

        # Check if the student is already marked in the file
            for entry in entry_list:
            # Check if the combination of i, r, n, d exists in any line
                if entry[0] == str(i) and entry[1] == str(r) and entry[2] == str(n) and entry[3] == str(d):
                    return  # Student already exists, don't add again

        # If the student is not in the list, write attendance to file
            now = datetime.now()
            d1 = now.strftime("%d/%m/%Y")
            dtString = now.strftime("%H:%M:%S")
            f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    

    #***********face recognition*******#
    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Harshal@1234", database="face_recognizer")    
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where Student_id=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("select Roll from student where Student_id=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute("select Dept from student where Student_id=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                if confidence > 77:
                    cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(id,r,n,d)

                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, f"Unknown Face", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord=draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        if not video_cap.isOpened():
            print("Error: Could not open video capture.")
            return

        while True:
            ret,img = video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face recognition", img)

            if cv2.waitKey(1) == 13:  # Press Enter to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
