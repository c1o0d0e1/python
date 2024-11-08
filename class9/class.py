# for else
# 如果for迴圈正常結束，則執行else區塊
# 如果for迴圈發生錯誤，則執行else區塊
for i in range(5):
    print(i)
else:
    print("迴圈正常結束")

i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("迴圈正常結束")

print("-------------------")

import time as t

m = int(input("請輸入計時秒數: "))
for i in range(m):
    print(m)
    t.sleep(1)
    m -= 1
else:
    print("時間到")

"""
second = int(input("請輸入計時秒數: "))
while second > 0:
    print(second)
    time.sleep(1)
    second -= 1
else:
    print("時間到")
"""

print("-------------------")

# loop continue
# 可以跳過一次迴圈，繼續執行下一次迴圈
for i in range(5):
    print(i)
    if i == 3:
        continue
    print(i)

i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        continue
    print(i)

j = 1
mm = int(input("請輸入計數: "))
while j <= mm:
    if j % 10 == 0:
        print(f"跳{j}次跳繩")
        j += 1
        continue
    print(j)
    j += 1

print("-------------------")

# loop break
# 可以直接結束迴圈， 但是要注意這個break只會結束所屬的迴圈
for i in range(5):
    for j in range(5):
        if j == 3:
            break
        print(j)
    if i == 3:
        break
    print(i)

i = 0
while i < 5:
    if i == 3:
        break
    print(i)
    i += 1
