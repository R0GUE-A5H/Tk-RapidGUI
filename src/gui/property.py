import tkinter as tk


class PropertyWindow(tk.Toplevel):
    def __init__(self, root: tk.Tk, title, geometry):
        super().__init__(root)
        self.title = title
        self.geometry = geometry
        self.attributes("-toolwindow", True)
        self.iconify()
