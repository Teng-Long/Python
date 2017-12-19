## 用 turtle 绘图


- [x] [五角星](star.py)
- [x] [太阳花](sunflower.py)
- [x] [螺旋线](spiral_line.py)
- [x] [彩色螺旋线](colored_spiral_line.py)
- [x] [蟒蛇](snake.py)
- [x] [彩色蟒蛇](colored_snake.py)
- [x] [等边三角形](equilateral_triangle.py)
- [x] [时钟](time.py)

---


    _tg_classes = ['ScrolledCanvas', 'TurtleScreen', 'Screen',
                   'RawTurtle', 'Turtle', 'RawPen', 'Pen', 'Shape', 'Vec2D']
    _tg_screen_functions = ['addshape', 'bgcolor', 'bgpic', 'bye',
            'clearscreen', 'colormode', 'delay', 'exitonclick', 'getcanvas',
            'getshapes', 'listen', 'mainloop', 'mode', 'numinput',
            'onkey', 'onkeypress', 'onkeyrelease', 'onscreenclick', 'ontimer',
            'register_shape', 'resetscreen', 'screensize', 'setup',
            'setworldcoordinates', 'textinput', 'title', 'tracer', 'turtles', 'update',
            'window_height', 'window_width']
    _tg_turtle_functions = ['back', 'backward', 'begin_fill', 'begin_poly', 'bk',
            'circle', 'clear', 'clearstamp', 'clearstamps', 'clone', 'color',
            'degrees', 'distance', 'dot', 'down', 'end_fill', 'end_poly', 'fd',
            'fillcolor', 'filling', 'forward', 'get_poly', 'getpen', 'getscreen', 'get_shapepoly',
            'getturtle', 'goto', 'heading', 'hideturtle', 'home', 'ht', 'isdown',
            'isvisible', 'left', 'lt', 'onclick', 'ondrag', 'onrelease', 'pd',
            'pen', 'pencolor', 'pendown', 'pensize', 'penup', 'pos', 'position',
            'pu', 'radians', 'right', 'reset', 'resizemode', 'rt',
            'seth', 'setheading', 'setpos', 'setposition', 'settiltangle',
            'setundobuffer', 'setx', 'sety', 'shape', 'shapesize', 'shapetransform', 'shearfactor', 'showturtle',
            'speed', 'st', 'stamp', 'tilt', 'tiltangle', 'towards',
            'turtlesize', 'undo', 'undobufferentries', 'up', 'width',
            'write', 'xcor', 'ycor']
    _tg_utilities = ['write_docstringdict', 'done']
    
    __all__ = (_tg_classes + _tg_screen_functions + _tg_turtle_functions +
               _tg_utilities + ['Terminator']) # + _math_functions)
    
    _alias_list = ['addshape', 'backward', 'bk', 'fd', 'ht', 'lt', 'pd', 'pos',
                   'pu', 'rt', 'seth', 'setpos', 'setposition', 'st',
                   'turtlesize', 'up', 'width']
    
    _CFG = {"width" : 0.5,               # Screen
            "height" : 0.75,
            "canvwidth" : 400,
            "canvheight": 300,
            "leftright": None,
            "topbottom": None,
            "mode": "standard",          # TurtleScreen
            "colormode": 1.0,
            "delay": 10,
            "undobuffersize": 1000,      # RawTurtle
            "shape": "classic",
            "pencolor" : "black",
            "fillcolor" : "black",
            "resizemode" : "noresize",
            "visible" : True,
            "language": "english",        # docstrings
            "exampleturtle": "turtle",
            "examplescreen": "screen",
            "title": "Python Turtle Graphics",
            "using_IDLE": False
           }
