import tkinter as tk

form = tk.Tk()
form.title("Entry")

giris = tk.Entry(form,fg="Black",bg="White")
giris.pack(side=tk.LEFT)

giris2 = tk.Entry(form,fg="Blue",bg="White")
giris2.pack(side=tk.RIGHT)


form.maxsize(600,400)
form.minsize(300,150)
form.geometry("500x300+300+300")
form.mainloop()