import turtle
import math

# Setup the turtle
t = turtle.Turtle()
t.speed(0)
t.color("red")
turtle.bgcolor("black")

# Heart equation
def corazon(t):
    x = 16 * math.sin(t) ** 3
    y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
    return x, y

# Draw hearts
t.penup()
for scale in range(1, 15):  # Scaling factor for each heart
    t.goto(0, 0)  # Return to the origin
    t.pendown()
    for n in range(0, 628):  # Loop from 0 to 2π in finer steps
        t_value = n / 100  # Convert to radians
        x, y = corazon(t_value)
        t.goto(x * scale, y * scale)
    t.penup()

# Hide the turtle and complete
t.hideturtle()
turtle.done()
