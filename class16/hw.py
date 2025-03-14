"""
score_dict = {}


def show_score():
    for d, score in score_dict.items():
        print(f"{d}: {score}")
    print("1. 新增科目成績")
    print("2. 刪除科目成績")
    print("3. 提交所有成績並顯示平均(會刪除所有成績)")


def add_score():
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


def delete_score():
    subject = input("請輸入想刪除的科目: ")
    if subject in score_dict:
        score_dict.pop(subject)
        print("刪除成功!")
    else:
        print("此科目尚未新增!")


def show_average():
    if len(score_dict) == 0:
        print("目前沒有登記成績!")
    else:
        for subject, score in score_dict.items():
            print(f"{subject}: {score}")
        print(f"總平均為{sum(score_dict.values()) / len(score_dict)}")


while True:
    show_score()
    choice = input("請選擇功能編號: ")
    print("=================================")
    if choice == "1":
        add_score()
    elif choice == "2":
        delete_score()
    elif choice == "3":
        show_average()
        break
    else:
        print("查無此功能，請重新輸入")

"""


def add():
    global score_dict
    subject = input("請輸入想新增的科目:")
    if subject in score_dict:
        print("此科目已經新增過囉!")
    else:
        while True:
            try:
                score = int(input("請輸入分數:"))
                score_dict[subject] = score
                break
            except:
                print("輸入錯誤，請重新輸入")


def delete():
    global score_dict
    subject = input("請輸入想刪除的科目:")
    if subject in score_dict:
        score_dict.pop(subject)
        print("刪除成功!")
    else:
        print("此科目尚未新增!")


def exit():
    global score_dict
    if len(score_dict) == 0:
        print("目前沒有登記成績喔!")
    else:
        for subject, score in score_dict.items():
            print(f"{subject}:{score}")
        print(f"總平均為:{sum(score_dict.values())/len(score_dict)}")


def edit():
    global score_dict
    subject = input("請輸入想修改的科目:")
    if subject in score_dict:
        while True:
            try:
                score = int(input("請輸入新的分數:"))
                score_dict[subject] = score
                break
            except:
                print("輸入錯誤，請重新輸入")
    else:
        print("此科目尚未新增!")


score_dict = {}
functions = [add, delete, edit, exit]
while True:
    for subject, score in score_dict.items():
        print(f"{subject}:{score}")
    for i in range(len(functions)):  # function=指令名稱
        print(f"{i + 1}. {functions[i].__name__}")  # 顯示指令名稱當作選項
    try:
        choice = int(input("請輸入功能編號:"))
        print("==========================")
        if 1 <= choice < len(functions):
            functions[choice - 1]()  # add() or delete()
        elif choice == len(functions):
            functions[choice - 1]()  # exit()
            break
        else:
            print("無效的選擇，請重新輸入")
    except:
        print("輸入錯誤，請輸入數字")
    print("==========================")
