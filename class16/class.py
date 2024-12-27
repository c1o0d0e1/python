toy_name = "玩具熊"


def play_with_toy():
    toy_name = "慧魚積木"
    print(f"下這時間我在玩: {toy_name}")


def share_toy():
    global toy_name
    toy_name = "積木"
    print(f"大家一起玩: {toy_name}")


# 讓我們來看看玩具的變化
print(f"一開始教室的玩具是{toy_name}")  # 顯示:玩具熊
play_with_toy()  # 下這時間我在玩: 慧魚積木
print(f"下課後的玩具還是{toy_name}")  # 顯示:玩具熊(沒有改變)
print("\n現在讓我們改變大家的玩具")
print(f"教室的玩具是{toy_name}")  # 顯示:玩具熊
share_toy()  # 大家一起玩: 積木
print(f"現在教室的玩具變成{toy_name}")  # 顯示:積木(真的改變了)


# 函式可以回傳資料-就像是我們請人當忙買東西，他會把東西帶回來給我們
# return 是回傳資料關鍵字，代表這個函式處理完後交回甚麼結果
def calculate_sum(number1, number2=0):
    total = number1 + number2
    return total


result = calculate_sum(5, 3)
print(f"Sum of 5 and 3 is: {result}")
result = calculate_sum(10)  # 使用預設0
print(f"Sum of 10 and 0 is: {result}")


# 函式餐數預設值的順序-有預設值的參數一定要放在沒有預設值的參數後面
# 就像是排隊買餐點，一定要先點主餐，才能選擇要不要加購配菜


# 這樣是對的
def order_lunch(main_dish, side_dish="薯條"):
    print(f"主餐是{main_dish}")
    print(f"配菜是{side_dish}")


order_lunch("漢堡")  # 只點主餐
order_lunch("漢堡", "沙拉")  # 主餐和配菜都點

# 這樣是錯的
# def wrong_order(dessert="冰淇淋", meal):
#     print(f"飯是:{meal}")
#     print(f"甜點是:{dessert}")
