import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("Hello", "You clicked the button!")

app = tk.Tk()
app.title("Simple GUI")

label = tk.Label(app, text="Hello, World!")
label.pack()

button = tk.Button(app, text="Click Me", command=on_button_click)
button.pack()

app.mainloop()
