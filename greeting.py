import tkinter as tk    

root = tk.Tk()
root.title("Greeting")
root.geometry("500x300")
root.grid_columnconfigure(0, weight=1)

def say_hello():
	greeting_label.config(text="Hello, World!")

def greet_user():
    name = name_input.get()
    greeting_label.config(text=f"Hello, {name}!")

greeting_label = tk.Label(root, text= "Nothing to see here yet")
greeting_label.grid(row=0, column=0, pady=10)

hello_button = tk.Button(root, text="Click me!", command=say_hello)
hello_button.grid(row=1, column=0, pady=10)

name_input = tk.Entry(root, width=30)
name_input.grid(row=2, column=0, pady=10)

greet_button = tk.Button(root, text="Greet me!", command=greet_user)
greet_button.grid(row=3, column=0, pady=10)

root.mainloop()