x_1 = 0
x_2 = 0
x_3 = 299
x_4 = 0
x_5 = 50
def setup ():
    size (300, 300)
def draw():
    background(0)
    global x_1
    global x_2
    global x_3
    global x_4
    global x_5
    square(x_1, 30, 50)
    if x_1 > height:
       x_1 = 0
    else:
       x_1 = map(second(), 0, 59, 0, height)
    circle(x_2, 150, 60)
    if x_2 > height:
       x_2 = 0
    else:
       x_2 = map(minute(), 0, 59, 0, height)
    triangle(x_3, 200, x_4, 250, x_5, 250)
    if x_3 > height:
       x_3 = 25
    else:
       x_3 = map(hour(), 0, 23, 25, height)
    if x_4 > height:
       x_4 = 0
    else:
       x_4 = map(hour(), 0, 23, 0, height)
    if x_5 > height:
       x_5 = 50
    else:
       x_5 = map(hour(), 0, 23, 50, height)
