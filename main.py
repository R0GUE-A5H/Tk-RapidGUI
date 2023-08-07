import tkinter as tk

root = tk.Tk()
root.title("Tkinter Rapid Development")
root.geometry("640x320")

new_window = tk.Toplevel(root)
new_window.title("Tool Window")
new_window.geometry("125x420+0+80")
new_window.attributes("-topmost", True)
new_window.attributes("-toolwindow", 1)

buttons = {}
button_count = 0

def on_button_press(event, button):
    button.is_dragging = True
    button.start_x = event.x_root - button.winfo_x()
    button.start_y = event.y_root - button.winfo_y()

def on_button_drag(event, button):
    if button.is_dragging:
        new_x = event.x_root - button.start_x
        new_y = event.y_root - button.start_y
        button.place(x=new_x, y=new_y)

def on_button_release(event, button):
    button.is_dragging = False
    update_button_position(button)

def instantiate_button():
    global button_count
    button_count += 1

    new_button = tk.Button(root, text="Dynamic Button")
    new_button.place(x=root.winfo_width() // 2, y=root.winfo_height() // 2, anchor="center")
    new_button.winfo_y
    new_button.is_dragging = False
    new_button.start_x = 0
    new_button.start_y = 0

    new_button.bind("<ButtonPress-1>", lambda event, button=new_button: on_button_press(event, button))
    new_button.bind("<B1-Motion>", lambda event, button=new_button: on_button_drag(event, button))
    new_button.bind("<ButtonRelease-1>", lambda event, button=new_button: on_button_release(event, button))

    buttons[button_count] = new_button

def update_button_position(button):
    position = (button.winfo_x(), button.winfo_y())
    print(f"Button ID {button_count}: {position}")

button_create = tk.Button(new_window, text="New Button", command=instantiate_button)
button_create.place(x=15, y=10)

label_create = tk.Button(new_window, text="New Label", command=instantiate_button)
label_create.place(x=15, y=40)




root.mainloop()
