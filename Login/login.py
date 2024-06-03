import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "password":
        # Replace this with your weather forecast web application code
        messagebox.showinfo("Login Successful", "Welcome to the Weather Forecast App!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

root = tk.Tk()
root.title("Weather Forecast App - Login")
root.geometry("550x500")

# Create labels
username_label = tk.Label(root, text="Username:")
username_label.place
password_label = tk.Label(root, text="Password:")

# Create entry fields
username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")  # Mask password characters

# Create login button
login_button = tk.Button(root, text="Login", command=login)

# Grid layout
username_label.grid(row=0, column=0)
password_label.grid(row=1, column=0)
username_entry.grid(row=0, column=1)
password_entry.grid(row=1, column=1)
login_button.grid(row=2, column=0, columnspan=2)

root.mainloop()