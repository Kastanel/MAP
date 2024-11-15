from tkinter import Button, Label, LabelFrame, Radiobutton, StringVar, Tk

root = Tk()
root.title("What are you?")

smoker_var = StringVar(value="smoker")
sex_var = StringVar(value="male")


def check_results():
    global sex_var, smoker_var
    sex = sex_var.get()
    smoker = smoker_var.get()

    result_label.config(text=f"You're a {smoker} {sex}!")


smoker_frame = LabelFrame(root, text="Are you a smoker? ")
smoker_frame.grid(row=0, column=0)

Radiobutton(
    smoker_frame,
    text="Smoker",
    value="smoker",
    variable=smoker_var,
    command=check_results,
).pack(anchor="w")
Radiobutton(
    smoker_frame,
    text="Non-Smoker",
    value="non-smoker",
    variable=smoker_var,
    command=check_results,
).pack(anchor="w")

sex_frame = LabelFrame(root, text="Sex")
sex_frame.grid(row=0, column=1)

Radiobutton(
    sex_frame, text="Male", value="male", variable=sex_var, command=check_results
).pack(anchor="w")
Radiobutton(
    sex_frame, text="Female", value="female", variable=sex_var, command=check_results
).pack(anchor="w")

result_label = Label(root, text=f"You're a {smoker_var.get()} {sex_var.get()}!")
result_label.grid(row=1, columnspan=2)

root.mainloop()
