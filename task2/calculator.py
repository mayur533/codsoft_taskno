from tkinter import *
import ttkbootstrap as ttk



def button_click(number):
	if number=="^":
		number="**"
	current_text = eqn.get()
	eqn.set(current_text + str(number))

def clear():
    eqn.set("")
    
def back():
	val=''
	temp=list(eqn.get())
	temp.pop(-1)
	for l in temp:
		val+=l
	eqn.set(str(val))
    
def calculate():
    eqn1=eqn.get()
    try:
        result = eval(eqn1)
        eqn.set(str(result))
    except:
        eqn.set("Error")
    store_prev(eqn1)

def store_prev(eqn1):
     hist.set(eqn1)


root = Tk()
root.geometry('320x376')
root.title("Basic Calculator")
style = ttk.Style(theme='darkly')
hist=ttk.StringVar()
eqn=ttk.StringVar()
lbl=ttk.Label(root,text="",textvariable=hist,font=("Calibri",14),bootstyle="secondary",width=10,anchor="e")
lbl.grid(row=0,column=2,columnspan=2,pady=10)
ent=ttk.Entry(root,textvariable=eqn,font=('Calibri', 20, 'bold'),width=15,justify="right")
ent.grid(row=1, columnspan=4, pady=10, padx=10)

buttons = [
    ["C","%","^","<"],
    [1, 2, 3, "+"],
    [4, 5, 6, "-"],
    [7, 8, 9, "*"],
    [0, ".", "=", "/"]
]

for i in range(5):
    for j in range(4):
        if buttons[i][j] == "=":
            button = ttk.Button(root, text=f"{buttons[i][j]}",width=4, bootstyle='warning', command=calculate)
        elif buttons[i][j] == "C":
            button = ttk.Button(root, text=f"{buttons[i][j]}",width=4, bootstyle='danger', command=clear)
        elif buttons[i][j] == "<":
            button = ttk.Button(root, text=f"{buttons[i][j]}",width=4, bootstyle='info', command=back)
        else:
            button = ttk.Button(root, text=f"{buttons[i][j]:^3}",width=4, bootstyle='success', command=lambda num=buttons[i][j]: button_click(num))
        button.grid(row=i + 2, column=j, padx=0, pady=10)


root.mainloop()