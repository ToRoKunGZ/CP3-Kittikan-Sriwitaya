retrytoken = 0
while retrytoken != "no":
    print("------------------------------------------------")
    x1 = float(input("Enter your first number: "))
    x2 = float(input("Enter your second number: "))
    oper = input("Select your operator (+ , - , * , / ): ")
    if oper == "+":
        print("Your answer: ", x1 + x2)
        retrytoken = input("Do you want to do another calculation?(yes or no)>>")
    elif oper == "-":
        print("Your answer: ", x1 - x2)
        retrytoken = input("Do you want to do another calculation?(yes or no)>>")
    elif oper == "*":
        print("Your answer: ", x1 * x2)
        retrytoken = input("Do you want to do another calculation?(yes or no)>>")
    elif oper == "/":
        print("Your answer: ", x1 / x2)
        retrytoken = input("Do you want to do another calculation?(yes or no)>>")
    else:
        print("Your input is wrong.")
if retrytoken == "no":
    print("------------------------------------------------")
    print("Thank you for using our calculator.")