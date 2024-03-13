import tkinter as tk 
from tkinter import messagebox
import ttkbootstrap as ttk
import sqlite3
import random
import string

def generate_password(ap,pa):
    if appname.get() != "" and passlength.get() > 6 :
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(passlength.get()))
        genpass.set(password)
    else:
        messagebox.showinfo("Error","Please Provide Valid Inputs")
    con.execute("insert into passtable(appname,passwd) values(?,?)",(appname.get(),password))
    db.commit()
    
    
def show_passwd_win(appname):
    lbl2.destroy()
    ent2.destroy()
    frame3.destroy()
    appname.set("")
    genpass.set("")
    btn1=ttk.Button(root,text="Show Password",command=lambda :show_password(appname))
    btn1.pack(padx=10,pady=10)

def show_password(appname):
    con.execute("select * from passtable")
    res=con.fetchall()
    for row in res:
        if(row[1]==appname.get()):
            genpass.set(row[2])

db=sqlite3.connect("pass.db")
con=db.cursor()
con.execute("create table if not exists passtable(id integer auto increment,appname text,passwd text);")

root=tk.Tk()
root.title("Password Generator")
root.geometry("500x250")
theme=ttk.Style(theme="darkly")
hdlbl=ttk.Label(root,text="Password Generator",bootstyle="success",font=("Calibri",20))
hdlbl.pack(pady=10)

frame1=ttk.Frame(root)
frame1.pack(pady=10)

lbl1=ttk.Label(frame1,text="Enter App/Site Name :",font=("Calibri",15),anchor="w")
lbl1.grid(row=0,column=0,pady=5)

appname=ttk.StringVar()

ent1=ttk.Entry(frame1,textvariable=appname)
ent1.grid(row=0,column=1,pady=5)

lbl2=ttk.Label(frame1,text="Enter Password Length :",font=("Calibri",15),anchor="w")
lbl2.grid(row=1,column=0,pady=5)

passlength=ttk.IntVar()

ent2=ttk.Entry(frame1,textvariable=passlength)
ent2.grid(row=1,column=1,pady=5)
genpass=ttk.StringVar()
passent=ttk.Entry(root,textvariable=genpass)
passent.pack()

frame3=ttk.Frame(root)
frame3.pack()

btn=ttk.Button(frame3,text="Generate Password",command=lambda :generate_password(appname,passlength))
btn.pack(side="left",pady=10)
btn1=ttk.Button(frame3,text="Show Password",command=lambda :show_passwd_win(appname))
btn1.pack(padx=10,pady=10)

root.mainloop()