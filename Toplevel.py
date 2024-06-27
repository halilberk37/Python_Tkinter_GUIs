import tkinter as tk

form = tk.Tk()

form.title("Top Level / Yeni Sekme")


toplevel=tk.Toplevel(bg="Green")
toplevel.title("Yeni Sekme")
toplevel.geometry("250x400")



form.geometry("300x300")
form.mainloop()
toplevel.mainloop()