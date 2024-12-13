while True:
    d = {}
    print("1. 新增科目成績")
    print("2. 刪除科目成績")
    print("3. 提交所有成績並顯示平均")
    m = input("請選擇功能: ")
    print("=================================")
    subject = input("請輸入科目名稱: ")
    try:
        score = int(input("請輸入成績: "))
    except:
        print("請輸入分數: ")
        continue
    else:
        if m == "1":
            d[subject] = score
            print(d)
