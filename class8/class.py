price = int(input("請輸入商品金額: "))
sum = 0
while price != 0:
    sum += price
    print(f"目前總金額為{sum}")
    price = int(input("請輸入商品金額: "))

num = int(input("請輸入正整數: "))
is_prime = True
for i in range(2, num):
    if num % i == 0:
        is_prime = False
if is_prime and num > 1:
    print(f"正整數{num}是質數")
else:
    print(f"正整數{num}不是質數")
