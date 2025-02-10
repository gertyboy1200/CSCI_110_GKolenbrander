import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
rat = turtle.Turtle()
data = [48, 117, 200, 240, 160, 260, 220]

def set_turtle(t):
    t.hideturtle()
    t.pensize(3)
    t.penup()
    t.goto(-200,-100)
    t.pendown()

def draw_bar(t, height):
    if(height >= 200):
        t.color("blue", "red")
    elif(100 <= height < 200):
        t.color("blue", "yellow")
    else:
        t.color("blue", "green")

    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write("  "+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.forward(10)

set_turtle(rat)

for value in data:
    draw_bar(rat, value)

turtle.done()
