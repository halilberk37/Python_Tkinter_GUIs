import tkinter as tk
from PIL import Image,ImageTk

form = tk.Tk()
form.title("Resim Ekleme")

resim = ImageTk.PhotoImage(Image.open("C://Users//Halil İbrahim Berk//Desktop//Adsız.png"))

label = tk.Label(form,image=resim)
label.pack(padx=10,pady=10)


form.geometry("500x400")
form.mainloop()