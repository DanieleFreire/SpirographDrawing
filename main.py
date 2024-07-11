import turtle
from turtle import Turtle, Screen
import random

#tim = Turtle()
# tim.shape("turtle")
# tim.color("green", "red")
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)

tom = Turtle()
turtle.colormode(255)
#tom.shape("turtle")

# for i in range(4):
#     tom.forward(100)
#     tom.right(90)

# for i in range(15):
#     tom.forward(10)
#     tom.color("white")
#     tom.forward(10)
#     tom.color("black")

# for i in range(15):
#     tom.forward(10)
#     tom.penup()
#     tom.forward(10)
#     tom.pendown()

# for i in range(4):
#     tom.random(colormode())
#     tom.forward(100)
#     tom.right(90)
# for i in range(3):
#     tom.color("red")
#     tom.forward(100)
#     tom.right(120)
# for i in range(4):
#     tom.color("green")
#     tom.forward(100)
#     tom.right(90)
# for i in range(5):
#     tom.color("blue")
#     tom.forward(100)
#     tom.right(72)
# for i in range(6):
#     tom.color("yellow")
#     tom.forward(100)
#     tom.right(60)
# for i in range(7):
#     tom.color("purple")
#     tom.forward(100)
#     tom.right(51.42)
# for i in range(8):
#     tom.color("teal")
#     tom.forward(100)
#     tom.right(45)
# for i in range(9):
#     tom.color("violet")
#     tom.forward(100)
#     tom.right(40)
# for i in range(10):
#     tom.color("magenta")
#     tom.forward(100)
#     tom.right(36)

#tom.color('black', 'green')
tom.shape('turtle')
#tom.pensize(15)
tom.speed("fastest")


#colours = ['cornflower blue', 'dark olive green', 'dark orchid', 'dark blue', 'lime green', 'peach puff', 'medium violet red', 'yellow green']

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


angles = [0, 90, 180, 270]

#3) Make a spirograph

#tom.speed("fastest")

def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tom.color(random_color())
        tom.circle(100)
        tom.setheading(tom.heading() + size_of_gap)
        #tom.left(5)


draw_spirograph(5)


#2) Make a random walk
# for i in range(200):
#     colour = random_color()
#     tom.pencolor(colour)
#     tom.forward(20)
#     tom.seth(random.choice(angles))

#1) Make 10 shapes
# def make_shape(num_sides):
#     for i in range(num_sides):
#         tom.forward(100)
#         tom.right(360.0 / num_sides)


# for i in range(3, 11):
#     #tom.color(random.choice(colours))
#     colour = random_color()
#     tom.screen.colormode(255)
#     tom.pencolor(colour)
#     make_shape(i)



screen = Screen()
screen.exitonclick()
