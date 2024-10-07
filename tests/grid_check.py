import tkinter as tk
from tkinter import ttk


class GridBasedDesigner:
    def __init__(self, master):
        self.master = master
        self.master.title("Grid-based GUI Designer")

        self.frame = tk.Frame(master)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.design_area = tk.Frame(self.frame, bg="white")
        self.design_area.grid(row=0, column=0, sticky="nsew")

        self.controls = tk.Frame(self.frame)
        self.controls.grid(row=0, column=1, sticky="ns")

        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)

        self.create_controls()

        self.widgets = []

    def create_controls(self):
        ttk.Button(self.controls, text="Add Button",
                   command=self.add_button).pack()
        ttk.Button(self.controls, text="Add Label",
                   command=self.add_label).pack()

        ttk.Label(self.controls, text="Row:").pack()
        self.row_var = tk.StringVar(value="0")
        ttk.Entry(self.controls, textvariable=self.row_var).pack()

        ttk.Label(self.controls, text="Column:").pack()
        self.col_var = tk.StringVar(value="0")
        ttk.Entry(self.controls, textvariable=self.col_var).pack()

        ttk.Label(self.controls, text="Row Span:").pack()
        self.rowspan_var = tk.StringVar(value="1")
        ttk.Entry(self.controls, textvariable=self.rowspan_var).pack()

        ttk.Label(self.controls, text="Column Span:").pack()
        self.colspan_var = tk.StringVar(value="1")
        ttk.Entry(self.controls, textvariable=self.colspan_var).pack()

        ttk.Button(self.controls, text="Update Position",
                   command=self.update_position).pack()

    def add_button(self):
        button = tk.Button(self.design_area, text="Button")
        self.add_widget(button)

    def add_label(self):
        label = tk.Label(self.design_area, text="Label", bg="lightgray")
        self.add_widget(label)

    def add_widget(self, widget):
        widget.grid(row=0, column=0)
        self.widgets.append(widget)
        widget.bind("<Button-1>", lambda e, w=widget: self.select_widget(w))

    def select_widget(self, widget):
        for w in self.widgets:
            w.config(relief="raised")
        widget.config(relief="sunken")
        self.selected_widget = widget
        self.update_position_vars()

    def update_position_vars(self):
        info = self.selected_widget.grid_info()
        self.row_var.set(info['row'])
        self.col_var.set(info['column'])
        self.rowspan_var.set(info['rowspan'])
        self.colspan_var.set(info['columnspan'])

    def update_position(self):
        if hasattr(self, 'selected_widget'):
            self.selected_widget.grid(
                row=int(self.row_var.get()),
                column=int(self.col_var.get()),
                rowspan=int(self.rowspan_var.get()),
                columnspan=int(self.colspan_var.get())
            )


root = tk.Tk()
app = GridBasedDesigner(root)
root.mainloop()
