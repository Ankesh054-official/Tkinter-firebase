""" # Main Console
   Designed By : ANKESH"""
from tkinter import *

def main_frame(self,Email):
    self=Tk()
    p1 = PhotoImage(file='../res/bit.png')
    self.iconphoto(False, p1)
    self.title("Tklogin-Firebase")
    self.geometry("1200x900")
    self.minsize(980, 660)
    self.config(bg="black")
    img = PhotoImage(file="../res/canvalogo1.png")
    label = Label(self, image=img)
    label.place(x=5, y=-1)
    lb = Label(self, text="WELCOME {0}".format(Email.split("@")[0].upper()),  bg="black", fg="white",
               font=("comicsansms",30,"bold"),relief=FLAT).place(x=140, y=300)
    self.mainloop()