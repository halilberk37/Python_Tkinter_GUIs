import tkinter as tk

background = tk.Tk()
background.title("Label Font Ayarları")
label = tk.Label(background,text ="Arayüz Dersleri")
label.pack()

label2 = tk.Label(background,text="Kırmızı Yazı",fg="red",bg="black")
label2.pack()

label3 = tk.Label(background,text="Arka Plan",fg="Black",bg="green")
label3.pack()

label4 = tk.Label(background,text="Halil BERK",fg="Blue",bg="Yellow",font="Times 40 italic")
label4.pack()

label5 = tk.Label(background,text="Georgia",fg="Green",bg="black",font="Georgia 30 bold")
label5.pack()
background.mainloop()