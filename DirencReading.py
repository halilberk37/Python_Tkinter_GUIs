import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter.ttk import Combobox


form = tk.Tk()
form.title("Direnç Değer Hesaplama")
resim = ImageTk.PhotoImage(Image.open("C://Users//halil//Desktop//Görseller//Unsplash ve Freepik//Freepik//20622.jpg"))

label = tk.Label(form,image=resim)
label.pack()

#Dört bantlı direnç başlangıç
def dortBantlı():
    label4 = tk.Label(form,text="4 Bantlı Dirençler İçin Renk Kodu Okuma",bg="black",fg="white")
    label4.place(x=10,y=40)
    liste=["Kahverengi","Kirmizi","Turuncu","Sari","Yesil","Mavi","Mor","Gri","Beyaz"]
    #kutu1
    kutu1 = Combobox(form,values=liste)
    kutu1.place(x=10,y=70,width=80)
    #kutu2
    listem=["Siyah","Kahverengi","Kirmizi","Turuncu","Sari","Yesil","Mavi","Mor","Gri","Beyaz"]
    kutu2 = Combobox(form,values=listem)
    kutu2.place(x=100,y=70,width=80)
    #kutu3
    liste2=["Siyah","Kahverengi","Kirmizi","Turuncu","Sari","Yesil","Mavi","Altin","Gumuş"]
    kutu3 = Combobox(form,values=liste2)
    kutu3.place(x=190,y=70,width=80)
    #kutu4
    listem4=["Kahverengi","Kirmizi","Altin","Gumus"]
    kutu4 = Combobox(form,values=listem4)
    kutu4.place(x=280,y=70,width=80)

    def hesapla():
        if len(kutu1.get())==0 or len(kutu2.get())==0 or len(kutu3.get())==0 or len(kutu4.get())==0:
            messagebox.showinfo("Lütfen Boş Bırakma",message="Boş Alanları Doldurunuz!!!")
        else:
            sozluk1 ={"Siyah":0,"Kahverengi":1,"Kirmizi":2,"Turuncu":3,"Sari":4,"Yesil":5,"Mavi":6,"Mor":7,"Gri":8,"Beyaz":9}
            sozluk2 = {"Siyah": 1, "Kahverengi": 10, "Kirmizi": 100, "Turuncu": 1000, "Sari": 10000, "Yesil": 100000, "Mavi": 1000000,"Altin":0.1,"Gumus":0.01}
            sozluk3={"Kahverengi":1,"Kirmizi":2,"Altin":5,"Gumus":10}
            deger1=kutu1.get()
            deger2=kutu2.get()
            deger3=kutu3.get()
            deger4=kutu4.get()

            ohm1 = str(sozluk1[deger1])+str(sozluk1[deger2])+"x"+str(sozluk2[deger3])+"="+str(sozluk1[deger1])+str(sozluk1[deger2])+str(sozluk2[deger3])[1:]+" Ohm"
            tolerans ="% "+str(sozluk3[deger4])
            ohm = tk.Label(form, text="Ohm Degeri:")
            ohm.place(x=10, y=120)
            label=tk.Label(form,text=ohm1)
            label.place(x=90,y=120)
            label = tk.Label(form, text="Tolerans Degeri:")
            label.place(x=10, y=150)
            label = tk.Label(form, text=tolerans)
            label.place(x=120, y=150)


    buton1 = tk.Button(form,text="Hesapla",command=hesapla)
    buton1.place(x=380,y=67)


#Beş bantlı direnç başlangıç
def besBantlı():
    label4 = tk.Label(form,text="5 Bantlı Dirençler İçin Renk Kodu Okuma",bg="black",fg="white")
    label4.place(x=10,y=190)
    liste=["Kahverengi","Kirmizi","Turuncu","Sari","Yesil","Mavi","Mor","Gri","Beyaz"]
    #kutu1
    kutu1 = Combobox(form,values=liste)
    kutu1.place(x=10,y=220,width=70)
    #kutu2
    listem=["Siyah","Kahverengi","Kirmizi","Turuncu","Sari","Yesil","Mavi","Mor","Gri","Beyaz"]
    kutu2 = Combobox(form,values=listem)
    kutu2.place(x=100,y=220,width=70)
    #kutu3

    kutu3 = Combobox(form,values=listem)
    kutu3.place(x=190,y=220,width=70)
    #kutu4
    liste2=["Siyah","Kahverengi","Kirmizi","Turuncu","Sari","Yesil","Mavi","Altin","Gumuş"]
    kutu4 = Combobox(form,values=liste2)
    kutu4.place(x=280,y=220,width=70)
    #kutu5
    listem5 = ["Kahverengi","Kirmizi","Altin","Gumus"]
    kutu5 = Combobox(form,values=listem5)
    kutu5.place(x=370,y=220,width=70)

    def hesapla():
        if len(kutu1.get())==0 or len(kutu2.get())==0 or len(kutu3.get())==0 or len(kutu4.get())==0 or len(kutu5.get())==0:
            messagebox.showinfo("Lütfen Boş Bırakma",message="Boş Alanları Doldurunuz!!!")
        else:
            sozluk1 ={"Siyah":0,"Kahverengi":1,"Kirmizi":2,"Turuncu":3,"Sari":4,"Yesil":5,"Mavi":6,"Mor":7,"Gri":8,"Beyaz":9}
            sozluk2 = {"Siyah": 1, "Kahverengi": 10, "Kirmizi": 100, "Turuncu": 1000, "Sari": 10000, "Yesil": 100000, "Mavi": 1000000,"Altin":0.1,"Gumus":0.01}
            sozluk3={"Kahverengi":1,"Kirmizi":2,"Altin":5,"Gumus":10}
            deger1=kutu1.get()
            deger2=kutu2.get()
            deger3=kutu3.get()
            deger4=kutu4.get()
            deger5=kutu5.get()

            ohm1 = str(sozluk1[deger1])+str(sozluk1[deger2])+str(sozluk1[deger3])+"x"+str(sozluk2[deger4])+"="+str(sozluk1[deger1])+str(sozluk1[deger2])+str(sozluk1[deger3])+str(sozluk2[deger3])[1:]+" Ohm"

            tolerans ="% "+str(sozluk3[deger5])
            ohm = tk.Label(form, text="Ohm Degeri:")
            ohm.place(x=10, y=250)
            label=tk.Label(form,text=ohm1)
            label.place(x=90,y=250)
            label = tk.Label(form, text="Tolerans Degeri:")
            label.place(x=10, y=280)
            label = tk.Label(form, text=tolerans)
            label.place(x=120, y=280)


    buton2 = tk.Button(form,text="Hesapla",command=hesapla)
    buton2.place(x=450,y=215)

#Altı bantlı direnç başlangıç
def altıBantlı():
    label4 = tk.Label(form,text="6 Bantlı Dirençler İçin Renk Kodu Okuma",bg="black",fg="white")
    label4.place(x=10,y=340)
    liste=["Kahverengi","Kirmizi","Turuncu","Sari","Yesil","Mavi","Mor","Gri","Beyaz"]
    #kutu1
    kutu1 = Combobox(form,values=liste)
    kutu1.place(x=10,y=370,width=70)
    #kutu2
    listem=["Siyah","Kahverengi","Kirmizi","Turuncu","Sari","Yesil","Mavi","Mor","Gri","Beyaz"]
    kutu2 = Combobox(form,values=listem)
    kutu2.place(x=100,y=370,width=70)
    #kutu3

    kutu3 = Combobox(form,values=listem)
    kutu3.place(x=180,y=370,width=70)
    #kutu4
    liste2=["Siyah","Kahverengi","Kirmizi","Turuncu","Sari","Yesil","Mavi","Altin","Gumuş"]
    kutu4 = Combobox(form,values=liste2)
    kutu4.place(x=270,y=370,width=70)
    #kutu5
    listem5 = ["Kahverengi","Kirmizi","Altin","Gumus"]
    kutu5 = Combobox(form,values=listem5)
    kutu5.place(x=360,y=370,width=70)
    #kutu6
    kutu6 = Combobox(form,values=listem5)
    kutu6.place(x=440,y=370,width=70)

    def hesapla():
        if len(kutu1.get())==0 or len(kutu2.get())==0 or len(kutu3.get())==0 or len(kutu4.get())== 0 or len(kutu5.get())==0 or len(kutu6.get())==0:
            messagebox.showinfo("Lütfen Boş Bırakma",message="Boş Alanları Doldurunuz!!!")
        else:
            sozluk1 ={"Siyah":0,"Kahverengi":1,"Kirmizi":2,"Turuncu":3,"Sari":4,"Yesil":5,"Mavi":6,"Mor":7,"Gri":8,"Beyaz":9}
            sozluk2 = {"Siyah": 1, "Kahverengi": 10, "Kirmizi": 100, "Turuncu": 1000, "Sari": 10000, "Yesil": 100000, "Mavi": 1000000,"Altin":0.1,"Gumus":0.01}
            sozluk3={"Kahverengi":1,"Kirmizi":2,"Altin":5,"Gumus":10}
            sozluk4 = {"Siyah": 250, "Kahverengi": 100, "Kirmizi": 50, "Turuncu": 15, "Sari": 25, "Yesil": 20, "Mavi": 10, "Mor": 5, "Gri": 1}
            deger1=kutu1.get()
            deger2=kutu2.get()
            deger3=kutu3.get()
            deger4=kutu4.get()
            deger5=kutu5.get()
            deger6=kutu6.get()


            ohm1 = str(sozluk1[deger1])+str(sozluk1[deger2])+str(sozluk1[deger3])+"x"+str(sozluk2[deger4])+"="+str(sozluk1[deger1])+str(sozluk1[deger2])+str(sozluk1[deger3])+str(sozluk2[deger3])[1:]+" Ohm"

            tolerans ="% "+str(sozluk3[deger5])
            ohm = tk.Label(form, text="Ohm Degeri:")
            ohm.place(x=10, y=400)
            label=tk.Label(form,text=ohm1)
            label.place(x=90,y=400)
            label = tk.Label(form, text="Tolerans Degeri:")
            label.place(x=10, y=440)
            label = tk.Label(form, text=tolerans)
            label.place(x=120, y=440)
            label = tk.Label(form, text="Sıcaklık Degeri:")
            label.place(x=120, y=490)
            sıcak=str(sozluk4[deger6]) + " ppm/K"
            sıcaklık = tk.Label(form, text=sıcak)
            sıcaklık.place(x=120, y=490)


    buton3 = tk.Button(form,text="Hesapla",command=hesapla)
    buton3.place(x=530,y=370)


var=tk.IntVar()

dort_bant =tk.Radiobutton(form,text="Dört Bantlı",value=1,variable=var,command=dortBantlı)
dort_bant.place(x=160,y=10)
bes_bant =tk.Radiobutton(form,text="Beş Bantlı",value=1,variable=var,command=besBantlı)
bes_bant.place(x=260,y=10)
altı_bant =tk.Radiobutton(form,text="Altı Bantlı",value=1,variable=var,command=altıBantlı)
altı_bant.place(x=360,y=10)


form.geometry("640x480+500+200")
form.mainloop()
