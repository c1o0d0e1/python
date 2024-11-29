# list型態轉換
print(range(10))  # 產生一個range但看不到裡面的數字
print(list(range(10)))  # 將range轉換成list
print(list("hello"))  # 將字串轉換成list

# split
s = "hello world"
L = s.split()  # 將字串以空白分割
print(L)
calendar = "2020/12/25"
L = calendar.split("/")  # 將字串以"/"分割
print(L)

# join
L = ["hello", "world"]
s = " ".join(L)  # 將list以空白合併
print(s)

# append
L = ["hello", "world"]
L.append("Python")  # 加入Python
print(L)

# remove
L = ["hello", "world", "Python"]
L.remove("world")  # 移除world
print(L)

# pop
L = ["hello", "world", "Python"]
S = L.pop(1)  # 移除第一個元素
print(S)

# count
L = ["hello", "world", "Python", "hello"]
print(L.count("hello"))  # hello出現的次數
