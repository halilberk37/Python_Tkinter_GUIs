import tkinter as tk

form = tk.Tk()
form.title("Geometrik Yöneticiler")

label = tk.Label(form,text="Geometrik Yöneticiler")
label.pack()

buton = tk.Button(form,text="Pack()")
buton.pack(fill=tk.X)

buton2 = tk.Button(form,text="Pack(2)",bg="Blue")
buton2.pack(ipadx=50,ipady=80)

buton3 = tk.Button(form,text="Konumlandırma",bg="Green")
buton3.place(x=200,y=250)

form.geometry("500x300+500+250")
form.mainloop()