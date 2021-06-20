from turtle import *

fillcolor('purple')
pencolor('blue')

def triangle(n):
    forward(n)
    left(120)
    forward(n)
    left(120)
    forward(n)

begin_fill()
triangle(50)
end_fill()

penup()
left(120)
forward(200)

pendown()
triangle(100)
