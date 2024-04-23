from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle() 

leo.forward(50)
leo.left(30)
leo.right(40)
done()

# form square 
i: int = 0
while (i < 4):
    leo.forward(300)
    leo.left(90)
    i = i + 1

# lift the turtle off of the page
leo.penup()
leo.goto(45, 60)
leo.pendown()

# form triangle 
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1

# specific color wanted to be filled in
leo.color(99, 204, 250)

leo.begin_fill()
# code for shape to be filled at correct positioning
leo.end_fill()

# useful color commands 
leo.pencolor("pink")
leo.fillcolor(32, 67, 93)
leo.color("green", "yellow")

# changes the speed of the turtle
leo.speed(50)

# to end the filling of turtle
leo.hideturtle()
