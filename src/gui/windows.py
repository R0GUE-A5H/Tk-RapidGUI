import tkinter as tk


class MainWindow(tk.Tk):

    def __init__(self, title, geometry):
        super().__init__()

        self.title = title
        self.geometry = geometry

        self._background_canvas = tk.Canvas(self)
        self._background_canvas.pack(fill=tk.BOTH, expand=True)

        self._background_canvas.bind("<Configure>", self.on_resize)

    def _draw_grid_line(self, cellSize):

        for x in range(0, self.winfo_width(), cellSize):
            self._background_canvas.create_line(
                x, 0, x, self.winfo_height(), fill="gray")
        for y in range(0, self.winfo_width(), cellSize):
            self._background_canvas.create_line(
                0, y, self.winfo_width(), y, fill="gray")

    def on_resize(self, event):
        # Call the draw grid method when the canvas is resized
        self.draw_grid(event.width, event.height, 20)
