import turtle

side = 100
for i in range(0, 2):
    turtle.forward(side)
    turtle.left(90)
    turtle.pencolor('red')
    turtle.shape("square")
for i in range(0, 3):

    turtle.forward(side)

    turtle.left(90)

    turtle.pencolor('green')
    
    turtle.shape ("circle")
