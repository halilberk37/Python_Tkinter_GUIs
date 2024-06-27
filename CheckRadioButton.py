import tkinter as tk

form = tk.Tk()
form.title("Buton Çeşitleri")

x=tk.IntVar()
x.set(0)

def onay():
    if x.get() == 0 :
        print("Kabul Edilmedi")
    else:
        print("Kabul Edildi")


check = tk.Checkbutton(form,text="Kabu Et",fg="Black",bg="White",variable=x,command=onay)
check.place(x=10,y=20)

def kontrol():
    if y.get()=="1":
        print("Radio1")
    else:
        print("Radio2")

buton = tk.Button(form,text="Buton",fg="Red",bg="black",activebackground="green",command=kontrol)
buton.pack()

y= tk.StringVar()

radio = tk.Radiobutton(form,text="Radio",activebackground="red",value="1",variable=y)
radio.pack()

radio1 = tk.Radiobutton(form,text="Radio1",activebackground="Green",value="2",variable=y)
radio1.pack()

form.geometry("500x500+500+300")
form.mainloop()