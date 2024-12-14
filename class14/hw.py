d = {}
while True:
    print("1. 新增科目成績")
    print("2. 刪除科目成績")
    print("3. 提交所有成績並顯示平均")
    m = input("請選擇功能: ")
    print("=================================")
    if m == "1":
        subject = input("請輸入科目新增的名稱: ")
        try:
            score = int(input("請輸入成績: "))
        except:
            print("輸入錯誤，請重新輸入")
            score = int(input("請輸入分數: "))
            print("=================================")
            continue
        else:
            d[subject] = score
            print(d)
    elif m == "2":
        subject = input("請輸入要刪除的科目名稱: ")
        try:
            d.pop(subject)
        except:
            print("此科目尚未新增!")
            print(d)
        else:
            print(d)
    elif m == "3":
        total = 0
        for i in d:
            total += d[i]
        print(f"平均成績為{total / len(d)}")
        break
