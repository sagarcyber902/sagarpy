from tkinter import *
import tkinter as tk
from tkinter import messagebox
from requests import get
import tkinter.messagebox

base = Tk()
base.title("Weather App")
base.config(bg="Black")
base.geometry("500x500")


def weather_response_format(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = int(weather['main']['temp'] - 273)
        humidity=weather['main']['humidity']
        wind_speed=weather['wind']['speed']

        display_str = 'City: %s \nConditions: %s \nTemperature(°C): %s \nHumidity: %s \nWind Speed: %s ' % (name, desc, temp,humidity,wind_speed)
    except:
        display_str = '''Sorry!
        City not found,Please try again!'''

    return display_str



def get_weather(city):
    weather_key = '14ed2a78adcbcbfe1ac9d1ffb8c5eea6'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city}
    weather_response = get(url, params=params)
    weather = weather_response.json()

    label['text'] = weather_response_format(weather)

def close_app():
    closeapp = tkinter.messagebox.askyesno("Weather App", "Do you want to exit App?")
    if closeapp > 0:
        base.destroy()
        return

def about():
    about = tkinter.messagebox.showinfo(title="About", message='''Made for PBL Project by
Sagar
Abhishek
Kedar
Karan''')
    return



# menu bars


menubar = Menu(base)
base.configure(menu=menubar)
submenu1 = Menu(menubar)
submenu2 = Menu(menubar)
menubar.add_cascade(label="File", menu=submenu1)
menubar.add_cascade(label="Help", menu=submenu2)

submenu1.add_command(label="Exit", command=close_app)
submenu2.add_command(label="About", command=about)

frame = Frame(base, bg='light blue', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = Entry(frame, font=('Courier', 15))
entry.place(relwidth=0.65, relheight=1)

button = Button(frame, text="Get Weather", font=('Times New Roman', 12), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)


lower_frame = Frame(base, bg='light blue', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = Label(lower_frame, background="white", font=('Times New Roman', 18))
label.place(relwidth=1, relheight=1)

base.mainloop()