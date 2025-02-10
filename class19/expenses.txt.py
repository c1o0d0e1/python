date_and_money = {}
import random

num = 0
open = []
number = []
for i in range(1, 11):
    number.append(num)
    num += 1
number.append("----------")
for j in range(1, 5):
    number2_0 = random.randrange(0, 9)
    number.append(number2_0)
str2_0 = print(number[11:])
for l in range(1, 5):
    str = input(f"請輸入驗證碼(第{l}個數字): ")
    int(str)
    open.append(str)
for m in range(1, 12):
    number.pop()
if open[:] == str2_0[:]:
    print("歡迎登入!")
else:
    print("驗證碼錯誤!")
