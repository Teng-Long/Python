#! python3.6


import turtle


turtle_obj = turtle.Turtle()
turtle_obj.speed(8)
turtle_obj.color('red', 'yellow')
turtle_obj.begin_fill()
while True:
    turtle_obj.forward(300)
    turtle_obj.left(170)
    if abs(turtle_obj.pos()) < 1:
        break
turtle_obj.end_fill()
turtle_obj.screen.mainloop()
