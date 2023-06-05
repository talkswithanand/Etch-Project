from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def move_leftward():
    t.left(10)

def move_rightward():
    t.right(10)

def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

screen.listen()


screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_leftward, "a")
screen.onkey(move_rightward, "d")
screen.onkey(clear, "c")

screen.exitonclick()
