
import tkinter as tk
from tkinter.ttk import Progressbar

root = tk.Tk()
root.title("Your Application")
root.geometry("640x320")
    
def funcButton1():
    pass

Button1 = tk.Button(root, text="Button1", command="funcButton1")
Button1.place(x=42, y=58)

def funcLabel2():
    pass

Label2 = tk.Label(root, text="Label2")
Label2.place(x=52, y=92)

def funcEntry3():
    pass

Entry3 = tk.Entry(root)
Entry3.place(x=154, y=91)

def funcProgressbar4():
    pass

Progressbar4 = Progressbar(root)
Progressbar4.place(x=111, y=138)

def funcButton5():
    pass

Button5 = tk.Button(root, text="Button5", command="funcButton5")
Button5.place(x=321, y=83)

def funcEntry6():
    pass

Entry6 = tk.Entry(root)
Entry6.place(x=307, y=54)

def funcLabel7():
    pass

Label7 = tk.Label(root, text="Label7")
Label7.place(x=23, y=139)

def funcEntry8():
    pass

Entry8 = tk.Entry(root)
Entry8.place(x=320, y=160)

root.mainloop()
