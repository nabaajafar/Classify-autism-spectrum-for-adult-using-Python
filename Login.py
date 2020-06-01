from tkinter import *
from tkinter import ttk
import tkinter as tk   
from tkinter import messagebox as mbox 
import sqlite3
from PIL import ImageTk, Image
from Register import r
from tkinter import messagebox as mbox 
from homepage import home


root=Tk()
root.title("Autism Detection System-Sign In")
root.resizable(False,False)
root.geometry("500x490")
root.configure(background='#ffffff')

lbl1= ttk.Label(root,text="Autism Detection System", background='#ffffff', font="Bold 25", foreground="#AFAF1D" )
lbl1.pack(padx=20, pady=20)

usernamelbl=ttk.Label(root,text="Username:", background='#ffffff', font="Bold 15", foreground="#AFAF1D")
usernamelbl.pack(padx=(10,125),pady=5)
usernametext=ttk.Entry(root, width=30, font=('Arial',10))
usernametext.pack(pady=5)

passlbl=ttk.Label(root,text="Password:", background='#ffffff', font="Bold 15", foreground="#AFAF1D")
passlbl.pack(padx=(10,125),pady=5)
passtext=ttk.Entry(root, width=30, font=('Arial',10))
passtext.config(show="*")
passtext.pack(pady=5)

loginbtn=Button(root, text="Sign In", bg='#AFAF1D', fg='#ffffff', font="Bold 10",  relief='flat', borderwidth=5)
loginbtn.pack(pady=5)

def onclick():

         conn=sqlite3.connect("DBMAs.db")
         c=conn.cursor()   
        
         c.execute("SELECT * FROM USER WHERE(username = '"  +str(usernametext.get()) + "' AND  password ='"  +str(passtext.get())+ "' )")
         
         resl = c.fetchone()
         if resl:
             root.withdraw()
             for i in resl:
                conn.commit()
                conn.close()
                home(usernametext.get())
                root.mainloop()
                break
         #elif usernametext and not usernametext.isspace() and passtext and not passtext.isspace():
         else:       
             err = tk.Tk()  
             err.title("Error")   
             ttk.Label(err, text="Please try again").grid(column=0,row=0,padx=20,pady=30)

loginbtn.config(command=onclick)
             
regbtn=Button(root, text="Sign Up", bg='#AFAF1D', fg='#ffffff', font="Bold 10",  relief='flat', borderwidth=3)
regbtn.pack(pady=5)
img = ImageTk.PhotoImage(Image.open("icon.png"))
panel = Label(root, image = img)
panel.pack()

def signup():
    sign=r()

def homepage():
    root.withdraw()
    go = home()

regbtn.config(command=signup)
root.mainloop()

