import tkinter as tk

form = tk.Tk()
form.title("Buton Ekleme")
def topla():
    print("topla")


buton = tk.Button(form,text="Tıkla",fg="Blue",bg="Black",command=topla)
buton.pack()

buton2 = tk.Button(form,text="Tıkla2",command=topla)
buton2.pack()


form.geometry("500x300+700+300")
form.mainloop()