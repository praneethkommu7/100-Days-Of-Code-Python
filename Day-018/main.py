import random
from turtle import Turtle, Screen, colormode

tim = Turtle()
tim.shape('turtle')
# tim.color('red')
#
# tim.forward(100)
# tim.right(90)

# Draw a square
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)

# Draw a dashed line
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Different Shapes
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
          "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
#
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)


# random walk
# tim.pensize(10)
# tim.speed(10)
# for _ in range(50):
#     tim.forward(30)
#     tim.color(random.choice(colors))
#     tim.setheading(random.choice(directions))


# Random RGB color
colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


tim.pensize(10)
for _ in range(50):
    tim.forward(30)
    tim.color(random_color())
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
