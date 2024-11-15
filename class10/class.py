import random

# random.randrange 設定範圍的方式跟randint一樣，特性也一樣不包含最後一個數字
# random.randrange 的功能是隨機取得一個數字， range式產生一組數字
print(random.randrange(10))  # 從0~9中隨機取得一個數字
print(random.randrange(1, 10))  # 從1~9中隨機取得一個數字
print(random.randrange(1, 10, 2))  # 從[1 , 3, 5, 7, 9]中隨機取得一個數字

# random.randint 設定範圍的方式必須要有開始跟結束， 且包含最後一個數字
# 不能跳數字抽籤
print(random.randint(1, 10))  # 從1~10中隨機取得一個數字

s = 1
n = int(input("請輸入1~100的整數: "))
m = random.randrange(1, 101)
while s == 5:
    while n != m:
        if m > n:
            print("在大一點")
            n = int(input("請輸入1~100的整數: "))
            s += 1
        elif m < n:
            print("在小一點")
            n = int(input("請輸入1~100的整數: "))
            s += 1

print("恭喜猜中!")

print("--------------------------------")

# List 清單
# List 可以存入很多資料，每筆資料用`,`隔開
# List 可以存入不同型態的資料
# List 最外層用`[]`包起來
L = [1, 2, 3, 4, 5]
print(L)
# 不同型態混合
L = [1, 2, 3, 4, 5, "hello", ["world", 6]]  # 數字, 字串, List
print(L)

# List 取值
# List 取值方式跟字串一樣, 用`[]`取值
# List 取值方式跟字串一樣, 也可以用`[:]`取值
# List 當中資料的編號(index)以0開始
L = [1, 2, 3, 4, 5]
print(L[0])  # 取得第一個值
print(L[1])  # 取得第二個值
print(L[2])  # 取得第三個值

# List 取值方式跟字串一樣, 也可以用`[:]`取值
# 設定範圍的方式跟range很像, 不包含最後一個數字
print(L[1:4:2])  # 取得第二個到第四個值, 且間隔2
print(L[0:3])  # 取得第一個到第三個值
print(L[:3])  # 取得第一個到第三個值
print(L[3:])  # 取得第四個到最後一個值
print(L[:])  # 取得所有值
