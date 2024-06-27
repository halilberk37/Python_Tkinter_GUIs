import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox


form = tk.Tk()
form.title("İnternet Arıza Uygulaması")
form.config(bg="Black")

lb_baslik = tk.Label(form,text="Arıza Bildirim Uygulaması",bg="Black",fg="White",font="Times 17 bold")
lb_baslik.pack()

kullanıcı_adı = tk.StringVar()
sifre = tk.StringVar()

lb_ad = tk.Label(form,text="Kullanıcı Adı:",bg="Black",fg="White",font="Times 12 italic")
lb_ad.place(x=10,y=50)

lb_sifre = tk.Label(form,text="Şifre:",bg="Black",fg="White",font="Times 12 italic")
lb_sifre.place(x=10,y=100)

entry_ad = tk.Entry(form,textvariable=kullanıcı_adı)
entry_sifre = tk.Entry(form,show="*",textvariable=sifre)
entry_ad.place(x=110,y=50)
entry_sifre.place(x=110,y=100)


def giris():
    if kullanıcı_adı.get()=="halil" and sifre.get()=="1234":
        msg = messagebox.showinfo(title="Tebrikler",message="Giriş Başarılı")
        if msg == "ok":
            basvuru_formu = tk.Toplevel()
            basvuru_formu.geometry("350x350")
            basvuru_formu.title("Arıza Bildirim Formu")
            basvuru_formu.config(bg="Yellow")
            baslık_lb = tk.Label(basvuru_formu,text="Arıza Bildirim Formu",bg="black",fg="Red",font="Times 15 bold")
            baslık_lb.pack()
            label_ad = tk.Label(basvuru_formu,text="Ad-Soyad:",font="Consoles 10 italic").place(x=10,y=40)
            label_ad = tk.Label(basvuru_formu, text="TC No:", font="Consoles 10 italic").place(x=10, y=80)
            label_ad = tk.Label(basvuru_formu, text="Modem Tipi:", font="Consoles 10 italic").place(x=10, y=120)
            label_ad = tk.Label(basvuru_formu, text="Arıza Tipi:", font="Consoles 10 italic").place(x=10, y=160)
            label_ad = tk.Label(basvuru_formu, text="Adres:", font="Consoles 10 italic").place(x=10, y=200)
            label_ad = tk.Label(basvuru_formu, text="Mail:", font="Consoles 10 italic").place(x=10, y=240)

            entry_isim=tk.Entry(basvuru_formu)
            entry_isim.place(x=100,y=40)

            entry_tc = tk.Entry(basvuru_formu)
            entry_tc.place(x=100, y=80)
            liste=["TPM","SKS34","HTPS","FİBOS","LOWOS"]
            combo_modem = Combobox(basvuru_formu,values=liste).place(x=100,y=120)

            liste1 = ["KABLO", "Giriş Arıza", "Hız Problemi", "Wifi sorunu", "Bağlantı Kopma Sorunu"]
            combo_modem = Combobox(basvuru_formu, values=liste1).place(x=100, y=160)


            entry_adres = tk.Entry(basvuru_formu)
            entry_adres.place(x=100, y=200)

            entry_mail = tk.Entry(basvuru_formu)
            entry_mail.place(x=100, y=240)
    else:
        ms2 = messagebox.showinfo("Hata",message="Hatalı veya Eksik Giriş Yaptınız")







def iptal():
    pass


btn_giris = tk.Button(form,text="Giriş",activebackground="Green",command=giris)
btn_giris.place(x=150,y=160,width=60)
btn_iptal = tk.Button(form,text="İptal",activebackground="Red",command=iptal)
btn_iptal.place(x=220,y=160,width=60)








form.geometry("400x400+600+300")
form.mainloop()