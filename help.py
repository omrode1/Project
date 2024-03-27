from tkinter import *

from PIL import Image, ImageTk


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Help")

        title_lbl = Label(self.root, text="Help",
                          font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Image 1
        img = Image.open("./college_images/1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img = img.resize((1530, 720), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=55, width=1530, height=720)

        dep_label = Label(f_lbl, text="Email:ylohi31@gmail.com", font=("times new roman", 20, "bold"), bg="white")
        dep_label.place(x=550, y=220)


if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()