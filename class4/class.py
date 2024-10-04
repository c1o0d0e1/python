# 比較運算子
print(1 == 1)  # True, 1 等於 1
print(1 != 1)  # False, 1 不等於 1
print(1 > 1)  # False, 1 大於 1
print(1 < 1)  # False, 1 小於 1
print(1 >= 1)  # True, 1 大於等於 1
print(1 <= 1)  # True, 1 小於等於 1
print("--------------------")

# 邏輯運算子
# and 代表全部條件鰾成立才會回傳 True
# or 代表只要有一個條件成立會回傳 True
# not 代表將原本的布林值反轉

print(True and True)  # True, True 且 True
print(True and False)  # False, True 且 False
print(False and False)  # False, False 且 True
print(True or True)  # True, True 或 True
print(True or False)  # True, True 或 False
print(False or False)  # False, False 或 True
print(not True)  # False, 非 True
print(not False)  # True, 非 False
print("--------------------")
# if elif else
pwd = input("請輸入密碼: ")
if pwd == "123":
    print("密碼正確")

# if else
pwd == input("請輸入密碼: ")
if pwd == "123456":  # 如果密碼是123
    print("密碼正確")  # 印出密碼正確
else:  # 如果密碼不是123
    print("密碼錯誤")  # 印出密碼錯誤

# if elif else
pwd = input("請輸入密碼: ")
if pwd == "123":
    print("歡迎Ray")
elif pwd == "456":  # 如果密碼是456,
    print("歡迎Tom")  # 印出歡迎Tom
else:
    print("密碼錯誤")

print("--------------------")
# if elif else是連續的判斷，只要有一個條件成立，後面的判斷就不會執行
# if 一定要有，elif可以有多個但是選用，else只能有一個但是選用

print("--------------------")

print("請使用者輸入成積")
score = int(input("請輸入成積: "))
if score >= 101 and score <= -1:
    print("輸入錯誤")
elif score >= 90 and score <= 100:
    print("A")
elif score >= 80 and score <= 89:
    print("B")
elif score >= 70 and score <= 79:
    print("C")
elif score >= 60 and score <= 69:
    print("D")
elif score >= 0 and score <= 59:
    print("E")
