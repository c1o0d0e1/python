# 函式，就像是一個神奇的工具箱，裡面可以放ˋ入我們常常使用的指令


# 建立最基本的函式-函式名稱後面一定要加上小括號()，並且記得加上冒號:
def say_hello():
    print("hello! I am Ming!")
    print("Nice to meet you!")


say_hello()  # 呼叫函式


# 函式可以接收資料(參數) - 參數就像是函式的原料，可以放入不同的值來得到不同的結果
def say_hello_with_name(name):
    print(f"hello! {name}!")
    print("Nice to meet you!")


say_hello_with_name("Hua")


# 函式可以有預設值 - 如果不給參數值，就會使用預設的值，就，就像是媽媽煮飯時準備備用食材
def say_hello_with_name(name="Ming"):
    print(f"hello! {name}!")
    print("Nice to meet you!")


say_hello_with_name()  # 使用預設值
say_hello_with_name("Hei")  # 使用新的值

# 區域變數與全數變數 - 想像一下學校和家裡的玩具
# 全數變數就像是學校的遊樂設施，每個人都可以使用
# 區域變數就像是你書包裡的鉛筆盒，只有你自己可以使用
toy_name = "玩具熊"


def play_with_toy():
    toy_name = "慧魚積木"
    print(f"下這時間我在玩: {toy_name}")


def share_toy():
    global toy_name
    toy_name = "積木"
    print(f"大家一起玩: {toy_name}")
