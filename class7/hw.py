"""
輸入一數字n為尋找的區間範圍, 找出區間範圍
3,7的倍數顯示在螢幕上, 其餘不顯示
hint:可以使用%取餘數進行判斷
EX
請輸入正整數:20
3
6
7
9
12
14
15
18
請輸入要印出的箭頭大小
hint:
可利用字串乘法
>>>val="*" * 3
>>>print(val)
>>>***
EX:
請輸入要印出的箭頭大小:3
  *  
 *** 
*****
  *  
  *  
  * 
"""

n = int(input("請輸入一個正整數: "))
h = 7
i = 1
j = 1
while i < n:
    if i % 3 == 0 and i < h:
        print(i)
        i += 1
    elif i % 3 != 0 and i < h:
        i += 1
    elif i % 3 == 0 and i >= h:
        print(h)
        print(i)
        i += 1
        h += 7
    elif i % 3 != 0 and i >= h:
        i += 1

print("--------------------")

nn = int(input("請輸入要印出的箭頭大小: "))
k = 1
print(((" " * nn) + ("*" * k).center(nn * (nn - k))))
while k < nn:
    print(((" " * nn) + ("*" * (k + (k + 1))).center(nn * (nn - 1))))
    k += 1

l = 1
while l < nn + 1:
    print((" " * (nn - 1) + ("*")).center(nn * (nn)))
    l += 1
