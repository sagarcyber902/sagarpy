from tkinter import *
from tkinter import ttk
import requests


def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=d4ba774cc91f1685ecdcc1793a89acbd").json()
    w_label1.config(text=data["weather"][0]["main"])
    wd_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.5)))
    p_label1.config(text=data["main"]["pressure"])


win=Tk()
win.title("PBL Project")
win.config(bg="blue")
win.geometry("500x570")

name_label=Label(win,text="Weather forecast App",font=("Time New Roman",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)
city_name=StringVar()

com=ttk.Combobox(win,font=("Time New Roman",20,"bold"),textvariable=city_name)
com.place(x=70,y=120,height=40,width=350)

w_label=Label(win,text="Weather Climate",font=("Time New Roman",20))
w_label.place(x=25,y=260,height=50,width=210)
w_label1=Label(win,text="",font=("Time New Roman",20))
w_label1.place(x=250,y=260,height=50,width=210)

wd_label=Label(win,text="Weather Description",font=("Time New Roman",17))
wd_label.place(x=25,y=330,height=50,width=210)
wd_label1=Label(win,text="",font=("Time New Roman",17))
wd_label1.place(x=250,y=330,height=50,width=210)

temp_label=Label(win,text="Temperature",font=("Time New Roman",20))
temp_label.place(x=25,y=400,height=50,width=210)
temp_label1=Label(win,text="",font=("Time New Roman",20))
temp_label1.place(x=250,y=400,height=50,width=210)

p_label=Label(win,text="Pressure",font=("Time New Roman",20))
p_label.place(x=25,y=470,height=50,width=210)
p_label1=Label(win,text="",font=("Time New Roman",20))
p_label1.place(x=250,y=470,height=50,width=210)

done_button=Button(win,text="Done",command=data_get(),font=("Time New Roman",20,"bold"))
done_button.place(x=200,y=190,height=50,width=100)

win.mainloop()