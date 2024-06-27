import tkinter as tk


form = tk.Tk()
sayac = 0
form.title("Sayaç Uygulaması")
form.config(bg="Gray")

x = tk.IntVar()
giris = tk.Entry(form,textvariable=x)
giris.place(x=70,y=50)

lb_giris = tk.Label(form,text="Giriş:",bg="gray",font="consoles 15 bold")
lb_giris.place(x=10,y=45)

def gerial():
    global sayac
    if sayac >= 0:
        lb_sayim.config(text=sayac)
        sayac = sayac-1
        lb_sayim.after(1000,gerial)
def ilerisar():
    global sayac
    if sayac >= 0:
        lb_sayim.config(text=sayac)
        sayac = sayac +1
        lb_sayim.after(1000, ilerisar)
def cevir():
    global sayac
    sayac=sayac+int(x.get())
    return sayac



buton1 = tk.Button(form,text="Geri Al",activebackground="Blue",command=gerial)
buton1.place(x=40,y=80)
buton2 = tk.Button(form,text="İleri Sar",activebackground="Green",command=ilerisar)
buton2.place(x=90,y=80)
buton3 = tk.Button(form,text="Cevir",activebackground="Red",command=cevir)
buton3.place(x=145,y=80)


lb_sayim=tk.Label(form,bg="green",font="Times 40 bold")
lb_sayim.place(x=200,y=80)

form.geometry("500x500+600+300")
form.mainloop()