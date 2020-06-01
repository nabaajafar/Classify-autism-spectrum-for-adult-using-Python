from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from ML import machineLearning
import sqlite3

def home(user):
    root = Toplevel()
    root.title("Autism Detection System-Home Page")
    root.resizable(False, False)
    root.geometry("500x490")
    root.configure(background='#ffffff')

    nam=user;
    lbl1 = ttk.Label(root, text="Welcome", background='#ffffff', font="Bold 25",
                         foreground="#AFAF1D")
    lbl1.pack(padx=20, pady=20)
    img = ImageTk.PhotoImage(Image.open("icon3.png"))
    panel = Label(root, image=img)
    panel.pack(pady=20)

    exambtn = Button(root, text="Take Exam", bg='#AFAF1D', fg='#ffffff', font="Bold 15", relief='flat', borderwidth=3)
    exambtn.pack(pady=5)

    resultbtn = Button(root, text="See previous results", bg='#AFAF1D', fg='#ffffff', font="Bold 15", relief='flat', borderwidth=3)
    resultbtn.pack(pady=5)

    logouttbtn = Button(root, text="Logout", bg='#AFAF1D', fg='#ffffff', font="Bold 15", relief='flat',
                       borderwidth=3)
    logouttbtn.pack(pady=5)

    def e():
        root.withdraw()
        e=exam(nam)

    def res():
        root.withdraw()
        r=result(nam)

    def d():
        root.destroy()
        exit()

    exambtn.config(command=e)
    resultbtn.config(command=res)
    logouttbtn.config(command=d)
    root.mainloop()

def result(nam):
    root = Toplevel()
    root.title("Autism Detection System-Result")
    root.resizable(False, False)
    root.configure(background='#ffffff')
    conn = sqlite3.connect("DBMAs.db")
    name=nam
    img = ImageTk.PhotoImage(Image.open("icon2.png"))
    panel = Label(root, image=img)
    panel.pack(pady=20)

    cursor = conn.cursor()
    sqlite_select_query ="SELECT * FROM CHILD WHERE username = '" +str(name)+"' "
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    for row in records:
        if(row[3]=="[1]"):
            v="Yes"
        if(row[3]=="[0]"):
            v="No"
        userlbl=ttk.Label(root, text="Username: "+row[0]+"      Child name: "+row[1]+"      Age: "+row[2]+"     Result: "+v
                          , background='#ffffff', font="Bold 10", foreground="#AFAF1D")
        userlbl.pack(pady=10)


    homebtn = Button(root, text="Home", bg='#AFAF1D', fg='#ffffff', font="Bold 12", relief='flat',
                       borderwidth=3)
    homebtn.pack(pady=5)

    def h():
        root.destroy()
        g=home(name)

    homebtn.config(command=h)
    root.mainloop()
def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

def exam(nam):
    root = Toplevel()
    root.title("Autism Detection System-Exam")
    root.resizable(False, False)
    root.geometry("590x490")
    root.configure(background='#ffffff')
    canvas = Canvas(root, borderwidth=0)
    frame = ttk.Frame(canvas, style='My.TFrame')
    vsb = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)
    vsb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((4, 4), window=frame, anchor="nw")
    frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
    name=nam
    lbl1 = ttk.Label(frame, text="Answer the following questions:", background='#ffffff', font="Bold 15",
                         foreground="#AFAF1D")
    lbl1.pack( pady=10,padx=10)
    
    namelbl = ttk.Label(frame, text="Enter child's name:", background='#ffffff', font="Bold 10",
                       foreground="#AFAF1D")
    namelbl.pack(pady=5)
    nametxt = ttk.Entry(frame, font=('Arial', 10))
    nametxt.pack(pady=5)
    agelbl=ttk.Label(frame, text="Enter child's age:", background='#ffffff', font="Bold 10",
                         foreground="#AFAF1D")
    agelbl.pack(pady=5)
    agetxt=ttk.Entry(frame, font=('Arial',10))
    agetxt.pack(pady=5)

    style = ttk.Style()
    style.configure("TRadiobutton", background="#ffffff", foreground="#737373")
    style.configure('My.TFrame', background='#ffffff')

    q1lbl = ttk.Label(frame, text="Does the person avoid meeting eyes?", background='#ffffff', font="Bold 10",
                       foreground="#AFAF1D")
    q1lbl.pack(pady=5)
    Spanq1 = StringVar()
    q1yes=ttk.Radiobutton(frame, text="Yes", variable=Spanq1, value=1)
    q1no = ttk.Radiobutton(frame, text="No", variable=Spanq1, value=0)
    q1yes.pack(pady=5)
    q1no.pack(pady=5)

    q2lbl = ttk.Label(frame, text="Does the person vibrates forward and backward while standing and sitting?", background='#ffffff', font="Bold 10",
                      foreground="#AFAF1D")
    q2lbl.pack(pady=5)
    Spanq2 = StringVar()
    q2yes = ttk.Radiobutton(frame, text="Yes", variable=Spanq2, value=1)
    q2no = ttk.Radiobutton(frame, text="No", variable=Spanq2, value=0)
    q2yes.pack(pady=5)
    q2no.pack(pady=5)

    q3lbl = ttk.Label(frame, text="Is the person's response inappropriate for simple orders?",
                      background='#ffffff', font="Bold 10",
                      foreground="#AFAF1D")
    q3lbl.pack(pady=5)
    Spanq3 = StringVar()
    q3yes = ttk.Radiobutton(frame, text="Yes", variable=Spanq3, value=1)
    q3no = ttk.Radiobutton(frame, text="No", variable=Spanq3, value=0)
    q3yes.pack(pady=5)
    q3no.pack(pady=5)

    q4lbl = ttk.Label(frame, text="Does the person realize the presence of people around him/her?",
                      background='#ffffff', font="Bold 10",
                      foreground="#AFAF1D")
    q4lbl.pack(pady=5)
    Spanq4 = StringVar()
    q4yes = ttk.Radiobutton(frame, text="Yes", variable=Spanq4, value=1)
    q4no = ttk.Radiobutton(frame, text="No", variable=Spanq4, value=0)
    q4yes.pack(pady=5)
    q4no.pack(pady=5)

    q5lbl = ttk.Label(frame, text="Does the person look at the vast space a lot?",
                      background='#ffffff', font="Bold 10",
                      foreground="#AFAF1D")
    q5lbl.pack(pady=5)
    Spanq5 = StringVar()
    q5yes = ttk.Radiobutton(frame, text="Yes", variable=Spanq5, value=1)
    q5no = ttk.Radiobutton(frame, text="No", variable=Spanq5, value=0)
    q5yes.pack(pady=5)
    q5no.pack(pady=5)

    q6lbl = ttk.Label(frame, text="Does the person seem deaf to some voices while responding to other voices?",
                      background='#ffffff', font="Bold 10",
                      foreground="#AFAF1D")
    q6lbl.pack(pady=5)
    Spanq6 = StringVar()
    q6yes = ttk.Radiobutton(frame, text="Yes", variable=Spanq6, value=1)
    q6no = ttk.Radiobutton(frame, text="No", variable=Spanq6, value=0)
    q6yes.pack(pady=5)
    q6no.pack(pady=5)

    q7lbl = ttk.Label(frame, text="Does the person use inappropriate pronouns?",
                      background='#ffffff', font="Bold 10",
                      foreground="#AFAF1D")
    q7lbl.pack(pady=5)
    Spanq7 = StringVar()
    q7yes = ttk.Radiobutton(frame, text="Yes", variable=Spanq7, value=1)
    q7no = ttk.Radiobutton(frame, text="No", variable=Spanq7, value=0)
    q7yes.pack(pady=5)
    q7no.pack(pady=5)

    q8lbl = ttk.Label(frame, text="Does the person do things repeatedly as if they were rituals?",
                      background='#ffffff', font="Bold 10",
                      foreground="#AFAF1D")
    q8lbl.pack(pady=5)
    Spanq8 = StringVar()
    q8yes = ttk.Radiobutton(frame, text="Yes", variable=Spanq8, value=1)
    q8no = ttk.Radiobutton(frame, text="No", variable=Spanq8, value=0)
    q8yes.pack(pady=5)
    q8no.pack(pady=5)

    q9lbl = ttk.Label(frame, text="Is the person unemotional or unfriendly,  does not give an emotional response to hugs or kisses?",
                      background='#ffffff', font="Bold 10",
                      foreground="#AFAF1D")
    q9lbl.pack(pady=5)
    Spanq9 = StringVar()
    q9yes = ttk.Radiobutton(frame, text="Yes", variable=Spanq9, value=1)
    q9no = ttk.Radiobutton(frame, text="No", variable=Spanq9, value=0)
    q9yes.pack(pady=5)
    q9no.pack(pady=5)

    q10lbl = ttk.Label(frame, text="Does the person make constant gestures and signals?",
                       background='#ffffff', font="Bold 10",
                       foreground="#AFAF1D")
    q10lbl.pack(pady=5)
    Spanq10 = StringVar()
    q10yes = ttk.Radiobutton(frame, text="Yes", variable=Spanq10, value=1)
    q10no = ttk.Radiobutton(frame, text="No", variable=Spanq10, value=0)
    q10yes.pack(pady=5)
    q10no.pack(pady=5)

    q11lbl = ttk.Label(frame, text="Is jundice?",
                       background='#ffffff', font="Bold 10",
                       foreground="#AFAF1D")
    q11lbl.pack(pady=5)
    Spanq11 = StringVar()
    q11yes = ttk.Radiobutton(frame, text="Yes", variable=Spanq11, value=1)
    q11no = ttk.Radiobutton(frame, text="No", variable=Spanq11, value=0)
    q11yes.pack(pady=5)
    q11no.pack(pady=5)

    q12lbl = ttk.Label(frame, text="Is autism?",
                       background='#ffffff', font="Bold 10",
                       foreground="#AFAF1D")
    q12lbl.pack(pady=5)
    Spanq12 = StringVar()
    q12yes = ttk.Radiobutton(frame, text="Yes", variable=Spanq12, value=1)
    q12no = ttk.Radiobutton(frame, text="No", variable=Spanq12, value=0)
    q12yes.pack(pady=5)
    q12no.pack(pady=5)

    resultbtn = Button(frame, text="Check the Results", bg='#AFAF1D', fg='#ffffff', font="Bold 10", relief='flat',
                       borderwidth=3)
    resultbtn.pack(pady=10)

    def res():
        machineLearning(name,nametxt.get(),Spanq1.get(),Spanq2.get(),Spanq3.get(),Spanq4.get(),Spanq5.get(),
                        Spanq6.get(),Spanq7.get(),Spanq8.get(),Spanq9.get(),Spanq10.get(),
                        agetxt.get(),Spanq11.get(), Spanq12.get())
        root.withdraw()
            
        r=result(name)

    resultbtn.config(command=res)
    root.mainloop()
    