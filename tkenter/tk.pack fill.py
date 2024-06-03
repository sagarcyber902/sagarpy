import tkinter as tk
win=tk.Tk()
frame1=tk.Frame(master=win,height=100,bg="orange")
#adding the fill argument
frame1.pack(fill=tk.X)
frame2=tk.Frame(master=win,height=100,bg="white")
frame2.pack(fill=tk.X)
frame3=tk.Frame(master=win,height=100,bg="green")
frame3.pack(fill=tk.X)
win.mainloop()