import turtle
import colorsys


t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
# t.pencolor("red")
t.speed(0)
t.goto(0, 200)
a = 0
b = 0

n = 50
h = 0

while True:
    c = colorsys.hsv_to_rgb(h, 1, 0.9)
    h += 1/n
    t.color(c)
    t.forward(a)
    t.right(b)
    a += 3
    b += 1
    if b == 210:
        break
    t.hideturtle()

