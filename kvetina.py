import turtle
from turtle import *
turtle.speed(9)
color('red', 'grey')
n = 100

begin_fill()
while True:
    forward(2*n)
    left(170)
    if abs(pos()) < 1:
        break
left(10)
penup()
forward(n)
pendown()

for i in range(9):
    penup()
    forward(n)
    pendown()
    for i in range(35):
        forward(n)
        left(170)
    penup()
    left(10)
    forward(2*n)
    pendown()
        #righ(10)
    #forward(100)

end_fill()
done()
