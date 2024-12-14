d = {}
while True:
    print("1. 新增科目成績")
    print("2. 刪除科目成績")
    print("3. 提交所有成績並顯示平均")
    m = input("請選擇功能編號: ")
    print("=================================")
    if m == "1":
        subject = input("請輸入新增的科目: ")
        try:
            score = int(input("請輸入分數: "))
        except:
            print("輸入錯誤，請重新輸入")
            score = int(input("請輸入分數: "))
            print("=================================")
            d[subject] = score
            for i in d:
                print(f"{i}: {d[i]}")
        else:
            d[subject] = score
            print("=================================")
            for i in d:
                print(f"{i}: {d[i]}")
    elif m == "2":
        subject = input("請輸入想刪除的科目: ")
        try:
            d.pop(subject)
        except:
            print("此科目尚未新增!")
            print("=================================")
            for i in d:
                print(f"{i}: {d[i]}")
        else:
            print("刪除成功!")
            print("=================================")
            for i in d:
                print(f"{i}: {d[i]}")
    elif m == "3":
        for i in d:
            print(f"{i}: {d[i]}")
        total = 0
        for i in d:
            total += d[i]
        print(f"平均成績為{total / len(d)}")
        break
