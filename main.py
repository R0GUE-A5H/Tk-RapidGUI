import tkinter as tk
from tkinter.ttk import Progressbar
import json

# Define the main application window
root = tk.Tk()
root.title("Tkinter Rapid Development")
root.geometry("640x320")

# Create dictionaries to store widget information and widgets
widget_info = {}    # Store widget positions
widgets = {}        # Store widget instances
widget_count = {}   # Store widget count for each type

_count = 0   # Global counter for widget instances

# Event handlers for widget dragging
def on_button_press(event, widget):
    widget.is_dragging = True
    widget.start_x = event.x_root - widget.winfo_x()
    widget.start_y = event.y_root - widget.winfo_y()
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

    # Update widget position information
    update_widget_position(widgetType)

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

# Save widget position information to a JSON file
def save_widget_info_to_file():
    with open("widget_info.json", "w") as json_file:
        json.dump(widget_info, json_file)

# Generate Python file based on widget positions
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

        # Similar code generation for other widget types

    file_code += f'''
root.mainloop()
'''

    # Write generated code to a Python file
    with open("GeneratedPyFile.py", "w") as code_file:
        code_file.write(file_code)

# Create a context menu for widgets
menu = tk.Menu(root, tearoff=0)
menu.add_command(label="Save positions", command=save_widget_info_to_file)
menu.add_separator()
menu.add_command(label="Generate Py File", command=generate_file)
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
menu.add_command(label="Scrollbar")
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
