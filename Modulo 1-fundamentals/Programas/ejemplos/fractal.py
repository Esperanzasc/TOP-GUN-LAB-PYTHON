import turtle
from random import randint

def generate_color():
    p = lambda: randint(0,255)
    return f"#{p():02x}{p():02x}{p():02x}"

def draw_triangle(side, lvl):
    turtle.fillcolor(generate_color())
    if lvl == 0:
        for _ in range(3):
            turtle.forward(side)
            turtle.left(120)
    else:
        turtle.begin_fill()
        draw_triangle(side / 2, lvl - 1)
        turtle.forward(side / 2)
        draw_triangle(side / 2, lvl - 1)
        turtle.backward(side / 2)
        turtle.left(60)
        turtle.forward(side / 2)
        turtle.right(60)
        draw_triangle(side / 2, lvl - 1)
        turtle.left(60)
        turtle.backward(side / 2)
        turtle.right(60)
        turtle.end_fill()
def main():
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-200, -200)
    turtle.pendown()
    draw_triangle(300, 4)
    turtle.done()

if __name__ == "__main__":
    main()