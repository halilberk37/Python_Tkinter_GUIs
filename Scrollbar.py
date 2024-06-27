import tkinter as tk

form = tk.Tk()
form.title("Scrollbar")


scrol=tk.Scrollbar()
scrol.pack(side=tk.RIGHT,fill=tk.Y)


listebox = tk.Listbox(form,yscrollcommand=scrol.get())


for i in range(500):
    listebox.insert("end","Tkinter Dersleri "+str(i))

listebox.pack(side=tk.LEFT)

scrol.config(command=listebox.yview)


form.mainloop()