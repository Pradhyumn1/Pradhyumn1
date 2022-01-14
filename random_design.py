from turtle import *
speed(0)
bgcolor('black')
pencolor("yellow")


for i in range(250):
    right(i)
    circle(280, i)
    forward(i)
    right(120)
    forward(200)

hideturtle()
done()
