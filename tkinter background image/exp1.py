from tkinter import*
import tkinter as tk
master=tk.Tk()
bgimg=tk.PhotoImage(file="Tulips.ppm")
#Specify the file name present in the same directory or else
#Specify the proper path for retrieving the image to set it as background image.
limg=Label(master,i=bgimg)
limg.pack()
master.mainloop()
