order = ["1. 新增餐點", "2. 刪除餐點", "3. 顯示餐點"]
while True:
    print(order)
    try:
        num = int(input("請輸入選擇: "))
    except:
        print("請輸入數字: ")
        continue
    else:
        if menu < 1 or menu > 3:
            print("輸入錯誤查無此選項，請重新輸入")
            continue
        else:
            if menu == 1:
                print("請輸入餐點名稱: ")
                name = input()
                menu.append(name)
            # elif order == 2:
