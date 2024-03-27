import os
import tkinter.messagebox
from time import strftime
from tkinter import *
from PIL import Image, ImageTk
from attendance import Attendance
from developer import Developer
from face_recognition import Face_Recognition
from help import Help
from student import Student
from train import Train


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        # Image 1
        img = Image.open("./college_images/banner.jpg")
        img = img.resize((1530, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1530, height=130)

        # # Image 2
        # img2 = Image.open("./college_images/facialrecognition.png")
        # img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        # self.photoimg2 = ImageTk.PhotoImage(img2)
        #
        # f_lbl = Label(self.root, image=self.photoimg2)
        # f_lbl.place(x=500, y=0, width=550, height=130)
        #
        # # Image 3
        # img3 = Image.open("./college_images/u.jpg")
        # img3 = img3.resize((500, 130), Image.Resampling.LANCZOS)
        # self.photoimg3 = ImageTk.PhotoImage(img3)
        #
        # f_lbl = Label(self.root, image=self.photoimg3)
        # f_lbl.place(x=1000, y=0, width=550, height=130)

        # Background Image 4
        img4 = Image.open("./college_images/bg3.jpg")
        img4 = img4.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl =Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE" ,font = ("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # ==========time===========
        def time():
            string = strftime('%H:%M:%S %p')
            lb1.config(text = string)
            lb1.after(1000, time)

        lb1 = Label(title_lbl, font=('time new roman', 14, 'bold'), background= 'white', foreground='blue')
        lb1.place(x=0, y=0, width=110, height=50)
        time()

        # student button 1
        img5 = Image.open("./college_images/student.jpg")
        img5 = img5.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, command=self.student_details, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)
        b1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font = ("times new roman", 15, "bold"), bg="white", fg="red")
        b1_1.place(x=200, y=300, width=220, height=40)

        # Detect face button 2
        img6 = Image.open("./college_images/face_detector1.jpg")
        img6 = img6.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2", command=self.face_data,)
        b1.place(x=500, y=100, width=220, height=220)
        b1_1 = Button(bg_img, text="Face Detector", cursor="hand2", command=self.face_data,font=("times new roman", 15, "bold"), bg="white",
                      fg="red")
        b1_1.place(x=500, y=300, width=220, height=40)

        # Attendance face button 3
        img7 = Image.open("./college_images/attendance.png")
        img7 = img7.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2", command=self.attendance)
        b1.place(x=800, y=100, width=220, height=220)
        b1_1 = Button(bg_img, text="Attendance", cursor="hand2", command=self.attendance, font=("times new roman", 15, "bold"), bg="white",
                      fg="red")
        b1_1.place(x=800, y=300, width=220, height=40)

        # Help face button 4
        img8 = Image.open("./college_images/help-desk.jpg")
        img8 = img8.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, command=self.help, cursor="hand2")
        b1.place(x=1100, y=100, width=220, height=220)
        b1_1 = Button(bg_img, text="Help desk", command=self.help, cursor="hand2", font=("times new roman", 15, "bold"), bg="white",
                      fg="red")
        b1_1.place(x=1100, y=300, width=220, height=40)

        # train face button 5
        img9 = Image.open("./college_images/Train.jpg")
        img9 = img9.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2", command=self.train_data,)
        b1.place(x=200, y=380, width=220, height=220)
        b1_1 = Button(bg_img, text="Train Face", cursor="hand2",  command=self.train_data,font=("times new roman", 15, "bold"), bg="white",
                      fg="red")
        b1_1.place(x=200, y=580, width=220, height=40)

        # Photos face button 6
        img10 = Image.open("./college_images/photos.jpg")
        img10 = img10.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10, cursor="hand2", command=self.open_img,)
        b1.place(x=500, y=380, width=220, height=220)
        b1_1 = Button(bg_img, text="Photos", cursor="hand2", command=self.open_img, font=("times new roman", 15, "bold"), bg="white",
                      fg="red")
        b1_1.place(x=500, y=580, width=220, height=40)

        # Developer face button 7
        img11 = Image.open("./college_images/Team.jpg")
        img11 = img11.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11, command=self.developer, cursor="hand2")
        b1.place(x=800, y=380, width=220, height=220)
        b1_1 = Button(bg_img, text="Developer", command=self.developer, cursor="hand2", font=("times new roman", 15, "bold"), bg="white",
                      fg="red")
        b1_1.place(x=800, y=580, width=220, height=40)

        # Exit face button 8
        img12 = Image.open("./college_images/exit.jpg")
        img12 = img12.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        b1 = Button(bg_img, image=self.photoimg12, command=self.iExit, cursor="hand2")
        b1.place(x=1100, y=380, width=220, height=220)
        b1_1 = Button(bg_img, text="Exit", command=self.iExit, cursor="hand2", font=("times new roman", 15, "bold"), bg="white",
                      fg="red")
        b1_1.place(x=1100, y=580, width=220, height=40)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognition", "Are you sure to exit this project", parent=self.root)
        if self.iExit > 0:
          self.root.destroy()
        else:
            return



# ================ Function buttons ====================

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)




if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
