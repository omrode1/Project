from datetime import datetime
from tkinter import *

import cv2
import mysql.connector
from PIL import Image, ImageTk


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face detection System")

        title_lbl = Label(self.root, text="FACE RECOGNITION ",
                          font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Image 1
        img = Image.open("./college_images/face_detector1.jpg")
        img = img.resize((650, 700), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=55, width=650, height=700)

        # Image 2
        img2 = Image.open(
            "./college_images/facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img2 = img2.resize((950, 700), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=600, y=55, width=950, height=700)

        b1_1 = Button(f_lbl, text="Face Recognition", command=self.face_recog, cursor="hand2",
                      font=("times new roman", 18, "bold"), bg="darkgreen", fg="white")
        b1_1.place(x=365, y=620, width=200, height=40)
    # ========================Attendance   ===============

    def mark_attendance(self, i, r, n, d):
        now = datetime.now()
        current_date = now.strftime("%Y-%m-%d")
        file_name = current_date + '.csv'

        # Check if the individuals are already marked in attendance
        name_list = []
        try:
            with open(file_name, 'r', newline="\n") as f_read:
                myDataList = f_read.readlines()
                for line in myDataList:
                    entry = line.split(",")
                    name_list.append(entry[0])
        except FileNotFoundError:
            # File doesn't exist, will be created in append mode later
            pass

        # Append a new record if individuals are not in name list
        if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
            with open(file_name, 'a', newline="\n") as f_write:
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f_write.writelines(f"\n{i},{r},{n},{d},{dtString}, {d1},Present")


    # ========================face_recognition  ===============



    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="VarshaLohi@12345",
                                               database="studentdatabase")
                my_cursor = conn.cursor()

                def fetch_info(query):
                    my_cursor.execute(query)
                    result = my_cursor.fetchone()
                    return "+".join([str(item) for item in result]) if result else "Not found"

                n = fetch_info(f"select Name from student where Student_id={id}")
                r = fetch_info(f"select Roll from student where Student_id={id}")
                d = fetch_info(f"select Dep from student where Student_id={id}")
                i = fetch_info(f"select Student_id from student where Student_id={id}")

                if confidence > 80:
                    cv2.putText(img, f"ID:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Dep:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i, r, n, d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To face Recognition", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
