import turtle

background = turtle.Screen()
rat = turtle.Turtle()
rat.hideturtle()

for i in range(5):
    rat.forward(200)
    rat.right(144)

background.mainloop()

turtle.done()