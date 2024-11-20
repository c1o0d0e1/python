import random

start = 0
end = 100
m = random.randrange(1, 101)
num = int(input("請輸入0~100的整數: "))
while num != m:
    if num < m:
        print("在大一點")
        start = num
        num = int(input(f"請輸入{start}~{end}的整數: "))
    elif num > m:
        print("在小一點")
        end = num
        num = int(input(f"請輸入{start}~{end}的整數: "))

print("恭喜猜中!")
