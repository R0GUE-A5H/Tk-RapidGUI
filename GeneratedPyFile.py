
import tkinter as tk
from tkinter.ttk import Progressbar

root = tk.Tk()
root.title("Your Application")
root.geometry("640x320")
    
def funcButton1():
    pass

Button1 = tk.Button(root, text="Button1", command="funcButton1")
Button1.place(x=388, y=75)

def funcButton2():
    pass

Button2 = tk.Button(root, text="Button2", command="funcButton2")
Button2.place(x=393, y=132)

root.mainloop()
