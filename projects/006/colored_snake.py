#! python3.6


import turtle


def draw_snake(self, rad, angle, length, neck_rad):
    colors = ['red', 'yellow', 'purple', 'blue']
    for i in range(length):
        self.color(colors[i % 4])
        self.circle(rad, angle)
        self.circle(-rad, angle)
    self.color(colors[(length + 1) % 4])
    self.circle(rad, angle / 2)
    self.forward(rad)
    self.circle(neck_rad + 1, 180)
    self.forward(rad * 2 / 3)


if __name__ == '__main__':
    snake_number = 7
    python_size = 30
    python_heading = 0
    turtle_obj = turtle.Turtle()
    turtle_obj.screen.setup(125 * snake_number, 320)
    turtle_obj.speed(0)
    turtle_obj.penup()
    turtle_obj.setposition(python_size - turtle_obj.screen.window_width() / 2, 0)
    turtle_obj.pendown()
    turtle_obj.speed('normal')
    turtle_obj.pensize(python_size)
    turtle_obj.pencolor('blue')
    turtle_obj.setheading(python_heading - 40)
    draw_snake(turtle_obj, 40, 80, snake_number, python_size / 2)
    turtle_obj.screen.exitonclick()
