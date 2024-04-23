"""TODO: A house with 2 different windows, a tree, and used circle in function as my above and beyond."""
 
__author__ = "730553436"
 
from turtle import Turtle, colormode, done 
colormode(255)
 

def main() -> None:
    """The entrypoint of my scene where the variables are defined with their corresponding colors."""
    # TODO: Declare your Turtle variable(s) here.
    turtle: Turtle = Turtle()
    turtle.color(7, 34, 25)
    draw_rectangle(turtle, -100, 0, 150, 150)
    turtle.color(11, 48, 57)
    draw_triangle(turtle, -70, 150, 150)
    draw_door(turtle, -40, 0, 30, 50)
    turtle.color(18, 72, 95)
    draw_window(turtle, -80, 80, 30, 30)
    draw_window(turtle, 0, 80, 30, 30)
    turtle.color(46, 18, 4)
    draw_trunk(turtle, 100, 0, 30, 50)
    draw_leaves(turtle, 115, 50, 30)
    # TODO: Call the procedures you define and pass your Turtle(s) as an argument.
    done()


def starter(turtle: Turtle, x: float, y: float, angle: float) -> None:
    """Allows for decreased repetition."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(angle)
    turtle.pendown()
 

# TODO: Define the procedures for other components in your scene here.
def draw_rectangle(turtle: Turtle, x: float, y: float, width: float, height: float) -> None:
    """This function definition codes for the actual house shape."""
    starter(turtle, x, y, 0.0)

    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)


def draw_triangle(turtle: Turtle, x: float, y: float, side: float) -> None:
    """This function definition codes for the roof of the house as a triangle shape."""
    starter(turtle, x, y, 0.0)
    turtle.begin_fill()
    turtle.forward(side)
    turtle.left(135)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(135)
    turtle.forward(side)
    turtle.end_fill()


def draw_door(turtle: Turtle, x: float, y: float, width: float, height: float) -> None:
    """This function definition codes for the door on the house."""
    starter(turtle, x, y, 0.0)
    turtle.begin_fill()

    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()


def draw_window(turtle: Turtle, x: float, y: float, width: float, height: float) -> None:
    """This function definition codes for the first window."""
    starter(turtle, x, y, 0.0)
    turtle.begin_fill()

    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()


def draw_trunk(turtle: Turtle, x: float, y: float, width: float, height: float) -> None:
    """This function definition codes for the rectangular trunk of the tree."""
    starter(turtle, x, y, 0.0)
    turtle.begin_fill()

    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()


def draw_leaves(turtle: Turtle, x: float, y: float, radius: float) -> None:
    """This function definition codes for the leaves on the tree with recursion, and used circle as above and beyond."""
    if radius <= 10:
        return
    else:
        starter(turtle, x, y, 0.0)
        turtle.pencolor(1, 50, 32)
        turtle.fillcolor(144, 238, 144)
        turtle.begin_fill()
        turtle.circle(radius)
        turtle.end_fill()
        draw_leaves(turtle, x, y + 5, radius - 5)


# TODO: Use the __name__ is "__main__" idiom shown in class
if __name__ == "__main__":
    main()