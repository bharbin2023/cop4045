import turtle
my_turtle = turtle.Turtle()

def branch(length, level):
    if level <=0:
        return
    my_turtle.forward(length)
    my_turtle.left(45)
    branch(0.6*length, level -1)
    my_turtle.right(90)

    branch(0.6 * length, level-1)
    my_turtle.left(45)
    my_turtle.backward(length)
    return
turtle.delay(0)
my_turtle.left(90)
branch(100,5)

if __name__ == '__main__':
    branch(100,5)