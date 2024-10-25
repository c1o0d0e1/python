# 99乘法表
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}")

# while 迴圈
# 這是條件是迴圈, 當條件成立時, 會執行回圈內的程式
i = 1
while i < 10:
    # 當i小於10時, 執行回圈內的程式
    print(i)
    i = i + 1

# 算術指定運算子
# +=, -=, *=, /=, %=, **=, //=
# x = x + 1 等於 x += 1
# x = x - 1 等於 x -= 1
# x = x * 1 等於 x *= 1
# x = x / 1 等於 x /= 1
# x = x % 1 等於 x %= 1
# x = x ** 1 等於 x **= 1
# x = x // 1 等於 x //= 1
i = 1
while i < 10:
    print(i)
    i += 1  # 等於 i = i + 1

user_input = ""
while user_input != "12345":
    user_input = input("請輸入密碼: ")
print("密碼正確")
