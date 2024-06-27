import tkinter as tk

form = tk.Tk()
form.title("Pizza Sipariş Uygulaması")

baslik = tk.Label(form,text="Pizza Sipariş Programı",fg="White",bg="Red",font="Times 15 bold").pack()

entr1=tk.StringVar()
entr2 =tk.StringVar()

lb_ad=tk.Label(form,text="Ad-Soyad:",fg="black",bg="Gray",font="Georgia 10 italic").place(x=10,y=40)
lb_boyut=tk.Label(form,text="Pizza Boyutu:",fg="black",bg="Gray",font="Georgia 10 italic").place(x=10,y=70)
lb_içindekiler=tk.Label(form,text="İçindekiler:",fg="black",bg="Gray",font="Georgia 10 italic").place(x=10,y=100)
lb_adres=tk.Label(form,text="Adres:",fg="black",bg="Gray",font="Georgia 10 italic").place(x=10,y=130)

entry_ad = tk.Entry(textvariable=entr1).place(x=110,y=40)
entry_adres = tk.Entry(textvariable=entr2).place(x=110,y=130)

boyut = tk.StringVar()

radbutton_kücük = tk.Radiobutton(form,text="Küçük Boy",activebackground="red",value="Küçük Boy",variable=boyut).place(x=100,y=70)
radbutton_orta = tk.Radiobutton(form,text="Orta Boy",activebackground="Blue",value="Orta Boy",variable=boyut).place(x=190,y=70)
radbutton_büyük = tk.Radiobutton(form,text="Büyük Boy",activebackground="Green",value="Büyük Boy",variable=boyut).place(x=270,y=70)


deger1 = tk.StringVar()
deger2 = tk.StringVar()
deger3 = tk.StringVar()


Check1 = tk.Checkbutton(form,text="Sucuklu",variable=deger1,onvalue="Sucuklu").place(x=100,y=100)
Check2 = tk.Checkbutton(form,text="Mısırlı",variable=deger2,onvalue="Mısırlı").place(x=190,y=100)
Check3 = tk.Checkbutton(form,text="Acılı Sos",variable=deger3,onvalue="Acılı Sos").place(x=270,y=100)

def siparisver():
    lb_siparis = tk.Label(form, text="Sipariş Bilgileri", fg="White", bg="Red", font="Times 15 italic").place(x=30,y=210)
    lb_ad = tk.Label(form, text="Ad-Soyad:", fg="black", bg="Gray", font="Georgia 10 italic").place(x=10, y=260)
    lb_boyut = tk.Label(form, text="Pizza Boyutu:", fg="black", bg="Gray", font="Georgia 10 italic").place(x=10, y=290)
    lb_içindekiler = tk.Label(form, text="İçindekiler:", fg="black", bg="Gray", font="Georgia 10 italic").place(x=10,y=320)
    lb_adres = tk.Label(form, text="Adres:", fg="black", bg="Gray", font="Georgia 10 italic").place(x=10, y=350)

    lb_ad = tk.Label(form, text=entr1.get(), fg="black", bg="white", font="Georgia 10 italic").place(x=100, y=260)
    lb_boyut = tk.Label(form, text=boyut.get(), fg="black", bg="white", font="Georgia 10 italic").place(x=100, y=290)
    lb_içindekiler = tk.Label(form, text=deger1.get()+"  "+deger2.get()+"  "+deger3.get(), fg="black", bg="White", font="Georgia 10 italic").place(x=100,y=320)
    lb_adres = tk.Label(form, text=entr2.get(), fg="black", bg="white", font="Georgia 10 italic").place(x=100, y=350)

def iptalet():
    form.quit()

siparis = tk.Button(form,text="Sipariş Ver",activebackground="Green",command=siparisver).place(x=170,y=160)
iptal = tk.Button(form,text="İptal Et",activebackground="Red",command=iptalet).place(x=250,y=160)

# Sipariş Bilgileri














form.geometry("500x500+700+200")
form.mainloop()