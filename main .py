   
from tkinter import *
import pyscreenrec

root = Tk()
root.title("Screen Recorder")
root.geometry("400x600")
root.resizable(0, 0)
root.config(bg="#fff")
rec = pyscreenrec.ScreenRecorder()


def start_rec():
    file = filename.get()
    rec.start_recording(str(file + ".mp4"), 5)


def pause_rec():
    rec.pause_recording()


def resume_rec():
    rec.resume_recording()


def stop_rec():
    rec.stop_recording()


# -------------------icon--------------------------
image_icon = PhotoImage(file="icon.png")
root.iconphoto(False, image_icon)

# -----------------Background----------------------

image1 = PhotoImage(file="yelllow.png")
Label(root, image=image1, bg="#fff").place(x=2, y=35)

image2 = PhotoImage(file="blue.png")
Label(root, image=image2, bg="#fff").place(x=223, y=200)

# ----------------Heading--------------------
lbl = Label(root, text="Screen Recorder", bg="#fff", font="arial 15 bold")
lbl.pack(pady=20)

image3 = PhotoImage(file="recording.png")
Label(root, image=image3, bd=0).pack(pady=30)

#  entry

filename = StringVar()
entry = Entry(root, textvariable=filename, width=16, font="arial 10")
entry.place(x=100, y=350)

filename.set("recording")

# Buttons

start = Button(root, text="Start", font="arial 15", bd=0, relief=GROOVE, command=start_rec)
start.place(x=140, y=258)

image4 = PhotoImage(file="pause.png")
pause = Button(root, image=image4, bd=0, bg="#fff", command=pause_rec)
pause.place(x=50, y=450)

image5 = PhotoImage(file="resume.png")
resume = Button(root, image=image5, bd=0, bg="#fff", command=resume_rec)
resume.place(x=150, y=450)

image6 = PhotoImage(file="stop.png")
stop = Button(root, image=image6, bd=0, bg="#fff", command=stop_rec)
stop.place(x=250, y=450)

root.mainloop()
