#! python


import turtle


turtle_obj = turtle.Turtle()
turtle_obj.pensize(3)
for i in range(3):
    turtle_obj.forward(300)
    turtle_obj.left(120)
turtle_obj.screen.mainloop()
