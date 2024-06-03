import tkinter
top=tkinter.Tk()
Can=tkinter.Canvas(top,bg="red",height=300,width=300)
coord=100,100,300,200
arc=Can.create_arc(coord,start=0,extent=150,fill="grey")
Can.pack()
top.mainloop()