# list len
L = [1, 2, 3, 4, 5]
print(len(L))  # 取得List長度, 也就是List當中有幾筆資料
# 務必不要跟index混淆, index是資料的編號, len是資料的數量
# len 可以搭配 for 迴圈使用來取得List當中的所有資料
for i in range(len(L)):
    print(L[i])

for i in L:  # 這邊的i是資料
    print(i)

# 要使用哪一種方式讀取List當中的資料, 要看使用的情境當中會不會需要index
juices_list = [" 蘋果汁", " 柳橙汁", " 葡萄汁", " 可樂", " 系統關閉", " 檸檬汁"]

while True:
    for i in range(len(juices_list)):
        print(f"{i + 1}. {juices_list[i]}")

    try:
        select = int(input("請輸入編號: "))
    except:
        print("請輸入數字: ")
        continue
    if select > len(juices_list):
        print("輸入錯誤，請重新輸入")
        continue
    elif juices_list[select - 1] == "系統關閉":
        print("系統關閉")
        break
    else:
        print(f"你點的商品是{juices_list[select - 1]}")

print("--------------------")

# 跟新List當中的資料
L = [1, 2, 3, 4, 5]
L[0] = 100  # 跟新第一筆資料
print(L)

# List跟字串很像的地方
# 合併清單資料
L1 = [1, 2, 3]
L2 = [4, 5, 6]
L3 = L1 + L2
print(L3)

# 重複清單資料
L = [1, 2, 3]
L = L * 3
print(L)
