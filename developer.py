from tkinter import *
from PIL import Image, ImageTk

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recognition_System")

        # Load and place the first header image
        img = Image.open("./college_images/dev.jpg")
        img = img.resize((1530, 150), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1530, height=130)

        # Load and place the background image
        bg1 = Image.open("./college_images/dev.jpg")
        bg1 = bg1.resize((1530, 768), Image.Resampling.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1530, height=768)

        # Title section
        title_lb1 = Label(bg_img, text="Developer Panel", font=("verdana", 30, "bold"), bg="white", fg="navyblue")
        title_lb1.place(x=0, y=0, width=1530, height=45)

        # Adjusted button placement
        button_details = [
            {"x": 150, "y": 250, "text": "Om Rode","image_path": "./college_images/or.png"},
            {"x": 380, "y": 250, "text": "Yash Lohi", "image_path": "./college_images/yl.png"},
            {"x": 610, "y": 250, "text": "Prathamesh L", "image_path": "./college_images/pl.png"},
            {"x": 840, "y": 250, "text": "Shraddha D", "image_path": "./college_images/Sd.png"},
            {"x": 1070, "y": 250, "text": "Sakshi Bhoyar", "image_path": "./college_images/sb.png"},
            {"x": 1300, "y": 250, "text": "Indriayni P", "image_path": "./college_images/Ip.png"}
        ]

        for detail in button_details:
            btn_img = Image.open(detail["image_path"])
            btn_img = btn_img.resize((180, 180), Image.Resampling.LANCZOS)
            photoimg = ImageTk.PhotoImage(btn_img)

            btn = Button(bg_img, image=photoimg, cursor="hand2")
            btn.image = photoimg  # Keep a reference!
            btn.place(x=detail["x"], y=detail["y"], width=180, height=180)

            btn_lbl = Button(bg_img, text=detail["text"], cursor="hand2", font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
            btn_lbl.place(x=detail["x"], y=detail["y"] + 180, width=180, height=45)

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()

