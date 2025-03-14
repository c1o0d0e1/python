def BMI():
    height = float(input("Enter your height in cm: "))
    weight = float(input("Enter your weight in kg: "))
    bmi = weight / (height / 100) ** 2
    print("Your BMI is: ", bmi)
    if bmi < 18.5:
        print("Underweight")
    elif bmi >= 18.5 and bmi < 24.9:
        print("Normal weight")
    elif bmi >= 25 and bmi < 29.9:
        print("Overweight")
    elif bmi >= 30:
        print("Obesity")


BMI()
