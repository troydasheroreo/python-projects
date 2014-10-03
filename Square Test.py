'''
penColour('#ff0000');
moveForward(100);
turnRight(90);
moveForward(100);
turnRight(90);
moveForward(100);
turnRight(90);
moveForward(100);
'''
from turtle import Turtle
from random import random

def random_color():
    return (random(),random(),random())

jane = Turtle()
jane.pensize(10)
jane.speed(0)
jane.hideturtle()


while True:

    for count in range(20):
        jane.pencolor(random_color())
        jane.forward(100)
        jane.right(120)
        jane.pencolor(random_color())
        jane.forward(100)
        jane.right(120)
        jane.pencolor(random_color())
        jane.forward(100)
        jane.right(120)
        
        
        
        
    

