import tkinter as tk
from tkinter import messagebox

form = tk.Tk()
form.title("Message Box")

def mesaj():
    messagebox.showinfo(title="Mesaj1",message="Bilgilendirme Kutusu")
    messagebox.askretrycancel(title="Mesaj2",message="Tekrar Dene veya iptal et")
    messagebox.askquestion(title="Mesaj3",message="Soru sorma mesaj kutusu")
    messagebox.askyesno(title="Mesaj4",message="Evet veya Hayır tercih kutusu")


buton = tk.Button(form,text="Mesaj Göster",command=mesaj)
buton.pack()



form.geometry("500x500+500+300")
form.mainloop()