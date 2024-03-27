import os
from tkinter import *
from tkinter import messagebox
import cv2
import numpy as np
from PIL import Image, ImageTk


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train System")

        title_lbl = Label(self.root, text="TRAIN DATASET ",
                          font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Image 1
        img = Image.open("./college_images/Stanford.jpg")
        img = img.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=55, width=1530, height=325)

        b1_1 = Button(self.root, text="Train Dataset", command=self.train_classifier, cursor="hand2",
                      font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_1.place(x=0, y=382, width=1530, height=66)

        # Image 2
        img2 = Image.open("./college_images/facialrecognition.png")
        img2 = img2.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=0, y=450, width=1530, height=325)

    def train_classifier(self):
        data_dir = ("data")

        # Check if the data directory exists
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", "Data directory not found")
            return

        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]


        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # Gray scale image
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)


        #================== Train the classifoer And save ==============
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets Completed!!")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
