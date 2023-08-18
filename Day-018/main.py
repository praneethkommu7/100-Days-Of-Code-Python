from turtle import Turtle, Screen

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
for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()



screen = Screen()
screen.exitonclick()
