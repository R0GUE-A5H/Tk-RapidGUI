# Tk-RapidGUI

## **Tkinter Rapid Development Tool**
Overview

The Tkinter Rapid Development Tool is a graphical user interface (GUI) development tool built using the Tkinter library in Python. This tool simplifies and accelerates the process of designing and positioning widgets in a Tkinter-based application. It provides a visual interface to drag and place widgets, and then automatically generates the corresponding Python code for widget placement.

1. **Features Drag-and-Drop Interface**
 
  The tool allows you to easily create and position widgets using a simple drag-and-drop interface. No need to manually calculate and set widget coordinates.

2. **Dynamic Widget Creation**

  You can create various types of widgets, such as buttons, labels, entries, progress bars, and frames, directly from the tool's menu.

3. **Real-time Widget Position Tracking**

  As you drag and place widgets, their positions are tracked in real-time and displayed in a properties window.

4. **Code Generation**

  The tool generates Python code based on the positioned widgets, enabling you to quickly implement the GUI layout in your application.

5. **Saving Widget Positions**

  You can save the positions of the widgets to a JSON file for later use or reference.

6.. **Why Use This Tool?**

Creating graphical user interfaces with Tkinter often involves manual placement of widgets using the `place` or `grid` geometry managers. This process can be challenging,  especially for newcomers to GUI programming. The Tkinter Rapid Development Tool addresses this challenge by providing an intuitive drag-and-drop interface that eliminates
the need for manual coordinate calculations. This tool bridges the gap between visual layout design and code generation, making GUI development with Tkinter more      accessible and efficient.

## **How to Use**

```Clone or download this repository to your local machine.

Run the main.py script using Python.

The tool's main window will open, displaying a canvas where you can create and position widgets.

Right-click on the canvas to access the context menu for widget creation and other actions.

Drag and place widgets on the canvas as desired.

The properties window displays real-time information about the selected widget, including its type, ID, and position.

To save the widget positions, click on the "Save positions" option in the context menu.

To generate Python code based on the positioned widgets, click on the "Generate Py File" option. The generated code will be saved in a file named GeneratedPyFile.py.

Customize the generated code to integrate the GUI layout into your application.
```
![image](https://github.com/R0GUE-A5H/Tk-RapidGUI/assets/38578557/9a7b6dc5-6d69-4e52-8c78-5a358e35c86b)
![image](https://github.com/R0GUE-A5H/Tk-RapidGUI/assets/38578557/df7d08a2-4740-43f5-812a-296504b9ad40)
![image](https://github.com/R0GUE-A5H/Tk-RapidGUI/assets/38578557/cc559d35-8e5d-4e41-87e6-78cec99eb648)
![image](https://github.com/R0GUE-A5H/Tk-RapidGUI/assets/38578557/ecebca99-6dba-482d-8bef-0213d2d3d372)


## **Example Generated Code**
The tool generates Python code that corresponds to the positioned widgets. Here is an example of the generated code:

```py

import tkinter as tk
from tkinter.ttk import Progressbar

root = tk.Tk()
root.title("Your Application")
root.geometry("640x320")
    
Button1 = tk.Button(root, text="Button1")
Button1.place(x=25, y=22)
            
Button2 = tk.Button(root, text="Button2")
Button2.place(x=28, y=138)
            
Label3 = tk.Label(root, text="Label3")
Label3.place(x=232, y=27)

Button4 = tk.Button(root, text="Button4")
Button4.place(x=396, y=211)
            
Label5 = tk.Label(root, text="Label5")
Label5.place(x=320, y=160)

Label6 = tk.Label(root, text="Label6")
Label6.place(x=330, y=102)
root.mainloop()
```

# **Contributions**
Contributions to this project are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## **License**
This project is licensed under the MIT License. See the _LICENSE_ file for details.

