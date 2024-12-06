order = ["1. 新增餐點", "2. 刪除餐點", "3. 顯示餐點"]
while True:
    print(f"目前order有{order}")
    print("1. 新增餐點")
    print("2. 刪除餐點")
    print("3. 顯示餐點")

    choice = input("請選擇功能: ")

    if choice == "1":
        item = input("請輸入餐點名稱: ")
        order.append(item)
    elif choice == "2":
        item = input("請輸入要刪除的餐點名稱: ")
        if item in order:
            for i in range(order.count(item)):
                order.remove(item)
    elif choice == "3":
        items = input("請輸入餐點名稱: ")
        for x in order:
            if x not in items:
                items.append(x)

        for x in items:
            print(f"{x}:{order.count(x)}")

        break

    else:
        print("無效的選擇，請重新輸入!")
