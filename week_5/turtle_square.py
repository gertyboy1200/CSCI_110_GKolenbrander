import turtle

background = turtle.Screen()
rat = turtle.Turtle()

rat.pensize(3)
background.bgcolor('lightgreen')
rat.pencolor('magenta')
rat.hideturtle()

for i in range(5):
    for j in range(4):
        rat.forward(20 * (i + 1))
        rat.right(90)
    rat.penup()
    rat.backward(10)
    rat.left(90)
    rat.forward(10)
    rat.right(90)
    rat.pendown()

background.mainloop()

turtle.done()
