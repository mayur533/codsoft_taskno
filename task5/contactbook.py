import tkinter as tk
from tkinter import *
from tkinter import messagebox
import ttkbootstrap as ttk
import sqlite3
from PIL import Image,ImageTk
db=sqlite3.connect("contacts.db")
con=db.cursor()

con.execute("create table if not exists contact(id integer primary key autoincrement,name varchar(30),number integer,email varchar(50),address text);")

def add_contactfun(head,frame):
    
    head.configure(text="Add Contact")
    frame.destroy()
    frame=ttk.Frame(root)
    frame.pack(padx=10,pady=10)
    lbl1=ttk.Label(frame,text="Name:")
    lbl1.grid(row=0,column=0,pady=10)
    nametxt=ttk.StringVar()
    name=ttk.Entry(frame,textvariable=nametxt)
    name.grid(row=0,column=1,pady=10)
    lbl2=ttk.Label(frame,text="Phone No:")
    lbl2.grid(row=1,column=0,pady=10)
    phonetxt=ttk.IntVar()
    mob_no=ttk.Entry(frame,textvariable=phonetxt)
    mob_no.grid(row=1,column=1,pady=10)
    lbl3=ttk.Label(frame,text="Email:")
    lbl3.grid(row=2,column=0,pady=10)
    emailtxt=ttk.StringVar()
    email=ttk.Entry(frame,textvariable=emailtxt)
    email.grid(row=2,column=1,pady=10)
    lbl4=ttk.Label(frame,text="Address:")
    lbl4.grid(row=3,column=0,pady=10)
    addrtxt=ttk.StringVar()
    address=ttk.Entry(frame,textvariable=addrtxt)
    address.grid(row=3,column=1,pady=10)
    back=ttk.Button(frame,text="back",command=lambda:reset(frame,head))
    back.grid(row=4,column=0,pady=15)
    add_contact=ttk.Button(frame,text="Add Contact",width=18,command=lambda : insert_contact(frame,nametxt.get(),phonetxt.get(),emailtxt.get(),addrtxt.get()))
    add_contact.grid(row=4,column=1,pady=15)

def reset(frame,head):
    head.configure(text="My Contacts")
    frame.destroy()
    main_page()
def insert_contact(frame,n,p,e,a):
    frame.destroy()
    con.execute("insert into contact(name,number,email,address) values(?,?,?,?)",(n,p,e,a))
    db.commit()
    main_page()
   
   

def refresh_tasks(lb):
    lb.delete(0,END)
    con.execute("select * from contact")
    data=con.fetchall()
    for row in data:
        lb.insert(END,row[1]+"\t: "+str(row[2]))
        

def delete_task(lb):
    cont=None
    for i in lb.curselection():
        cont=lb.get(i)
    if cont!=None:     
        res=cont.split("\t: ")
        con.execute("delete from contact where name=? and number=?",(res[0],int(res[1])))
        lb.delete(ANCHOR)
        refresh_tasks(lb)
        db.commit()
    else:
        messagebox.showinfo("Delete", "Please select a Contact to Delete")

def update(res,frame,n,p,e,a):
    
    con.execute("update contact set name=? , number=?, email=?, address=? where name=? and number=?",(n,p,e,a,res[0],res[1]))
    frame.destroy()
    db.commit()
    main_page()
    
def update_task(lb,frame):
    cont=None
    for i in lb.curselection():
        cont=lb.get(i)
    if cont!=None:   
        res=cont.split("\t: ")
        head.configure(text="Update Contact")
        frame.destroy()
        frame=ttk.Frame(root)
        frame.pack(padx=10,pady=10)
        lbl1=ttk.Label(frame,text="Name:")
        lbl1.grid(row=0,column=0,pady=10)
        nametxt=ttk.StringVar()
        name=ttk.Entry(frame,textvariable=nametxt)
        name.grid(row=0,column=1,pady=10)
        lbl2=ttk.Label(frame,text="Phone No:")
        lbl2.grid(row=1,column=0,pady=10)
        phonetxt=ttk.IntVar()
        mob_no=ttk.Entry(frame,textvariable=phonetxt)
        mob_no.grid(row=1,column=1,pady=10)
        lbl3=ttk.Label(frame,text="Email:")
        lbl3.grid(row=2,column=0,pady=10)
        emailtxt=ttk.StringVar()
        email=ttk.Entry(frame,textvariable=emailtxt)
        email.grid(row=2,column=1,pady=10)
        lbl4=ttk.Label(frame,text="Address:")
        lbl4.grid(row=3,column=0,pady=10)
        addrtxt=ttk.StringVar()
        address=ttk.Entry(frame,textvariable=addrtxt)
        address.grid(row=3,column=1,pady=10)
        con.execute("select * from contact where name=? and number=?",(res[0],int(res[1])))
        data=con.fetchall()
        for row in data:
            
            nametxt.set(row[1])
            phonetxt.set(row[2])
            emailtxt.set(row[3])
            addrtxt.set(row[4])
        back=ttk.Button(frame,text="back",command=lambda:reset(frame,head))
        back.grid(row=4,column=0,pady=15)
        add_contact=ttk.Button(frame,text="Update Contact",width=18,command=lambda : update(res,frame,nametxt.get(),phonetxt.get(),emailtxt.get(),addrtxt.get()))
        add_contact.grid(row=4,column=1,pady=15)
    else:
        messagebox.showinfo("Uodate", "Please select a Contact to Update")

def search1(s,lb):
    lb.delete(0,END)
    con.execute("select * from contact where name like ? or number like ?;",(f'%{s.get()}%',f'%{s.get()}%'))
    data=con.fetchall()
    for row in data:
        lb.insert(END,row[1]+"\n"+str(row[2]))
        print(row)



root=tk.Tk()
root.geometry("570x360")
root.title("Contact Book")
theme=ttk.Style(theme="darkly")
head=ttk.Label(root,text="My Contacts",font=('arial',20),bootstyle="warning")
head.pack(anchor="center",pady=10)
def main_page():
    
    frame=ttk.Frame(root)
    frame.pack(padx=10,pady=5)
    lb = Listbox(
        frame,
        width=28,
        height=11,
        font=('Times', 18),
        bd=0,
        fg='#464646',
        highlightthickness=0,
        selectbackground='#a6a6a6',
        activestyle="none", 
    )
    lb.grid(rowspan=4,column=0)

    

    searchtxt=ttk.StringVar()
    searchbar=ttk.Entry(frame,width=13,textvariable=searchtxt)
    searchbar.grid(padx=4,row=0,column=1)
    search=ttk.Button(frame,text="Search",command=lambda:search1(searchtxt,lb),width=5)
    search.grid(row=0,column=2)

    update=ttk.Button(frame,text="Update Contact",width=20,command=lambda:update_task(lb,frame))
    update.grid(padx=8,row=1,column=1,columnspan=2)

    delete=ttk.Button(frame,text="Delete Contact",width=20,command=lambda:delete_task(lb))
    delete.grid(padx=8,row=2,column=1,columnspan=2)

    add_contact=ttk.Button(frame,text="Add Contact",width=20,command=lambda : add_contactfun(head,frame))
    add_contact.grid(padx=8,row=3,column=1,columnspan=2)
    refresh_tasks(lb)

main_page()

root.mainloop()