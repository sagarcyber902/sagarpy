import tkinter as tk
from tkinter import messagebox

# Function to validate login credentials
def validate_login(username, password):
    # Replace with your own validation logic
    if username == "id" and password == "1234":
        return True
    else:
        return False
def login():
    username = username_entry.get()
    password = password_entry.get()

    if validate_login(username, password):
        import PBL

    else:
        messagebox.showerror("Login", "Invalid username or password")
root = tk.Tk()
root.title("Weather Forecast App")
root.geometry("500x500")

# Create labels and entries for username, password
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

login_button = tk.Button(root, text="Login",activeforeground="blue", command=login)
login_button.pack()

root.mainloop()


