import tkinter as tk

def show_value():
    label_value.config(text=f"Value: {var.get()}")

root = tk.Tk()
root.title("Variable Example")

# StringVar example with Entry widget
string_var = tk.StringVar()
entry = tk.Entry(root, textvariable=string_var)
entry.pack()

# IntVar example with Scale widget
int_var = tk.IntVar()
scale = tk.Scale(root, variable=int_var, from_=0, to=100, orient=tk.HORIZONTAL)
scale.pack()

# BooleanVar example with Checkbutton widget
bool_var = tk.BooleanVar()
checkbutton = tk.Checkbutton(root, text="Check me", variable=bool_var)
checkbutton.pack()

# DoubleVar example with Spinbox widget
double_var = tk.DoubleVar()
spinbox = tk.Spinbox(root, textvariable=double_var, from_=0.0, to=10.0, increment=0.1)
spinbox.pack()

# Radiobutton example with Radiobutton widgets
var = tk.StringVar(value="Option 1")
radio1 = tk.Radiobutton(root, text="Option 1", variable=var, value="Option 1")
radio2 = tk.Radiobutton(root, text="Option 2", variable=var, value="Option 2")
radio1.pack()
radio2.pack()

# Button to show the value of the selected options
btn_show_value = tk.Button(root, text="Show Value", command=show_value)
btn_show_value.pack()

# Label to display the selected value
label_value = tk.Label(root, text="Value: ")
label_value.pack()

root.mainloop()
