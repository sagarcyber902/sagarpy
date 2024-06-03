import tkinter
top=tkinter.Toplevel()
Can=tkinter.Canvas(top,bg="blue",height=500,width=500)
imagename=tkinter.PhotoImage(file="C:/Users/ASUS/Pictures/sagar/IMG_20220306_112737.jpg")
image=Can.create_image(50,50,image=imagename)
Can.delete(image)
Can.pack()
top.mainloop()