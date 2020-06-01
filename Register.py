from tkinter import *
from tkinter import ttk
import sqlite3
from homepage import home
from PIL import ImageTk, Image
# from db import db

def r():
    root = Toplevel()
    root.title("Autism Detection System-Sign Up")
    root.resizable(False, False)
    root.geometry("500x490")
    root.configure(background='#ffffff')
    lbl1 = ttk.Label(root, text="Autism Detection System", background='#ffffff', font="Bold 25",
                         foreground="#AFAF1D")
    lbl1.pack(padx=20, pady=20)
    namelbl= ttk.Label(root, text="Username:", background='#ffffff', font="Bold 10",
                         foreground="#AFAF1D") 
    namelbl.pack(padx=(10, 160), pady=5)
    nametext = ttk.Entry(root, width=30, font=('Arial', 10))
    nametext.pack(pady=5)
    
 
    passwordlbl = ttk.Label(root, text="Password:", background='#ffffff', font="Bold 10", foreground="#AFAF1D")
    passwordlbl.pack(padx=(10, 160), pady=5)
    passwordtext = ttk.Entry(root, width=30, font=('Arial', 10))
    passwordtext.config(show="*")
    passwordtext.pack(pady=5)
    confpasslbl = ttk.Label(root, text="Confirm Password:", background='#ffffff', font="Bold 10", foreground="#AFAF1D")
    confpasslbl.pack(padx=(10, 119), pady=5)
    confpasstext = ttk.Entry(root, width=30, font=('Arial', 10))
    confpasstext.config(show="*")
    confpasstext.pack(pady=5)
    emaillbl = ttk.Label(root, text="Email:", background='#ffffff', font="Bold 10",
                                   foreground="#AFAF1D")
    emaillbl.pack(padx=(10, 180), pady=5)
    emailtext = ttk.Entry(root, width=30, font=('Arial', 10))
    emailtext.pack(pady=5)
    relationllbl = ttk.Label(root, text="Relationship:", background='#ffffff', font="Bold 10",
                             foreground="#AFAF1D")
    relationllbl.pack(padx=(10, 150), pady=5)
    relationtext = ttk.Entry(root, width=30, font=('Arial', 10))
    relationtext.pack(pady=5)
    signup = Button(root, text="Sign Up", bg='#AFAF1D', fg='#ffffff', font="Bold 10", relief='flat', borderwidth=3)
    signup.pack(pady=5)



    def onclick():
      #   print('working...')
      # #  signup.onclick()
         conn=sqlite3.connect("DBMAs.db")
         c=conn.cursor()
         c.execute("INSERT INTO USER VALUES('"  +str(nametext.get()) + "','" +str(passwordtext.get())+"', '"+str(emailtext.get())+"', '"+str(relationtext.get())+ "' )")
      # #  db.execute("insert into user (username,password,email,rel) values(?,?,?,?)", (nametext,passwordtext, emailtext, relationtext))
      #   db.execute("""INSERT INTO user(username, password, email, rel) VALUES (?,?,?,?)""", ('nametext','passwordtext', 'emailtext', 'relationtext'))
         conn.commit()
         conn.close()
         home(nametext.get())
         root.mainloop()
    signup.config(command=onclick)
    
#def login():
 #       root.withdraw()

  #  signup.config(command=login)
 #   root.mainloop()

