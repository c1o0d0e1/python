weather = ["晴天", "多雲", "雨天", "晴天", "多雲", "雷震天", "晴天"]
while True:
    for i in range(len(weather)):
        print(f"{i + 1}. {weather[i]}")

    try:
        select = int(input("請輸入要修改的天氣編號: "))
    except:
        print("請輸入數字: ")
        continue
    if select < 1 or select > len(weather):
        print("輸入錯誤查無此星期，請重新輸入")
        continue
    print(f"你要修改的是星期{select}")
    print(f"原本的天氣是{weather[select - 1]}")
    weather[select - 1] = input("請輸入新的天氣: ")
    print(f"修定後的天氣是{weather[select - 1]}")
    more = input("是否更多天氣？(y/n): ")
    if more == "n":
        break
print("程式結束")
