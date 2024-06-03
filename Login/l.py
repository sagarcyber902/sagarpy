import tkinter as tk
from tkinter import messagebox
import requests
import json

# Function to validate login credentials
def validate_login(username, password):
    # Replace with your own validation logic
    if username == "admin" and password == "password":
        return True
    else:
        return False

# Function to retrieve weather forecast data
def get_weather_forecast(city):
    # Replace 'YOUR_API_KEY' with your OpenWeatherMap API key
    api_key = '14ed2a78adcbcbfe1ac9d1ffb8c5eea6'
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(base_url)
    data = json.loads(response.text)

    return data

# Function to handle login button click event
def login():
    username = username_entry.get()
    password = password_entry.get()

    if validate_login(username, password):
        messagebox.showinfo("Login", "Login Successful")
        open_weather_forecast()
    else:
        messagebox.showerror("Login", "Invalid username or password")

# Function to handle weather forecast button click event
def open_weather_forecast():
    city = city_entry.get()

    # Get weather forecast data
    data = get_weather_forecast(city)

    # Extract relevant information from the data
    weather = data['weather'][0]['main']
    description = data['weather'][0]['description']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']

    # Display weather forecast in a message box
    messagebox.showinfo("Weather Forecast", f"Weather: {weather}\nDescription: {description}\nTemperature: {temperature}°F\nHumidity: {humidity}%")

# Create the main window
root = tk.Tk()
root.title("Weather Forecast App")

# Create labels and entries for username, password, and city
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

city_label = tk.Label(root, text="City:")
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()

# Create login button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack()

# Create weather forecast button
weather_button = tk.Button(root, text="Weather Forecast", command=open_weather_forecast)
weather_button.pack()

# Start the main loop
root.mainloop()
