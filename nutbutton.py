import tkinter as tk
import winsound
from PIL import ImageTk, Image

window = tk.Tk()
window.title("NUT BUTTON")
window.geometry("600x600")
window.config(bg="black")

greeting = tk.Label(text="Click this plz", pady=10, bg="white", fg="black", font="Arial")
greeting.pack()
clickme = tk.Button()

img = ImageTk.PhotoImage(Image.open("NUT.jpg"))

clickme = tk.Button(image = img)
clickme.pack()

window.mainloop()