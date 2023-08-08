import tkinter as tk
from tkinter.ttk import Progressbar
import os, json


root = tk.Tk()
root.title("Tkinter Rapid Development")
root.geometry("640x320")

new_window = tk.Toplevel(root)
new_window.title("Property")
new_window.geometry(f"320x300")#125x420+0+80
new_window.attributes("-topmost", True)
new_window.attributes("-toolwindow", 1)

# Create a dictionary to store widget information
widget_info = {}
widgets = {}  # Use a single dictionary to store widgets of different types
widget_count = {}  # Use a dictionary to store counts for different widget types

_count = 0



def on_button_press(event, widget):
    widget.is_dragging = True
    widget.start_x = event.x_root - widget.winfo_x()
    widget.start_y = event.y_root - widget.winfo_y()
    # print(widgets)
    print(widget_info)

def on_button_drag(event, widget):
    if widget.is_dragging:
        new_x = event.x_root - widget.start_x
        new_y = event.y_root - widget.start_y
        widget.place(x=new_x, y=new_y)

def on_button_release(event, widget, widget_dict):
    widget.is_dragging = False
    update_widget_position(widget, widget_dict)
    print(widget_info)
    

def instantiate_widget(widgetType, count_key, dict_widget):
    global _count
    _count += 1

    widgetType.place(x=root.winfo_width() // 2, y=root.winfo_height() // 2, anchor="center")

    widgetType.is_dragging = False
    widgetType.start_x = 0
    widgetType.start_y = 0

    # Add widget's initial position to widget_info dictionary
    widget_id = _count
    widget_info[widget_id] = (widgetType.winfo_x(), widgetType.winfo_y())

    widgetType.bind("<ButtonPress-1>", lambda event, widget=widgetType: on_button_press(event, widget))
    widgetType.bind("<B1-Motion>", lambda event, widget=widgetType: on_button_drag(event, widget))
    widgetType.bind("<ButtonRelease-1>", lambda event, widget=widgetType: on_button_release(event, widget, dict_widget))

    widget_count[count_key] = _count
    dict_widget[_count] = widgetType

def update_widget_position(widgetType, widget_dict):
    global widget_type_name, widget_id
    position = (widgetType.winfo_x(), widgetType.winfo_y())
    widget_type_name = type(widgetType).__name__
    widget_id = list(widget_dict.keys())[list(widget_dict.values()).index(widgetType)]

    # Update position in properties window
    name_Label = tk.Label(new_window)
    name_Label.config(text=f"{widget_type_name} ID {widget_id}")
    name_Label.place(x=0, y=10)

    # Update widget_info dictionary with new position
    widget_info[widget_type_name] = position

    # print(f"{widget_type_name} ID {widget_id}: {position}")

def instantiate_button():
    new_button = tk.Button(root, text="Dynamic Button")
    instantiate_widget(new_button, 'button', widgets)

def instantiate_label():
    new_label = tk.Label(root, text="Dynamic Label")
    instantiate_widget(new_label, 'label', widgets)

def instantiate_entry():
    new_entry = tk.Entry(root)
    instantiate_widget(new_entry, 'entry', widgets)

def instantiate_progressbar():
    new_bar = Progressbar(root)
    instantiate_widget(new_bar, 'progressbar', widgets)

def instantiate_frame():
    new_frame = tk.Frame(root, bg="red", height=120, width=220)
    instantiate_widget(new_frame, 'frame', widgets)
def save_widget_info_to_file():

    with open("widget_info.json", "w") as json_file:
        json.dump(widget_info, json_file)
    
menu = tk.Menu(root, tearoff = 0)
menu.add_command(label="Generate Python File", command=save_widget_info_to_file)
menu.add_separator()
menu.add_command(label ="New Button", command=instantiate_button)
menu.add_command(label ="New Label", command=instantiate_label)
menu.add_command(label ="New Entry", command=instantiate_entry)
menu.add_separator()
menu.add_command(label ="ProgressBar", command=instantiate_progressbar)
menu.add_separator()
menu.add_command(label ="CheckButton")
menu.add_command(label="RadioButton")
menu.add_command(label="Combobox")
menu.add_separator()
menu.add_command(label="Scale")
menu.add_command(label="Scrollbar")
menu.add_command(label="Frame", command=instantiate_frame)

root.bind("<Button-3>", lambda event: menu.tk_popup(event.x_root, event.y_root))



# def resize_widget(event):
#     pass
# root.bind("<Configure>", resize_widget)
root.mainloop()
