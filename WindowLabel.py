import tkinter as tk

form = tk.Tk()
form.title("Pencere Arayüzü")
yazi = tk.Label(text= "Halil İbrahim BERK")
yazi.pack()

yazi2 = tk.Label(form,text="Bu formun üzerinde bir yazıyım.")
#Labelın formda gözükmesi için .pack kullanılıyor.
yazi2.pack()


form.mainloop()
