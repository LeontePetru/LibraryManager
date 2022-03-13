import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import os


root = tk.Tk()
root.geometry('1280x720')

background_image = tk.PhotoImage(file='.\Images\LogIn.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1,relheight=1)

font = tkFont.Font(family="Times New Roman",size=16,weight="bold")

userEntry=tk.Entry(bg="#cccccc",font=font)
userEntry.place(relx=0.65,rely=0.525,relheight=0.06,relwidth=0.23)

passwordEntry=tk.Entry(bg="#cccccc",font=font)
passwordEntry.place(relx=0.65,rely=0.68,relheight=0.06,relwidth=0.23)

def buttonLogInFunc():
    print(userEntry.get())
    print(passwordEntry.get())

def Guest():
    root.quit()
    os.system('BookInventoryGUI.py')
    #root.destroy()


logInButton=tk.Button(bg="#cccccc",font=font,text="Log In",command=buttonLogInFunc,foreground="#ff6366")
logInButton.place(relx=0.675,rely=0.77,relheight=0.06,relwidth=0.18)

guestButton=tk.Button(bg="#cccccc",font=font,text="Continue as Guest",command=Guest,foreground="#ff6366")
guestButton.place(relx=0.675,rely=0.86,relheight=0.06,relwidth=0.18)

#passwordEntry.pack()


root.mainloop()