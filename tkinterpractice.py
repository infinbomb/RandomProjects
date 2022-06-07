import tkinter as tk

window = tk.Tk()

greeting = tk.Label(text="Greetings", pady=20)
greeting.pack()
clickme = tk.Button(text="Click", pady=30)
clickme.pack()

window.mainloop()