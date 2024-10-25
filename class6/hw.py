import turtle as t

t.speed(0)
for j in range(61):
    for i in range(12):
        t.penup()
        t.forward(100)
        t.stamp()
        t.backward(100)
        t.right(30)

    t.left(90)
    t.right(6 * j)
    t.forward(90)
    t.pendown()
    t.backward(90)
    t.penup()
    t.clearscreen()
    t.speed(0)

t.done()
