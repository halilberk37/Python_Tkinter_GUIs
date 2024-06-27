import tkinter as tk

form = tk.Tk()
form.title("Pencere Boyutlandırma")

label = tk.Label(form,text="Pencere Boyutlandırma",fg="red")
label.pack()


#Geometry Pencere boyutu ve konumunu ayarlıyor.
form.geometry("500x250+500+300")
form.minsize(400,150)
form.maxsize(600,400)
form.mainloop()