import turtle as t
import time

t.speed(0)
for j in range(60):
    for i in range(1, 13):
        t.penup()
        t.forward(100)
        t.stamp()
        t.backward(100)
        t.right(30)

    print(6 * j)
    t.right(6 * j)
    t.pendown()
    t.forward(90)
    t.backward(90)
    time.sleep(1)
    t.clear()
    t.left(6 * j)

t.done()
