import tkinter as tk

window = tk.Tk()

greeting = tk.Label(text="Hello, Tkinter!")
greeting.pack()

window.mainloop() 
# If you don’t include window.mainloop() at the end of a 
# program in a Python file, then the Tkinter application 
# will never run, and nothing will be displayed.