i = 1
while i < 5:
    juice = int(input("請輸入果汁編號: "))
    if juice == 1:
        print("您點的商品式蘋果汁")
    elif juice == 2:
        print("您點的商品式柳橙汁")
    elif juice == 3:
        print("您點的商品式葡萄汁")

    try:
        juice = int(input("請輸入果汁編號: "))
    except:
        print("輸入錯誤查無此果汁，請重新輸入")
    else:
        print("~~系統關閉~~")
        i = 5
