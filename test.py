import tkinter as tk

root = tk.Tk()

button = tk.Button(root, text="Button")
button.place(x=90, y=80, anchor="center")


text_create = tk.Entry(root, width=300)
text_create.place(x=100, y=120)

# def on_select(event, widget):
#     global start_x, start_y
#     start_x = event.x
#     start_y = event.y

# def on_drag(event, widget):
#     global start_x, start_y
#     delta_x = event.x - start_x
#     delta_y = event.y - start_y
#     new_width = widget.winfo_width() + delta_x
#     new_height = widget.winfo_height() + delta_y
#     widget.configure(width=new_width, height=new_height)
#     start_x = event.x
#     start_y = event.y

# def on_release(event, widget):
#     widget.unbind("<B1-Motion>")
#     widget.unbind("<ButtonRelease-1>")

# button.bind("<ButtonPress-1>", lambda event: on_select(event, button))
# button.bind("<B1-Motion>", lambda event: on_drag(event, button))
# button.bind("<ButtonRelease-1>", lambda event: on_release(event, button))

root.mainloop()
