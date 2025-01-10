"""
基本型態
print(1) 整數 
print(1.1) 浮點數,只要有小數點就是浮點數
print('hallo') 字串, 用雙引號""或單引號''包起來
print(True) 布林值,第一個字母要大寫
print(None) 空值
"""

"""
a = 1 把1這個整數存到電腦的記憶體中，並且取名為a
# = 的功能是將右邊的資料存到左邊的變數空間當中
print(a) # 把這個變數的質硬出來
"""
"""

d = {}
while True:
    s = input("是否要輸入新手:(請填(是)或(不是))")
    if s == "是":
        n = input("請輸入註冊帳號:")
        while True:
            try:
                nn = int(input("請輸入密碼:"))
            except:
                print("請重新輸入密碼!")
                continue
            else:
                d[n] = nn
            while True:
                nn_nn = int(input("請再一次輸入您的密碼，系統要再次當您確認。"))
                if d[nn] == nn_nn:
                    print(f"歡迎登入: {n}")
                else:
                    nn = input("是否要跟改密碼?(請填(是)或(不是))")
                    if nn == "是":
                        print("請輸入新密碼")
                        nn = int(input("請輸入新密碼:"))
                        d[n] = nn
                    else:
                        continue
"""
name = []
import random

number = 1
while True:
    add_name = input("是否要新增名字?(請填(是)或(不是))")
    if add_name == "是":
        nuw_name = input("請輸入新名字:")
        name.append(nuw_name)
    elif add_name == "不是":
        name_2_0 = []
        while number != len(name):
            s = random.randrange(1, len(name))
            if s in name_2_0:
                continue
            else:
                print(f"{number}. {name[s]}")
                name_2_0.append(s)
                number += 1
        break
    else:
        print("輸入錯誤，請重新輸入")
