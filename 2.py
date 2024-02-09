import turtle

def draw_tree(t, level, size):
    if level == 0:
        return
    else:
        t.forward(size)
        t.right(45)
        draw_tree(t, level - 1, size * 0.7)
        t.left(90)
        draw_tree(t, level - 1, size * 0.7)
        t.right(45)
        t.backward(size)

def draw(level):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(4)
    t.penup()
    t.setpos(0, -200)
    t.pendown()
    t.left(90)

    draw_tree(t, level, 200)

    window.mainloop()

user_input = int(input("Enter the recursion level: "))
draw(user_input)
