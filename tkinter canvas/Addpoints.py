from tkinter import*
canvas_w=200
canvas_h=200
python_green="#476042"
master=Tk()
Can=Canvas(master,width=canvas_w,height=canvas_h)
Can.pack()
points=points=[0,0,0,200,100,100,50,90]
Can.create_polygon(points,outline=python_green,fill="green",width=3)
mainloop()