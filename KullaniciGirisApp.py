import tkinter as tk

form = tk.Tk()
form.title("Kullanıcı Girişi")

mail =tk.Label(form,text="Mail Adresi",fg="white",bg="Black",font="Times 10 bold")
mail.place(x=15,y=30)

sifre =tk.Label(form,text="Şifre",fg="white",bg="Black",font="Times 10 bold")
sifre.place(x=15,y=60)

mail_entr = tk.Entry()
mail_entr.place(x=100,y=30)

sifre_entr = tk.Entry(show="*",fg="red")
sifre_entr.place(x=100,y=60)

def kayıtol():
    mail = tk.Label(form, text="Mail Adresi:", fg="white", bg="Black", font="Times 10 bold")
    mail.place(x=15, y=190)
    sifre = tk.Label(form, text="Şifre:", fg="white", bg="Black", font="Times 10 bold")
    sifre.place(x=15, y=220)
    ad = tk.Label(form, text="Adınız:", fg="white", bg="Black", font="Times 10 bold")
    ad.place(x=15, y=250)

    mail_entr = tk.Entry()
    mail_entr.place(x=100, y=190)

    sifre_entr = tk.Entry(show="*", fg="red")
    sifre_entr.place(x=100, y=220)

    ad_entr = tk.Entry(show="*", fg="red")
    ad_entr.place(x=100, y=250)




def giris():
    mail_entr.delete(0,"end")
    sifre_entr.delete(0,"end")


kayıt = tk.Button(form,text="Kayıt Ol",fg="Black",bg="Gray",command=kayıtol)
kayıt.place(x=100,y=100)


giris = tk.Button(form,text="Giriş",fg="White",bg="Blue",command=giris)
giris.place(x=180,y=100)

form.geometry("300x400+700+300")
form.mainloop()