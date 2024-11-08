"""
輸入一組整數範圍，將範圍中的所有質數顯示於畫面上。
EX：
請輸入開始整數:10
請輸入結束整數:50
11
13
17
19
23
29
31
37
41
43
47
"""

"""
i = 1
j = 1
num = int(input("請輸入開始整數: "))
end = int(input("請輸入結束整數: "))


while num <= end:
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
        num += 1
    else:
        print(num)
        num += 1
"""
'''
num = int(input("請輸入開始整數: "))
end = int(input("請輸入結束整數: "))
while num <= end:
    is_prime = True
    for i in range(2, num):
        if is_prime and num > 1:
            is_prime = False
            i += 1
            """
        elif num % i != 0:
            is_prime = True
            print(num)
            num += 1
"""
'''

start = int(input("請輸入開始整數: "))
end = int(input("請輸入結束整數: "))
is_prime = True
for num in range(start, end + 1):
    is_prime = True
    for i in range(2, num):
        if start % i == 0:
            is_prime = False

    if is_prime and num > 1:
        print(f"正整數{num}是質數")
    else:
        print(f"正整數{num}不是質數")
