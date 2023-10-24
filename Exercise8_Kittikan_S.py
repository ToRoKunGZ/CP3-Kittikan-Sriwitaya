usernameInput = input("Enter your username: ")
passwordInput = input("Enter your password: ")
if usernameInput == "admin" and passwordInput == "1234":
    print("Done.")
    print("Welcome to Gamer Center.")
    print("----------------------------")
    print("Select one of our service below")
    print("1.Buy Game Console (PS5,PS4,Nintendo Switch)")
    print("2.Buy Digital Game for Console")
    print("3.Contact our Operator")
    print("----------------------------")
    userselect = input(">>")
    if userselect == "1" or userselect == "Buy Game Console":
        consoleselect = input("Select your console(PS5, PS4, Nintendo Switch): ")
        if consoleselect == "PS5":
            ps5num = int(input("How many PS5 you want to buy? (cost 16900 THB each):"))
            totalcost1 = ps5num*16900
            print("----------------------------")
            print("Total cost is",totalcost1,"THB")
        elif consoleselect == "PS4":
            ps4num = int(input("How many PS4 you want to buy? (cost 8900 THB each):"))
            totalcost1 = ps4num * 8900
            print("----------------------------")
            print("Total cost is", totalcost1, "THB")
        elif consoleselect == "Nintendo Switch":
            nsnum = int(input("Hpw many Nintendo Switch you to buy? (cost 10900 THB each):"))
            totalcost1 = nsnum * 10900
            print("----------------------------")
            print("Total cost is", totalcost1, "THB")
        else:
            print("Your input is wrong!")
    elif userselect == "2" or userselect == "Buy Digital Game":
        digitalgamenum = int(input("How many game you want to buy? (cost 1990 THB each):"))
        totalcost2 = digitalgamenum*1990
        print("----------------------------")
        print("Total game cost is",totalcost2, "THB")
    elif userselect == "3" or userselect == "Contact our Operator":
        print("OK, we will contact you after our operator is availible.")
    else:
        print("Your input is wrong!")

