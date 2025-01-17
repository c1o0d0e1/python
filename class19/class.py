# 附加檔案 - 使用 open() 函式
# 例如:
file = open("class18/file_test.py", "a")
file.write("print('hello world')")
file.close()

# 附加檔案 - 使用 with open() as
# 例如:
with open("class18/file_test.py", "a") as file:
    file.write("\nprint('hello python')")

# replace - 取代字串中的特定字串
# 例如:
text = "hello world"
new_text = text.replace("world", "python")
print(new_text)  # hello python

# strip - 去除字串中的空白
# 例如:
text = "   hello world   "
new_text = text.strip()
print(new_text)

# split - 依照特定字元分割字串
# 例如:
text = "hello,world,python"
words = text.split(",")
print(words)

# zfill - 字串補零
# 例如:
number = "7"
nuw_number = number.zfill(2)
print(nuw_number)


# datetime 模組
# datetime 模組提供了處理日期和時間的類別和函式
import datetime

# 取得當前日期和時間 - 使用 datetime.datetime.nuw_now() 函式
# 例如:
now = datetime.datetime.now()
print(now)

# 字串轉成日期 - 使用 datetime.datetime.strptime() 函式
# 例如:
date = datetime.datetime.strptime("2021-01-01", "%Y-%m-%d")
print(date)

# 有哪一些格式化字串可以使用？
# (What formatting strings can be used?)
# %Y - 年份（四位數）
# (Year (four digits))
# %m - 月份（兩位數）
# (Month (two digits))
# %d - 日期（兩位數）
# (Day (two digits))
# %H - 小時（24小時制，兩位數）
# (Hour (24-hour clock, two digits))
# %M - 分鐘（兩位數）
# (Minute (two digits))
# %S - 秒（兩位數）
# (Second (two digits))
# 例如：(For example:)
# %A - 星期幾的全名
# (Full name of the day of the week)
# %B - 月份的全名
# (Full name of the month)
# %c - 日期和時間的字串表示
# (String representation of date and time)
# %p - AM 或 PM
# (AM or PM)

# 日期轉換成字串 - 使用 datetime.datetime.strftime() 函式
# 例如:
date = datetime.datetime.now()
date_str = date.strftime("%Y-%m-%d")
print(date_str)

# 計算距離目標日期還有多少天
# 例如:
target_date = datetime.datetime.strptime("2021-01-01", "%Y-%m-%d")
now = datetime.datetime.now()
days_left = (target_date - now).days
print(days_left)
