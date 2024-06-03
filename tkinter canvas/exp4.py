import tkinter
from tkinter import *

top=tkinter.Toplevel()
Can=tkinter.Canvas(top,bg="blue",height=500,width=500)
imagename=tkinter.PhotoImage(file="C:\\Users\\ASUS\\Downloads\\—Pngtree—instagram logo social media instagram_3572487.png")
image=Can.create_image(50,50,image=imagename)
coord=10,50,400,200
arc=Can.create_image(700,400,image=imagename)
Can.pack(fill=tkinter.BOTH,expand=1)
top.mainloop()