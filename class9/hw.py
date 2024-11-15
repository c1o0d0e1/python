while True:
    print("1. 蘋果汁")
    print("2. 柳橙汁")
    print("3. 葡萄汁")
    print("4. 系統關閉")
    type = input("請輸入編號: ")
    if type == "1":
        print("你點的商品是蘋果汁")
    elif type == "2":
        print("你點的商品是柳橙汁")
    elif type == "3":
        print("你點的商品是葡萄汁")
    elif type == "4":
        print("系統關閉")
        break
    else:
        print("輸入錯誤，請重新輸入")
