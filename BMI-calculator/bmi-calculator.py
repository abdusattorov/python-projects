def bmi(weight, height):
    res = weight/height**2
    print(bmi)
    return res
    

def main():

    while True:
        
        weight = float(input("Enter your weight\n - "))
        height = float(input("Enter your height\n - "))
        
        if weight or height == '/q':
            break
        else:
            print("Wrong Command!!!")
            print("Restarting...")

    user_bmi = bmi(weight, height)

    if user_bmi < 18.5:

        times = 1
        temp = 0
        while temp >= 18.5:
            temp = bmi(weight+times*0.5, height)
            times += 1

        extra = times * 0.5
            

        print(
            f"Your BMI is {user_bmi}",
            f"which is lower than the average meaning that you are underweight.\nThis is considered unhealthy. You should gain at least {extra} kg\n")

main()