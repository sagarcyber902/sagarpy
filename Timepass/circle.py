import turtle

turtle.bgcolor("black")
turtle.pensize(3)
turtle.speed(0)
b=["red","blue","green","purple","orange","indigo","violet"]
for i in range(9):
    for a in b:
        turtle.color(a)
        turtle.circle(100)
        turtle.left(10)
turtle.mainloop()