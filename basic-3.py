import tkinter as tk
from tkinter import ttk
win = tk.Tk()
# win.resizable(10,10) 
win.title("learning")
ttk.Label(win,text="a lable something").grid(column=0, row=0)
win.mainloop()