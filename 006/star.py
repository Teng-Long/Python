#! python2.7

import turtle


turtle_obj = turtle.Turtle()
turtle_obj.fillcolor('red')
turtle_obj.begin_fill()
while True:
    turtle_obj.forward(200)
    turtle_obj.right(144)
    if abs(turtle_obj.pos()) < 1:
        break
turtle_obj.end_fill()
turtle_obj.screen.mainloop()

