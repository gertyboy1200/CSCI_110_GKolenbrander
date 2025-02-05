import turtle

background = turtle.Screen()
background.bgcolor("lightgreen")
rat = turtle.Turtle()
rat.color("blue")
rat.hideturtle()

size = 100
rat.pensize(3)
rat.penup()

for j in range(12):
    rat.forward(80)
    rat.pendown()
    rat.forward(10)
    rat.penup()
    rat.backward(90)
    rat.left(30)

rat.shape("turtle")
rat.stamp()

for i in range(12):
    rat.forward(110)
    rat.stamp()
    rat.backward(110)
    rat.left(30)

background.mainloop()

turtle.done()