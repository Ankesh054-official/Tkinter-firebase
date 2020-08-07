import socket,tkinter
from tkinter import messagebox


def check_internet():
	#Check Internet is conected or not
	global IPaddress,x
	IPaddress = socket.gethostbyname(socket.gethostname())
	if IPaddress == "127.0.0.1":
		print("offline ")
		return messagebox.showerror('No Internet', "Check your internet connection.")

	elif IPaddress == "127.0.0.2":
		print("offline ")
		return 	messagebox.showerror('No Internet', "Check your internet connection.")

	else:
		print("online")
		return 1