import tkinter as tk
from tkinter.ttk import Progressbar
import os, json


root = tk.Tk()
root.title("Tkinter Rapid Development")
root.geometry("640x320")

# property_win = tk.Toplevel(root)
# property_win.title("Property")
# property_win.geometry(f"320x300")#125x420+0+80
# property_win.attributes("-topmost", True)
#= property_win.attributes("-toolwindow", 1)

# Create a dictionary to store widget information
widget_info = {}
widgets = {}  # Use a single dictionary to store widgets of different types
widget_count = {}  # Use a dictionary to store counts for different widget types

_count = 0

def on_button_press(event, widget):
    widget.is_dragging = True
    widget.start_x = event.x_root - widget.winfo_x()
    widget.start_y = event.y_root - widget.winfo_y()
    update_widget_position(widget)
    # print(widgets)
    print(widget_info)

def on_button_drag(event, widget):
    if widget.is_dragging:
        new_x = event.x_root - widget.start_x
        new_y = event.y_root - widget.start_y
        widget.place(x=new_x, y=new_y)

def on_button_release(event, widget):
    widget.is_dragging = False
    update_widget_position(widget)
    print(widget_info)
    

def instantiate_widget(widgetType, count_key):
    global _count
    _count += 1

    widgetType.place(x=root.winfo_width() // 2, y=root.winfo_height() // 2, anchor="center")

    widgetType.is_dragging = False
    widgetType.start_x = 0
    widgetType.start_y = 0

    widgetType.bind("<ButtonPress-1>", lambda event, widget=widgetType: on_button_press(event, widget))
    widgetType.bind("<B1-Motion>", lambda event, widget=widgetType: on_button_drag(event, widget))
    widgetType.bind("<ButtonRelease-1>", lambda event, widget=widgetType: on_button_release(event, widget))

    widget_count[count_key] = _count
    widgets[_count] = widgetType

    # Call update_widget_position to add widget information to widget_info
    update_widget_position(widgetType)

def update_widget_position(widgetType):
    global widget_type_name, widget_id #, name_Label
    position = (widgetType.winfo_x(), widgetType.winfo_y())
    widget_type_name = type(widgetType).__name__
    widget_id = list(widgets.keys())[list(widgets.values()).index(widgetType)]
    
    # Update position in properties window

    # name_Label.configure(text=f"{widget_type_name} {widget_id}")
    
    # Update widget_info dictionary with new position
    widget_key = f"{widget_type_name} {widget_id}"
    widget_info[widget_key] = position

def instantiate_button():
    new_button = tk.Button(root, text="Dynamic Button")
    instantiate_widget(new_button, 'button')

def instantiate_label():
    new_label = tk.Label(root, text="Dynamic Label")
    instantiate_widget(new_label, 'label')

def instantiate_entry():
    new_entry = tk.Entry(root)
    instantiate_widget(new_entry, 'entry')

def instantiate_progressbar():
    new_bar = Progressbar(root)
    instantiate_widget(new_bar, 'progressbar')

def instantiate_frame():
    new_frame = tk.Frame(root, bg="red", height=120, width=220)
    instantiate_widget(new_frame, 'frame', widgets)

def save_widget_info_to_file():
    with open("widget_info.json", "w") as json_file:
        json.dump(widget_info, json_file)

def generate_file():
    file_code = f'''
import tkinter as tk
from tkinter.ttk import Progressbar

root = tk.Tk()
root.title("Your Application")
root.geometry("640x320")
    '''
    for widget_type, widget_pos in widget_info.items():
        widget_name = widget_type.split()[0]
        widget_id = widget_type.split()[1]
        widget_name = widget_type[:widget_type.index(' ')]  # Directly assign the desired substring

        x, y = widget_pos

        x = root.winfo_width() // 2 if x ==0 else x
        y = root.winfo_height() // 2 if y ==0 else y 

        if widget_name == "Button":
            file_code += f'''
Button{widget_id} = tk.Button(root, text="{widget_name+widget_id}")
Button{widget_id}.place(x={x}, y={y})
            '''
        elif widget_name == "Label":
            file_code += f'''
Label{widget_id} = tk.Label(root, text="{widget_name+widget_id}")
Label{widget_id}.place(x={x}, y={y})
'''
        
    file_code += "root.mainloop()"

    with open("GeneratedPyFile.py", "w") as code_file:
        code_file.write(file_code)


# name_Label = tk.Label(new_window)
# name_Label.place(x=0, y=10)
menu = tk.Menu(root, tearoff = 0)
menu.add_command(label="Save positions", command=save_widget_info_to_file)
menu.add_separator()
menu.add_command(label="Generate Py File", command=generate_file)
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

root.mainloop()
