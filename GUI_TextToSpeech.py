from tkinter import *
from tkinter import messagebox
from tkinter import font
import pyttsx3

engine = pyttsx3.init()
win = Tk()
win.title("SPEAKY")
win.configure(bg="grey")
win.geometry("750x100")

def speech():
    txt=entry1.get()
    engine.say(txt)
    engine.runAndWait()
    engine.stop()
    if(txt==""):
        messagebox.showerror("Error","Please Enter Text")

#lable frame
lf = LabelFrame(win,text="Text to Speech".center(110),font="50",fg="red")
lf.pack(fill="both",expand="yes",padx=10,pady=10)
Label(lf,text="Enter text here",font=30,fg="blue",padx=15).pack(side=LEFT)

#entry---user enter his/her text
text=StringVar()
entry1=Entry(lf,width=35,bd=5,font=18,textvariable=text,fg="purple")
entry1.pack(side=LEFT,padx=10)

#button
Button(lf,width=9,bd=1,text="Speak",font=15,command=speech,fg="brown").pack(side=LEFT)

mainloop()

