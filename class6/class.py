import turtle as t

t.shape("star")
t.color("yellow")
for i in range(1, 100, 2):
    t.stamp()
    t.penup()
    t.backward(10 + i)
    t.left(15)

t.done()
# print("--------------------")

# import time
# print('開始計時')
# time.sleep(5) # 暫停5秒
# print('結束計時')
# print("--------------------")

# import turtle as t

# t.speed(1) # 設定畫筆速度
# t.penup() # 提筆,這樣就不會畫線但是可以移動

# for i in range(12)
#     t.forward(100) # 向前移動100單位
#     t.stamp() # 蓋一個印章
#     t.backward(100) # 向後移動100單位
#     t.right(30) # 向右移動30度

# t.right(6) # 轉六度
# t.pendown() # 提筆
# t.forward(80)   # 向前移動50，秒針出現了
# t.penup() # 提筆
# time.sleep(1) # 暫停1秒
# t.backward(80)   # 向後移動50，秒針消失了


# t.done() # 讓視窗不要關閉
# num = int(input("請輸入數字: "))
# sum = 0
# for i in range(num + 1):
#     sum = sum + i# print("--------------------")
# n

# print(f"0到{num}的總和為{sum}")
