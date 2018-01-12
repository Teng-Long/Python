#! python3.6


import turtle


turtle_obj = turtle.Turtle()
turtle_obj.pensize(2)
turtle_obj.screen.bgcolor('black')
turtle_obj.speed(0)
colors = ['red', 'yellow', 'purple', 'blue']
# turtle_obj.screen.tracer(False)
for i in range(640):
    turtle_obj.forward(2 * i)
    turtle_obj.color(colors[i % 4])
    turtle_obj.left(91)
# turtle_obj.screen.tracer(True)
turtle_obj.screen.mainloop()
