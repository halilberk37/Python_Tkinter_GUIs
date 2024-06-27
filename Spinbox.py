import tkinter as tk

form = tk.Tk()

form.title("Spinbox and Background")

form.config(bg="blue")

deger=tk.IntVar()
spinbox = tk.Spinbox(form, from_=10,to=100,textvariable=deger).pack()

def verial():
    print(deger.get())


btn = tk.Button(form,text="veri al",command=verial).pack()

form.geometry("500x300")
form.mainloop()