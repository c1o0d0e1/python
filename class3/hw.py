"""
請使用者輸入身高(公尺)h以及體重(公斤)w
透過下面公式計算出BMI數值並顯示計算結果
bmi = w/h**2
"""

h = float(input("請輸入身高(公尺)h: "))
w = float(input("請輸入體重(公斤)w: "))
bmi = w / h**2
print(f"你得bmi為{bmi}")
print("--------------------")
