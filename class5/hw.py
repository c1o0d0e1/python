"""
作業說明:
讓turtle蓋出一個時鐘數字的位置
總共會蓋出12個印章
"""

import turtle as t

for i in range(12):
    t.penup()
    t.forward(100)
    t.stamp()
    t.backward(100)
    t.right(30)

t.done()
