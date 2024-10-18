try:
    number = int(input("請輸入一個數字: "))
except:
    print("請輸入數字: ")
else:
    if number % 2 == 0:
        print("這是一個偶數")
    else:
        print("這是一個奇數")
print("--------------------")
# 匯入模組
# import turtle 匯入turtle
import turtle as t  # 匯入模組turtle並取別名為t

# from turtle import * 匯入模組turtle的所有指令
# from turtle import done * 匯入模組turtle的done指令

# done()
# turtle.done()
t.forward(100)  # 向前移動100單位
t.backward(200)  # 向後移動200單位
# 發現turtle一開始面相右邊
t.done()  # 讓視窗不要關閉

t.speed(1)  # 設定速度為1
t.forward(100)  # 向前移動100單位
t.left(90)  # 向左移動90度
t.forward(100)  # 向前移動100單位
# 發現turtle一開始面相右邊
t.done()  # 讓視窗不要關閉
print("--------------------")
# for example
# for的組成只有三個部分
# for 迴圈變數 in 範圍:
# 迴圈變數只能活在for迴圈裡面
# 迴圈變數每回合都會從漢為中取出一個值
for i in range(6):  # range可以產出一組數字0-5
    print(i)  # 印出0~5

for i in range(1, 6):  # 1~5
    print(i)  # 印出1~5

for i in range(1, 6, 2):  # 1, 3, 5
    print(i)  # 印出1, 3, 5
print("--------------------")
import turtle as t

t.penup()  # 提筆,這樣就不會畫線但是可以移動
t.stamp()  # 蓋一個印章
for i in range(4):
    t.forward(100)  # 向前移動100單位
    t.stamp()  # 蓋一個印章
    t.right(90)  # 向右移動90度

t.done()  # 讓視窗不要關閉
print("--------------------")
