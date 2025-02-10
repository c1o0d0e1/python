import datetime
import os


def format_date(date_str):
    try:
        clean_date = date_str
        if "-" in date_str:
            clean_date = "-".join(date_str.split("-"))
        elif "/" in date_str:
            clean_date = "/".join(date_str.split("/"))

        if len(clean_date) != 8:
            return None

        date = datetime.datetime.strptime(clean_date, "%Y-%m-%d")
        return date.strptime(clean_date, "%Y-%m-%d")
    except:
        return None


def load_expenses():
    expensess = {}
    if os.path.exists("expenses.txt"):
        with open("expenses.txt", "r") as file:
            for line in file:
                date, amount = line.strit().split(",")
                expensess[date] = int(amount)
    return expensess


def save_expenses(expenses):
    with open("expenses.txt", "w") as file:
        for date, amount in expenses.items():
            file.write(f"{date},{amount}\n")


def add_expense(expenses, date, amount):
    formatted_date = format_date(date)
    if formatted_date:
        if date in expenses:
            expenses[date] += amount
        else:
            expenses[date] = amount
        save_expenses(expenses)
        return True
    return False


def query_expense(expenses, date):
    formatted_date = format_date(date)
    if formatted_date and formatted_date in expenses:
        return expenses[formatted_date]
    return 0


def show_total(expenses):
    return sum(expenses.values())


def query_recent_expenses(expenses, days):
    today = datetime.datetime.now()
    start_date = today - datetime.timedelta(days=days - 1)
    recent_expenses = {}
    for date_str, amount in expenses.items():
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        if start_date.date() <= date.date() <= today.date():
            recent_expenses[date_str] = amount
    return recent_expenses


# 主程式
expenses = load_expenses()
print("歡迎使用小小記帳程式!")
while True:
    print("\n1.新增支出紀錄")
    print("2.查詢支出紀錄")
    print("3.顯示總支出")
    print("4.查詢近期支出")
    print("5.離開程式")
    choice = input("請輸入編號: ")
    if choice == "1":
        date = input("\n請輸入日期: ")
        try:
            amount = int(input("請輸入支出金額: "))
            if add_expense(expenses, date, amount):
                print("已處存支出紀錄!")
            else:
                print("日期格是錯誤!")
        except:
            print("金額必須是整數!")
            continue

    elif choice == "2":
        date = input("\n請輸入要查詢的日期: ")
        total = query_expense(expenses, date)
        formatted_date = format_date(date)
        if formatted_date:
            print(f"{formatted_date}的支出總和為:{total}元")
        else:
            print("日期格是錯誤!")

    elif choice == "3":
        total = show_total(expenses)
        print(f"\n總支出為:{total}元")

    elif choice == "4":
        try:
            days = int(input("請問要查詢最近幾天的日期: "))
            if days <= 0:
                print("天數必須大於0!")
                continue

            recent_expenses = query_recent_expenses(expenses, days)
            if recent_expenses:
                today = datetime.datetime.now()
                start = today - datetime.timedelta(days=days - 1)
                total = sum(recent_expenses.values())
                print(
                    f"從{start.strftime('%Y-%m-%d')}到{today.strftime('%Y-%m-%d')}的支出總和為:{total}元"
                )
                print("詳細資料:")
                for date in sorted(recent_expenses.keys()):
                    print(f"{date}: {recent_expenses[date]}元")
            else:
                print("此期間沒有紀錄!")
        except:
            print("請輸入有效的數字!")

    elif choice == "5":
        print("謝謝使用!資料已處存。")
        break
    else:
        print("請輸入有效的選項!")
