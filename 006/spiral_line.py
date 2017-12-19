#! python3.6


import turtle


turtle_obj = turtle.Turtle()
turtle_obj.speed(10)
turtle_obj.pensize(2)
for i in range(120):
    turtle_obj.forward(2 * i)
    turtle_obj.left(90)
turtle_obj.screen.mainloop()
