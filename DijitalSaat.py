import tkinter as tk
import time


form = tk.Tk()
form.title("Dijital Saat")


def zaman():
    zaman_format=time.strftime("%H:%M:%S")
    lb_zaman.config(text=zaman_format)
    lb_zaman.after(200,zaman)


lb_zaman= tk.Label(bg="white",font="Times 35 bold")
lb_zaman.place(x=30,y=50)
zaman()

form.geometry("250x200+500+200")
form.config(bg="Green")
form.mainloop()