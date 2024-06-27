import tkinter as tk
from tkinter.ttk import Combobox

form = tk.Tk()
form.title("ComboBox Kullanımı")

dizi=["Python","C++","Java","HTML","Sayılar"]
sayilar =[1,2,3,4,5,6,7,8,9,10]
deger = tk.StringVar()
kutu = Combobox(form,values=(1,2,3)).pack()
kutu2 = Combobox(form,values=dizi,textvariable=deger).pack()
kutu3 = Combobox(form,values=sayilar,height=3).pack()

def yazdir():
    print(deger.get())

buton = tk.Button(form,text="Yazdır",command=yazdir).pack()


form.geometry("500x300+700+300")
form.mainloop()