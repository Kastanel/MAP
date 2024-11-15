from tkinter import Tk, Label, Button, Entry
from tkinter import messagebox


def say_hi():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    messagebox.showinfo("Salutations", f"Hi, {first_name} {last_name}")


obj = Tk()

obj.geometry("350x350")
obj.title("This is a title")

Label(obj, text="First name:", font=("Arial", 12), fg="red", justify="left").grid(row=0)
Label(obj, text="Last name:", font=("Arial", 12), fg="red", justify="left").grid(row=1)

first_name_entry = Entry(obj)
first_name_entry.grid(row=0, column=1)
last_name_entry = Entry(obj)
last_name_entry.grid(row=1, column=1)

Button(obj, text="Hi", command=say_hi, justify="right", width=10).grid(
    row=2, sticky="w"
)


obj.mainloop()
