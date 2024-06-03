import tkinter
top=tkinter.Toplevel()
Can=tkinter.Canvas(top,bg="blue",height=2000,width=2000)
imagename=tkinter.PhotoImage(file="C:\\Users\\ASUS\\Pictures\\sagar\\HappyColor_36877.png")
image=Can.create_image(800,500,image=imagename)
Can.pack()
top.mainloop()