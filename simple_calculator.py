from tkinter import END, Button, Entry, Label, Tk, messagebox

root = Tk()
root.title("Simple calculator")


def on_validate_input(P):
    if P == "" or P.isdigit() or (P.count(".") == 1 and P.replace(".", "").isdigit()):
        return True
    else:
        return False

validate_input = root.register(on_validate_input)

for i in range(2):
    root.columnconfigure(i, weight=1)

val_1_label = Label(root, text="First value:")
val_1_label.grid(row=0, padx=20)
val_1 = Entry(root, validate="key", validatecommand=(validate_input, "%P"))
val_1.grid(row=1, padx=20, pady=10)

val_2_label = Label(root, text="Second value:")
val_2_label.grid(row=0, column=1, padx=20)
val_2 = Entry(root, validate="key", validatecommand=(validate_input, "%P"))
val_2.grid(row=1, column=1, padx=20, pady=10)


def do_operation(operation):
    first_value = second_value = result = 0
    if operation in ["+", "-", "*", "/"]:
        try:
            first_value = float(val_1.get())
            second_value = float(val_2.get())
        except:
            messagebox.showerror("Error", "Please input numeric values!")

    match operation:
        case "+":
            result = first_value + second_value
        case "-":
            result = first_value - second_value
        case "*":
            result = first_value * second_value
        case "/":
            if second_value == 0:
                messagebox.showerror("Error", "The divisor must not be 0!")
                return
            result = first_value / second_value
        case _:
            val_1.delete(0, END)
            val_2.delete(0, END)
    result_label.config(text=f"Result: {result:.2f}")


Button(root, text="+", command=lambda: do_operation("+")).grid(
    row=2, column=0, sticky="ew", padx=20, pady=10
)
Button(root, text="-", command=lambda: do_operation("-")).grid(
    row=2, column=1, sticky="ew", padx=20, pady=10
)
Button(root, text="*", command=lambda: do_operation("*")).grid(
    row=3, column=0, sticky="ew", padx=20, pady=10
)
Button(root, text="/", command=lambda: do_operation("/")).grid(
    row=3, column=1, sticky="ew", padx=20, pady=10
)
Button(root, text="Clear", command=lambda: do_operation("Clear")).grid(
    row=4, columnspan=2, sticky="ew", padx=20, pady=10
)

result_label = Label(root, text="Result: 0.00", anchor="w", justify="left")
result_label.grid(row=5, columnspan=2, padx=20, pady=10, sticky="ew")

root.mainloop()
