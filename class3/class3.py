# 型態轉變
# int() 轉換成整數
# float() 轉換成浮點數
# str() 轉換成字串
# bool() 轉換成布林值

print(int("123"))  # 123
print(int(123.999999))  # 123
print(int(True))  # 1
print(int(False))  # 0
print("--------------------")

print(float("123.456"))  # 123.456
print(float(123))  # 123.0
print(float(True))  # 1.0
print(float(False))  # 0.0
print("--------------------")

print(str(123))  # '123'
print(str(123.456))  # '123.456'
print(str(True))  # 'True'
print(str(False))  # 'False'
print("--------------------")

print(bool(123))  # True
print(bool(0))  # False
print(bool("-1"))  # True
print(bool(""))  # False
print("0")  # True
print("--------------------")

# input() 讓使用者在終端機輸入資料
# input() 的括弧內可以放入"提示文字"
a = input("請輸入數字: ")
# 透過 input() 輸入的資料都是字串
print(a + "1")  # 字串相加
print(int(a) + 1)  # 將字串轉換成整數後相加
print("--------------------")

# 格式化字串 f-string

# try except 錯誤處理
try:  # 嘗試執行可能會出錯的程式碼
    n = int(input("input a number: "))

except:  # 如有錯誤發生則會執行
    print("you should input a number")

else:  # 如果沒有錯誤發生則會執行
    print(n + 1)
