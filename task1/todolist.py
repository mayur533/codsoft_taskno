import tkinter as tk
import ttkbootstrap as ttk
import sqlite3
#Defining window ui
root=tk.Tk()
root.geometry("400x400")
style = ttk.Style(theme="darkly")

tasks=ttk.StringVar()
db=sqlite3.connect("todolist.db")
cur=db.cursor()
task=[]
check=[]
cur.execute("create table if not exists list(id integer primary key autoincrement,task text,checked int);")

cur.execute("select * from list;")
result=cur.fetchall()
frame1=ttk.Frame(root,bootstyle="secondary")
for row in result:
	for i in range(row[0]):
		task.append(i)
		check.append(i)
		check_var=ttk.IntVar(row[2])
		
		check[i]=ttk.Checkbutton(frame1,style='success.TCheckbutton',variable=check_var)
		check[i].grid(row=[i],column=0)
		
		tasks.set(row[1])
		task[i]=ttk.Label(frame1,textvariable=tasks)
		task[i].grid(row=i,column=1)
		
		
frame1.pack()

root.mainloop()
