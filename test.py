import tkinter as tk

def resize_button(event):
    new_width = button.winfo_width() + event.x - start_x
    new_height = button.winfo_height() + event.y - start_y
    button.config(width=new_width, height=new_height)

    # Update the starting position
    start_x = event.x
    start_y = event.y

def start_resize(event):
    global start_x, start_y
    start_x = event.x
    start_y = event.y

root = tk.Tk()
root.title("Resize Button Example")

button = tk.Button(root, text="Resize Me", width=10, height=3)
button.pack()

button.bind("<Button-1>", start_resize)
button.bind("<B1-Motion>", resize_button)

root.mainloop()
