""" # Facing window/Welcome Screen
   Designed By : ANKESH"""
from tkinter import *
from core import layout_decision,loading


def lay(frame1):
    # frame1.overrideredirect(True)
    p1 = PhotoImage(file='res/bit.png')
    frame1.iconphoto(False,p1)
    frame1.title("Little Brother")
    def ch():
        # Check Internet is conected or not,raise error accordingly.
        if loading.check_internet()!=1:
            ch()
    ch()
    btn1 = Button(frame1, activebackground="black", activeforeground="white", text="Register",
                  font=("comicsansms", 12, "bold"),
                  relief=SUNKEN, borderwidth=3,
                  command=lambda frame1=frame1: layout_decision.create_lay(frame1, "Create Account")).place(x=115,
                                                                                                            y=100)
    btn2 = Button(frame1, activebackground="black", activeforeground="white", text="SignIn",
                  font=("comicsansms", 12, "bold"),
                  relief=SUNKEN, borderwidth=3,
                  command=lambda frame1=frame1: layout_decision.create_lay(frame1, "SignIn")).place(x=115, y=150)
    btn3 = Button(frame1, activebackground="black", activeforeground="white", text="Forgot Password",
                  font=("comicsansms", 12, "bold"),
                  relief=SUNKEN, borderwidth=3,
                  command=lambda frame1=frame1: layout_decision.create_lay(frame1, "Forgot Password")).place(x=115, y=200)


root = Tk()
root.minsize(713,398)
root.maxsize(713,398)
root.config(bg="black")
img = PhotoImage(file="res/canvalogo.png")
label = Label(root, image=img)
label.place(x=-1, y=-1)
# photo = PhotoImage(file="res/back.png")     background image
# x_lable = Label(image=photo)
# Label.pack(self=x_lable)
lay(root)
root.mainloop()