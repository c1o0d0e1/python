def add_ne_expense_records():
    date = input("請輸入日期:")
    while True:
        try:
            money = int(input("請輸入金額:"))
            if date in date_and_money:
                date_and_money[date] += money
                break
            else:
                date_and_money[date] = money
                break
        except:
            print("輸入錯誤，請重新輸入")


def Query_total_expenses_for_a_specific_subject():
    date = input("請輸入日期:")
    if date in date_and_money:
        print(f"{date}的支出總和為{date_and_money[date]}")
    else:
        print("此日期沒有支出!")


def Show_sum_of_all_records():
    if len(date_and_money) == 0:
        print("目前沒有登記日期喔!")
    else:
        print(f"所有紀錄的總和為{sum(date_and_money.values())}")


def Exit_system():
    global date_and_money


date_and_money = {}
money = 0
functions = [
    add_ne_expense_records,
    Query_total_expenses_for_a_specific_subject,
    Show_sum_of_all_records,
    Exit_system,
]
while True:
    for i in range(len(functions)):  # function=指令名稱
        print(f"{i + 1}. {functions[i].__name__}")  # 顯示指令名稱當作選項
    try:
        choice = int(input("請輸入功能編號:"))
        if 1 <= choice < len(functions):
            functions[
                choice - 1
            ]()  # add_ne_expense_records() or Query_total_expenses_for_a_specific_subject() or Show_sum_of_all_records()
        elif choice == len(functions):
            functions[choice - 1]()  # Exit_system()
            break
        else:
            print("無效的選擇，請重新輸入")
    except:
        print("輸入錯誤，請輸入數字")
