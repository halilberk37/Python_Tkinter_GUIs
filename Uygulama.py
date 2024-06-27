import tkinter as tk
import random as rd

form = tk.Tk()
form.title("Tekrar Uygulaması")
liste=[]

for i in range(5):
    while len(liste)!=6:
        a = rd.randint(1,50)
        if a not in liste:
            liste.append(a)

def göster():
    label.config(text=liste,bg="green")

def saydam():
    form.wm_attributes("-alpha",0.5)

def döndür():
    form.wm_attributes("-alpha", 1)
def MaxYap():
    form.state("zoomed")
def MinYap():
    form.state("iconic")


label = tk.Label(form,fg="red",bg="White",font="Times 15")
label.pack()

göster = tk.Button(form,text="Göster",fg="black",bg="Blue",command =göster)
göster.pack()
saydam = tk.Button(form,text="Saydamlaştır",fg="White",bg="Black",command =saydam)
saydam.pack()

döndür = tk.Button(form,text="Eskiye Dön",fg="black",bg="White",command =döndür)
döndür.pack()
Max = tk.Button(form,text="Pencereyi Büyüt",fg="black",bg="Blue",command =MaxYap)
Max.pack()
Min = tk.Button(form,text="İkon Boyutu",fg="black",bg="Blue",command =MinYap)
Min.pack()


form.geometry("500x400+500+350")
form.mainloop()
