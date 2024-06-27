import tkinter as tk


form=tk.Tk()
form.title("Text Aracı")

text1 = tk.Text(form,width=20,heigh=20).place(x=300,y=100)
text2 = tk.Text(form,width=20,heigh=20,padx=10,pady=20,bg="gray",bd=20,selectbackground="Red",font="Times 10 italic").place(x=40,y=100)




form.geometry("500x500+500+400")
form.mainloop()