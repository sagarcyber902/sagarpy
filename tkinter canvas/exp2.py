import tkinter
top=tkinter.Tk()
Can=tkinter.Canvas(top,bg="red",height=300,width=300)
arc=Can.create_oval(100,100,300,200,fill="grey")
Can.pack()
top.mainloop()