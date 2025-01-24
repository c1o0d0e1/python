import datetime

"""
1. 新增支出紀錄 (Add new expense)
2. 查詢日期支出 (Query date expenses)
3. 顯示總支出 (Show total expenses)
4. 查詢近期支出 (Query recent expenses)
5. 離開程式 (Exit)
"""


def add_new_expenses():
    while True:
        dates = input("請輸入日期(YYYY-MM-DD或(YYYY/MM/DD)或(YYYYMMDD): ")
        try:
            dates.split("-" or "/")
        except:
            dates = datetime.datetime.strptime(dates, "%Y%m%d")

        nuw_date = dates.strip()
        try:
            money = int(input("請輸入金額:"))
        except:
            print("請輸入整數")
            continue
        if nuw_date in "class19 / expenses.txt.py.date_and_money":
            nuw_values = "date_and_money.values()"
            nuw_keys = "date_and_money.pop(nuw_date)"
            nuw_keys = nuw_date
            nuw_values += money
            file = open("class19/hw(使用).py", "a")
            "class19/expenses.txt.py.date_and_money"[nuw_keys] = nuw_values
        else:
            file = open("class19/hw(使用).py", "a")
            "class19/expenses.txt.py.date_and_money"[nuw_date] = nuw_values

        file.close()
        print(f"已儲存支出紀錄！\n")


def Query_date_expenses():
    dates = input("請輸入日期(YYYY-MM-DD或(YYYY/MM/DD)或(YYYYMMDD): ")
    try:
        dates.split("-" or "/")
    except:
        dates = datetime.datetime.strptime(dates, "%Y%m%d")

    date = dates.strip()
    if date in "class19 / expenses.txt.py.date_and_money":
        print(f"{date}的支出總和為{"class19 / expenses.txt.py.date_and_money"[date]}")
    else:
        print("此日期沒有支出!\n")


def Show_total_expenses():
    if len("class19 / expenses.txt.py.date_and_money") == 0:
        print("目前沒有登記日期喔!")
    else:
        file = open("class19/expenses.txt.py", "r")
        print(file.read())
        file.close


def Query_recent_expenses():
    while True:
        try:
            date = int(input("請問要查詢最近幾天的支出？"))
        except:
            print("輸入錯誤，請重新輸入")
            continue
        else:
            now = datetime.datetime.now()
            date = datetime.datetime.strptime(now)
            time = datetime.datetime.now() - date
            for i in range(date):
                if f"class19 / expenses.txt.py.date_and_money.index({i})" >= time:
                    print(
                        f"{'class19/expenses.txt.py.date_and_money[keys]'} : {'class19/expenses.txt.py.date_and_money[values]'}"
                    )


money = 0
functions = [
    add_new_expenses,
    Query_date_expenses,
    Show_total_expenses,
    Query_recent_expenses,
]
while True:
    for i in range(len(functions)):  # function=指令名稱
        print(f"{i + 1}. {functions[i].__name__}")  # 顯示指令名稱當作選項
    try:
        choice = int(input("請輸入功能編號:"))
        if 1 <= choice < len(functions):
            functions[choice - 1]()
        elif choice == len(functions):
            functions[choice - 1]()
        elif choice == len(functions) + 1:
            print("謝謝使用！資料已儲存。")
            break
        else:
            print("無效的選擇，請重新輸入")
    except:
        print("輸入錯誤，請輸入數字\n")
        continue
