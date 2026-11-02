import turtle
turt = turtle.Turtle()

def branch(length, level):
    if level <=0:
        return
    turt.forward(length * 0.6)
    turt.left(45)
    branch(0.6*length, level -1)

    turt.right(90)
    branch(0.6 * length, level-1)
    turt.left(45)
    turt.backward(length)

    return

def draw_leaf_straight(level, length):
    turt.up()
    turt.goto(0,-200)
    turt.down()
    turt.left(90)
    branch(length, level)

def main():
    turt.speed(4) 
    branch(100,10)
    turtle.delay(0)
    draw_leaf_straight(1,120)
    turtle.exitonclick()


if __name__ == '__main__': 
    main()