import turtle
from turtle import *
turtle.speed(9)
color('red', 'grey')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break

for i in range(4):
    right(30)
    for i in range(3):
        forward(200)
        for i in range(35):
            forward(100)
            left(170)
        #right(10)
    #forward(100)

end_fill()
done()