import pyrebase
from tkinter import messagebox
from Guis import main_frame

"""chdir,getcwd,rmdir"""

def login(frame1,Email,Password):
    firebaseConfig = {
        "apiKey": "AIzaSyCPCLf2oLLfXY-gzzGiR8JH4l9Z1EO_BqU",
        "authDomain": "python-tkinter-login.firebaseapp.com",
        "databaseURL": "https://python-tkinter-login.firebaseio.com",
        "projectId": "python-tkinter-login",
        "storageBucket": "python-tkinter-login.appspot.com",
        "messagingSenderId": "323517919210",
        "appId": "1:323517919210:web:cc72da9dfc9ea80d188c93",
        "measurementId": "G-PLX0C2HTR5"
    }
    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()
    try:
        login = auth.sign_in_with_email_and_password(email=Email, password=Password)
        #divert to the little brother console
        frame1.destroy()
        main_frame.main_frame(frame1, Email)
    except:
        return messagebox.showerror("SIGNIN_INVALID","Maybe, INVALID_EMAIL\nor\nINVALID_PASSWORD")
    # auth.send_email_verification(login["idToken"])


def create_ac(frame1,Email,Password):
    firebaseConfig = {
        "apiKey": "AIzaSyCPCLf2oLLfXY-gzzGiR8JH4l9Z1EO_BqU",
        "authDomain": "python-tkinter-login.firebaseapp.com",
        "databaseURL": "https://python-tkinter-login.firebaseio.com",
        "projectId": "python-tkinter-login",
        "storageBucket": "python-tkinter-login.appspot.com",
        "messagingSenderId": "323517919210",
        "appId": "1:323517919210:web:cc72da9dfc9ea80d188c93",
        "measurementId": "G-PLX0C2HTR5"
    }
    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()
    user = auth.create_user_with_email_and_password(email=Email, password=Password)
    # login = auth.sign_in_with_email_and_password(email=email,password=password)
    auth.send_email_verification(id_token=user['idToken'])
    frame1.destroy()
    main_frame.main_frame(frame1, Email)


def terms_and_conditions():
        print("terms & conditions")#terms and conditions
def forgotpassword(email):
    firebaseConfig = {
        "apiKey": "AIzaSyCPCLf2oLLfXY-gzzGiR8JH4l9Z1EO_BqU",
        "authDomain": "python-tkinter-login.firebaseapp.com",
        "databaseURL": "https://python-tkinter-login.firebaseio.com",
        "projectId": "python-tkinter-login",
        "storageBucket": "python-tkinter-login.appspot.com",
        "messagingSenderId": "323517919210",
        "appId": "1:323517919210:web:cc72da9dfc9ea80d188c93",
        "measurementId": "G-PLX0C2HTR5"
    }
    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()
    try:
        auth.send_password_reset_email(email=email)
        return 1
    except:
        return messagebox.showerror("Not Found","EMAIL_NOT_FOUND")