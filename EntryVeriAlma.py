import tkinter as tk

form = tk.Tk()
form.title("Entryden Veri Alma")

giris =tk.Entry(form,fg="Blue",bg="White")
giris.place(x=10,y=10)


giris1 =tk.Entry(form,fg="Red",bg="White",show="*")
giris1.place(x=10,y=30)
def verial():
    etiket["text"] = giris.get()
def verisil():
    giris.delete(0,"end")
    giris1.delete(0, "end")

buton = tk.Button(form,text="Veri Al",fg="Green",bg="white",command=verial)
buton.pack()

buton2 = tk.Button(form,text="Veri Sil",fg="Black",bg="white",command=verisil)
buton2.pack()


etiket = tk.Label(form,text="Entry Verileri Burada Gözükür",font="Times 15 italic")
etiket.pack()


form.geometry("500x300+500+300")
form.mainloop()