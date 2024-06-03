from tkinter import*
canvas_w=200
canvas_h=200
python_green="#476042"
master=Tk()
Can=Canvas(master,width=canvas_w,height=canvas_h)
Can.pack()
points=(0,0,100,100,0,100)
Can.create_polygon(points,outline=python_green,fill="red",width=3)
mainloop()
