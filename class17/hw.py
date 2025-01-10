"""
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
"""


# 新增支出紀錄的函式
# Function to add a new expense record
def add_expense(records, date, amount):
    # 檢查日期是否已經存在於紀錄中
    # Check if the date already exists in records
    if date in records:
        # 如果日期存在，就把新金額加到現有金額上
        # If date exists, add new amount to existing amount
        records[date] += amount
    else:
        # 如果是新的日期，就建立新的紀錄
        # If it's a new date, create a new record
        records[date] = amount


# 查詢特定日期支出的函式
# Function to query expenses for a specific date
def query_expense(records, date):
    # 檢查要查詢的日期是否存在
    # Check if the date exists in records
    if date in records:
        # 如果日期存在，回傳該日期的支出金額
        # If date exists, return the expense amount
        return records[date]
    else:
        # 如果日期不存在，回傳0元
        # If date doesn't exist, return 0
        return 0


# 計算所有支出總和的函式
# Function to calculate total of all expenses
def show_total(records):
    # 把所有日期的支出加起來
    # Add up all expenses from all dates
    return sum(records.values())


# 建立一個空的字典來儲存所有支出紀錄
# Create an empty dictionary to store all expense records
records = {}

# 主程式迴圈，會一直執行直到使用者選擇退出
# Main program loop, continues until user chooses to exit
while True:
    # 顯示功能選單
    # Display menu options
    print("1. Add new expense record")
    print("2. Query expenses for a specific date")
    print("3. Show total of all records")
    print("4. Exit system")
    function_number = input("Please enter function number:")

    # 根據使用者的選擇執行不同功能
    # Execute different functions based on user's choice
    if function_number == "1":
        # 選項1：新增支出紀錄
        # Option 1: Add new expense record
        date = input("Please enter date (YYYY-MM-DD):")
        amount = int(input("Please enter amount:"))
        add_expense(records, date, amount)
    elif function_number == "2":
        # 選項2：查詢特定日期的支出
        # Option 2: Query expenses for a specific date
        date = input("Please enter date (YYYY-MM-DD):")
        total = query_expense(records, date)
        print(f"Total expenses for {date} is {total}")
    elif function_number == "3":
        # 選項3：顯示所有支出總和
        # Option 3: Show total of all expenses
        total = show_total(records)
        print(f"Total of all records is {total}")
    elif function_number == "4":
        # 選項4：離開系統
        # Option 4: Exit system
        break
    else:
        # 如果輸入無效的選項號碼
        # If invalid option number is entered
        print("Invalid function number. Please try again.")
