import turtle


WIDTH = 1000
HEIGHT = 1000


def draw_square(x, y, length):
    turtle.penup()
    turtle.setpos(x, y)
    
    turtle.pendown()
    turtle.forward(length)
    turtle.right(90)

    turtle.forward(length)
    turtle.right(90)

    turtle.forward(length)
    turtle.right(90)

    turtle.forward(length)
    turtle.right(90)


def draw_carpet(offset_x, offset_y, length, level):
    if level > 0:
        sublength = length // 3
        draw_square(offset_x + sublength, offset_y - sublength, sublength)

        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    pass
                else:
                    draw_carpet(offset_x + i * sublength, offset_y - j * sublength, sublength, level - 1)

def main():
    screen = turtle.Screen()

    screen.setup(WIDTH, HEIGHT)
    screen.screensize(WIDTH, HEIGHT)

    screen.title("Sierpinski Carpet")

    turtle.speed("fastest")
    draw_carpet(0, 0, 300, level=5)

    turtle.done()

# 5! -> 5 * 4 * 3 * 2 * 1

# 3! -> 3 * 2 * 1

# n! -> n * (n - 1) * (n - 2) * .... * 2 * 1

# 4! -> 4 * 3 * 2 * 1

# 5! -> 5 * 4!


def factorial_1(n):
    fac = 1
    for i in range(1, n):
        fac *= i

    return fac


def factorial_2(n):
    if n == 1:
        return 1
    else:
        fac = n * factorial_2(n - 1)
        return fac

# stack
# factorial_2(3) -> fac = 3 * factorial_2(2)
# factorial_2(2) -> fac = 2 * factorial_2(1)
# factorial_2(1) -> fac = 1

print(factorial_2(4))


if __name__ == '__main__':
    main()