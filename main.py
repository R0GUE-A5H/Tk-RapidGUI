""" Tk-RapidGUI

Prerequisites (Python 3.x):
tkinter, ttk, json


MIT License

Copyright (c) 2023 Ashwin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. """


# Future Additions
# ----------------

# TODO: Implement a Property Window that allows users to customize various aspects of widgets,
#       such as size, color, background, foreground, text, and position. Similar to the features
#       found in tools like Unity for game development.

# TODO: Refactor the codebase for better organization and readability.
#       Add comments to explain the purpose of different sections and functions.

# TODO: Implement a mechanism to adjust widget positions dynamically as the root window is resized.
#       This ensures that widgets maintain their positions relative to the window size.

# TODO: Provide an option for users to choose where to save the GeneratedPyFile.
#       Additionally, offer the ability to save widget positions in a JSON format for easy configuration.

# TODO: Expand widget support to include more advanced components like PhotoImage, ScrollBar, ListBox, etc.
#       This will enhance the versatility of the GUI application.

# TODO: Allow the root window geometry to be set according to the user's resizing by mouse.
#       This ensures that the window size and position can be customized to user preferences.

# End of Future Additions
# -----------------------


import tkinter as tk
from tkinter.ttk import Progressbar, Combobox
from tkinter import messagebox
import json

class TK_Entry(tk.Entry):

    def __init__(self, master=None, callback=None, **kwargs):
        super().__init__(master=master, **kwargs) # same as below one
        # tk.Entry.__init__(self, master=master, **kwargs)

        self.callback = callback

        self.var = tk.StringVar()

        self.config(textvariable=self.var)

        if self.callback:
            self.var.trace('w', self.on_val_change)
    
    def on_val_change(self, *args):
        if self.callback:
            self.callback(self.var.get())


# Define the main application window
root = tk.Tk()
root.title("Tkinter Rapid Development")
root.geometry("640x320")

# Create dictionaries to store widget information and widgets
widget_info = {}    # Store widget positions
widgets = {}        # Store widget instances
widget_count = {}   # Store widget count for each type

_count = 0   # Global counter for widget instances

pop_window = tk.Toplevel(root)
pop_window.geometry(f"300x320+770+0")
pop_window.title("Property")
pop_window.attributes("-toolwindow", True)
pop_window.attributes("-topmost", True)
property_frame = tk.LabelFrame(pop_window, text="Property").pack(padx=2,pady=2,fill="both", expand=True)


_background_canvas = tk.Canvas(root)
_background_canvas.pack(fill=tk.BOTH, expand=True)

# Create a series of vertical lines
# Create a solid black line from (50, 50) to (250, 150)
def draw_grid(width, height, cell_size):
    for x in range(0, root.winfo_width(), cell_size):
        _background_canvas.create_line(x, 0, x, height, fill="gray")
    for y in range(0, root.winfo_height(), cell_size):
        _background_canvas.create_line(0, y, width, y, fill="gray")

_background_canvas.bind("<Configure>", lambda event: draw_grid(event.width, event.height, 20))
# Create property of each widgets into it
def create_properties(widget):
    widget_name = widget.__class__.__name__
    
    for widgets in pop_window.winfo_children():
        widgets.destroy()
    
    def resize(val): #Accepts INT
            try:
                widget.config(font=('Arial', int(val)))
            except:
                if int(val) <0  or int(val) ==0 or int(val) < 5:
                    messagebox.showinfo("Enter valid int value")
    def change_text(texts):
        widget.config(text=texts)
    
    def relief_change(event, combobox):
        get_relief = combobox.get()
        for i in relief_style_lst:
            if i == get_relief:
                widget.config(relief=i)

    if widget_name == "Button":        
    
        size_label = tk.Label(pop_window, text="Button Size", font=('Arial', 10))
        size_label.place(x=0, y=10)

        size_entry = TK_Entry(pop_window, callback=resize)
        size_entry.place(x=80,y=11)

        button_label = tk.Label(pop_window, text="Button Text", font=('Arial', 10))
        button_label.place(x=0, y=50)
        button_text_entry = TK_Entry(pop_window, callback=change_text)
        button_text_entry.place(x=80,y=51)

        relief_style_lst = ["sunken", "raised", "flat", "groove", "solid", "ridge"]
        relief_label = tk.Label(pop_window, text="Relief Style", font=('Arial', 10))
        relief_label.place(x=0, y=90)
        relief_style_button = Combobox(pop_window, values=relief_style_lst, state="readonly")
        relief_style_button.current(1)
        relief_style_button.set("Pick Relief Style")
        relief_style_button.place(x=80, y=91)

        relief_style_button.bind("<<ComboboxSelected>>", lambda event, combo=relief_style_button : relief_change(event, combo))



    elif widget_name == "Label":
        size_label = tk.Label(pop_window, text="Label Size", font=('Arial', 10))
        size_label.place(x=0, y=10)

        size_entry = TK_Entry(pop_window, callback=resize)
        size_entry.place(x=80,y=11)

        name_label = tk.Label(pop_window, text="Label Text", font=('Arial', 10))
        name_label.place(x=0, y=50)

        label_entry = TK_Entry(pop_window, callback=change_text)
        label_entry.place(x=80,y=51)

        relief_style_lst = ["sunken", "raised", "flat", "groove", "solid", "ridge"]
        relief_label = tk.Label(pop_window, text="Relief Style", font=('Arial', 10))
        relief_label.place(x=0, y=90)
        relief_style_label = Combobox(pop_window,values=relief_style_lst)
        relief_style_label.current(2)
        relief_style_label.place(x=80, y=91)

        relief_style_label.bind("<<ComboboxSelected>>", lambda event, combo=relief_style_label : relief_change(event, combo))
    
    elif widget_name == "Progressbar":

        def Progressbar_length(length):
            widget.config(length=length)

        def on_orient_change(event):
            selected_orient = orient_box.get()
            for i in orient_list:
                if selected_orient == i:
                    widget.config(orient=i)

        def on_mode_change(event):
            selected_mod = mode_box.get()
            for i in mode_list:
                if selected_mod == i:
                    widget.config(mode=i)

        size_label = tk.Label(pop_window, text="Progressbar Length", font=('Arial', 10))
        size_label.place(x=0, y=10)

        size_entry = TK_Entry(pop_window, callback=Progressbar_length)
        size_entry.place(x=120,y=11)

        orient_list = ["vertical", "horizontal"]
        mode_list = ["determinate", "indeterminate"]

        orient_label = tk.Label(pop_window, text="Orient Style", font=('Arial', 10))
        orient_label.place(x=0, y=40)
        orient_box = Combobox(pop_window, values=orient_list, state="readonly")
        orient_box.current(1)
        orient_box.place(x=80, y=40)

        mode_label = tk.Label(pop_window, text="Mode", font=('Arial', 10))
        mode_label.place(x=0, y=70)
        mode_box = Combobox(pop_window, values=mode_list, state="readonly")
        mode_box.set("Pick A Mode")
        mode_box.place(x=50, y=70)

        orient_box.bind("<<ComboboxSelected>>", on_orient_change)
        mode_box.bind("<<ComboboxSelected>>", on_mode_change)
        

# Event handlers for widget dragging
def on_button_press(event, widget):
    widget.is_dragging = True
    widget.start_x = event.x_root - widget.winfo_x()
    widget.start_y = event.y_root - widget.winfo_y()
    create_properties(widget)
    update_widget_position(widget)
    

def on_button_drag(event, widget):
    if widget.is_dragging:
        new_x = event.x_root - widget.start_x
        new_y = event.y_root - widget.start_y
        widget.place(x=new_x, y=new_y)
        update_status(new_x, new_y)

def on_button_release(event, widget):
    widget.is_dragging = False
    update_widget_position(widget)

def instantiate_widget(widgetType, count_key):
    global _count
    _count += 1

    # Initialize widget attributes and bindings
    widgetType.place(x=root.winfo_width() // 2, y=root.winfo_height() // 2, anchor="center")
    widgetType.is_dragging = False
    widgetType.start_x = 0
    widgetType.start_y = 0

    widgetType.bind("<ButtonPress-1>", lambda event, widget=widgetType: on_button_press(event, widget))
    widgetType.bind("<B1-Motion>", lambda event, widget=widgetType: on_button_drag(event, widget))
    widgetType.bind("<ButtonRelease-1>", lambda event, widget=widgetType: on_button_release(event, widget))

    # Store widget count and instance
    widget_count[count_key] = _count
    widgets[_count] = widgetType
    print(type(widgetType).__name__)

    # Update widget position information
    update_widget_position(widgetType)
    create_properties(widget=widgetType)

# Update widget position in widget_info dictionary
def update_widget_position(widgetType):
    global widget_type_name, widget_id

    position = (widgetType.winfo_x(), widgetType.winfo_y())
    widget_type_name = type(widgetType).__name__
    widget_id = list(widgets.keys())[list(widgets.values()).index(widgetType)]
    
    # Update widget_info dictionary with new position
    widget_key = f"{widget_type_name} {widget_id}"
    widget_info[widget_key] = position

# Widget instantiation functions
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
    instantiate_widget(new_frame, 'frame')

def instantiate_combobox():
    new_combobox = Combobox(root)
    instantiate_widget(new_combobox, 'combobox')

def instantiate_radiobutton():
    new_frame = tk.Frame(root, bg="red", height=120, width=220)
    instantiate_widget(new_frame, 'frame')

def instantiate_checkbutton():
    new_frame = tk.Frame(root, bg="red", height=120, width=220)
    instantiate_widget(new_frame, 'frame')

def instantiate_separator():
    new_frame = tk.Frame(root, bg="red", height=120, width=220)
    instantiate_widget(new_frame, 'frame')

def instantiate_():
    new_frame = tk.Frame(root, bg="red", height=120, width=220)
    instantiate_widget(new_frame, 'frame')

def instantiate_frame():
    new_frame = tk.Frame(root, bg="red", height=120, width=220)
    instantiate_widget(new_frame, 'frame')


# Save widget position information to a JSON file
def save_widget_info_to_file():
    with open("widget_info.json", "w") as json_file:
        json.dump(widget_info, json_file)

# Generate Python file based on widget positions
count=0
def generate_file():
    global count
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
        widget_name = widget_type[:widget_type.index(' ')]

        x, y = widget_pos

        x = root.winfo_width() // 2 if x == 0 else x
        y = root.winfo_height() // 2 if y == 0 else y

        # Generate code for each widget type
        if widget_name == "Button":
            count += 1
            if(count):
                file_code += f'''
def func{widget_name+widget_id}():
    pass
'''       
            file_code += f'''
Button{widget_id} = tk.Button(root, text="{widget_name+widget_id}", command="func{widget_name+widget_id}")
Button{widget_id}.place(x={x}, y={y})
'''
    file_code += f'''
root.mainloop()
'''

    # Write generated code to a Python file
    with open("GeneratedPyFile.py", "w") as code_file:
        code_file.write(file_code)

def change_geometry():
    window = tk.Toplevel(root)
    window.geometry("300x55")

    #place widgets into it
    width_label = tk.Label(window, text="Width").place(x=40, y=10)
    width_entry = tk.Entry(window)
    width_entry.place(x=90, y=10)

    height_label = tk.Label(window, text="Height").place(x=40, y=30)
    height_entry = tk.Entry(window)
    height_entry.place(x=90, y=30)

    def resize():
        try:
            new_width = int(width_entry.get())  # Get the value from the width entry and convert to integer
            new_height = int(height_entry.get())  # Get the value from the height entry and convert to integer
            new_geometry = f"{new_width}x{new_height}"  # Create the new geometry string
            root.geometry(new_geometry)  # Update the geometry of the window
            # window.destroy()
        except ValueError:
            messagebox.showerror("Error","Enter a int value")

    Change_Button = tk.Button(window, text="Resize", command=resize).place(x=230, y = 20)

# Create a context menu for widgets
menu = tk.Menu(root, tearoff=0)
menu.add_command(label="Save positions", command=save_widget_info_to_file)
menu.add_separator()
menu.add_command(label="Generate Py File", command=generate_file)
menu.add_separator()
menu.add_command(label="Resize Window", command=change_geometry)
menu.add_separator()
menu.add_command(label="New Button", command=instantiate_button)
menu.add_command(label="New Label", command=instantiate_label)
menu.add_command(label="New Entry", command=instantiate_entry)
menu.add_separator()
menu.add_command(label="ProgressBar", command=instantiate_progressbar)
menu.add_separator()
menu.add_command(label="CheckButton")
menu.add_command(label="RadioButton")
menu.add_command(label="Combobox")
menu.add_separator()
menu.add_command(label="Scale")
# menu.add_command(label="Scrollbar")
menu.add_command(label="Frame", command=instantiate_frame)

# Status bar to display widget information
status_bar = tk.Label(root, text=f"{widget_info}", relief="sunken")
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

# Update status bar with widget position information
def update_status(x, y):
    status_bar.config(text=f"{widget_type_name, widget_id}: x={x}, y={y}")

# Bind right-click event to the context menu
root.bind("<Button-3>", lambda event: menu.tk_popup(event.x_root, event.y_root))
# Run the main event loop
root.mainloop()
