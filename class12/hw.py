order = ["1. 新增餐點", "2. 刪除餐點", "3. 顯示餐點"]
menu = []
while True:
    print(order)
    try:
        num = int(input("請輸入選擇: "))
    except:
        print("請輸入數字: ")
        continue
    else:
        if num < 1 or num > 3:
            print("輸入錯誤查無此選項，請重新輸入")
            continue
        else:
            if num == 1:
                name = input("請輸入餐點名稱: ")
                menu.append(name)
                print(menu)
            elif num == 2:
                name = input("請輸入要刪除的餐點名稱: ")
                for i in range(menu.count(name)):
                    menu.remove(name)

                print(menu)
            elif num == 3:
                for i in range(len(menu)):
                    if menu.count(name) > 1:
                        for j in range(menu.count(name)):
                            menu.remove(name)
                    else:
                        print(f"{menu[i]}:{menu.count(menu[i])}")
