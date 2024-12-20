score_dict = {}
while True:
    for d, score in score_dict.items():
        print(f"{subject}: {score}")
    print("1. 新增科目成績")
    print("2. 刪除科目成績")
    print("3. 提交所有成績並顯示平均")
    choice = input("請選擇功能編號: ")
    print("=================================")
    if choice == "1":

        subject = input("請輸入新增的科目: ")
        if subject in score_dict:
            print("此科目已經新增過了!")
        else:
            while True:
                try:
                    score = int(input("請輸入分數: "))
                    score_dict[subject] = score
                    break
                except:
                    print("輸入錯誤，請重新輸入")

    elif choice == "2":
        subject = input("請輸入想刪除的科目: ")
        if subject in score_dict:
            score_dict.pop(subject)
            print("刪除成功!")
        else:
            print("此科目尚未新增!")

    elif choice == "3":
        if len(score_dict) == 0:
            print("目前沒有登記成績!")
        else:
            for subject, score in score_dict.items():
                print(f"{subject}: {score}")
            print(f"總平均為{sum(score_dict.values()) / len(score_dict)}")
        break
    else:
        print("查無此功能，請重新輸入")
