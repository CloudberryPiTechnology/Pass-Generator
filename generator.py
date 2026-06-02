from tkinter import *
from tkinter import messagebox
import passwordcreate
root = Tk()
root.title("Pass-Generator")
root.geometry("500x500")
root.iconphoto(True, PhotoImage(file="./key.png"))
Label(root, text="Please enter the number of digits: ").pack()
digits=Entry(root)
digits.pack()
def run():
    try:
        n = digits.get()
        passw = passwordcreate.generate(int(n))
        messagebox.showinfo("Pass-Generator", "Password Generated and copied to clipboard")
        root.clipboard_clear()
        root.clipboard_append(passw)
    except Exception as e:
        messagebox.showerror("Pass-Generator", str(e))
Button(root, text="Generate", command=run).pack()
root.mainloop()