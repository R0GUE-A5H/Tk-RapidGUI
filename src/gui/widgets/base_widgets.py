import tkinter as tk
import tkinter.ttk as ttk
from windows import MainWindow


__all__ = []


class BaseWidget():

    def __init__(self, event: tk.Event, widget: tk.Widget, **kwargs):

        self.event = event
        self.widget = widget
        self.is_dragging = False
        self.start_x = 0
        self.start_y = 0

        self.count = 0

        self._store_widget_instance = {}
        self._store_widget_position = {}
        self._store_widget_count = {}

        self.widget_types = {
            "Button": (tk.Button, kwargs),
            "Label": (tk.Label, kwargs),
            "Entry": (tk.Entry, kwargs),
            "Frame": (tk.Frame, kwargs),
            "Scrollbar": (tk.Scrollbar, kwargs),
            "Scale": (tk.Scale, kwargs),
            "Checkbutton": (tk.Checkbutton, kwargs),
            "Radiobutton": (tk.Radiobutton, kwargs),
            "Combobox": (ttk.Combobox, kwargs),
            "Listbox": (tk.Listbox, kwargs),
            "Entry": (tk.Entry, kwargs),
            "Canvas": (tk.Canvas, kwargs),
            "Text": (tk.Text, kwargs),
            "Treeview": (ttk.Treeview, kwargs),
            "Progressbar": (ttk.Progressbar, kwargs),
            "Spinbox": (tk.Spinbox, kwargs),
            "Toplevel": (tk.Toplevel, kwargs),
            "Menubutton": (tk.Menubutton, kwargs),
            "Menu": (tk.Menu, kwargs),
            "Tk": (tk.Tk, kwargs),
            "PhotoImage": (tk.PhotoImage, kwargs),
            "Image": (tk.Image, kwargs),

        }

        self._create_properties()

    def _on_button_press(self):
        self.is_dragging = True
        self.start_x = self.event.x_root - self.widget.winfo_x()
        self.start_y = self.event.y_root - self.widget.winfo_y()
        self._create_properties()
        self.update_position()

    def _on_button_drag(self):
        if self.is_dragging:
            new_x = self.event.x_root - self.start_x
            new_y = self.event.y_root - self.start_y
            self.widget.place(x=new_x, y=new_y)
            self.update_position()  # Look here if it is not working

    def _on_button_release(self):
        self.is_dragging = False
        self.update_position()

    def _create_properties(self):
        widget_name = self.widget.__class__.__name__
        # Rewrite the property window
        pass

    def update_position(self):
        position = (self.widget.winfo_x(), self.widget.winfo_y())
        widget_name = type(self.widget).__name__
        widget_id = list(self._store_widget_instance.keys())[
            list(self._store_widget_instance.values()).index(self.widget)]

        # Update widget_info dictionary with new position
        widget_key = f"{widget_name} {widget_id}"
        self._store_widget_position[widget_key] = position

    def _create_widget(self):

        self.count += 1

        self.widget.place(x=MainWindow.winfo_width() // 2,
                          y=MainWindow.winfo_height() // 2,
                          anchor="center",
                          bordermode='inside')
        self.is_dragging = False

        self.widget.bind("<ButtonPress-1>", self.button_press_event)
        self.widget.bind("<B1-Motion>", self.button_drag_event)
        self.widget.bind("<ButtonRelease-1>", self.button_release_event)

      #  self._store_widget_count[self.widget_types[]]
