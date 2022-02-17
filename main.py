#2022/02/17
#Logan Hamton/Tristan Labbez-johnson


from tkinter import *
from functools import partial

def validateLogin(password):
  if(password.get() == ""):
    print("Please enter Password")
  elif (password.get() =="password"):
    print("Correct password")
  else:
    print("Incorrect Userna an Password")
  
  return


#window
tkWindow = Tk()  
tkWindow.geometry('400x250')  
tkWindow.title('AMI day 4')


#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=5)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=6)  





validateLogin = partial(validateLogin, password)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=2, column=4)  

tkWindow.mainloop()# main.py
# Thorin Schmidt
# 02/01/22

'''
My Awesome App

Simple program to demonstrate how to create a login screen and switch frames in a single app.
'''

import tkinter as tk
import sys
from app import Application
#from login import Login

class Root(tk.Tk):
  """Root class"""

  def __init__(self):
    super(Root, self).__init__()
    self.title("My Awesome App")
    self.geometry("300x300")
    app_frame = tk.Frame(root)
    password_frame = tk.Frame(root)

  def change_to_app(self):
    app_frame.pack(fill = 'both', expand = 1)
    login_frame.forget()
  
  
  def login_fail(self):
    sys.exit()
  
# main
# The frames are called login_frame, and app_frame
# I'm pretty sure you can figure out which is which
# Check the announcements channel for linksto helpful
# resources.