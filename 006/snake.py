#! python3.6


import turtle


def draw_snake(self, rad, angle, length, neck_rad):
    for i in range(length):
        self.circle(rad, angle)
        self.circle(-rad, angle)
    self.circle(rad, angle / 2)
    self.forward(rad)
    self.circle(neck_rad + 1, 180)
    self.forward(rad * 2 / 3)


if __name__ == '__main__':
    turtle_obj = turtle.Turtle()
    turtle_obj.screen.setup(800, 400)
    turtle_obj.speed(0)
    turtle_obj.penup()
    turtle_obj.setposition(60 - turtle_obj.screen.window_width() / 2, 0)
    turtle_obj.pendown()
    turtle_obj.speed('normal')
    python_size = 30
    turtle_obj.pensize(python_size)
    turtle_obj.pencolor('blue')
    turtle_obj.setheading(-40)
    draw_snake(turtle_obj, 40, 80, 5, python_size / 2)
    turtle_obj.screen.exitonclick()
