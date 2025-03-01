while True:
    score = int(input("Enter the score you have got: "))
    prize = ""

    if score <= 0 or score >= 200:
        print("Enter a valid score...")

    else:
        if score >= 1 and score <= 50:
            prize = "wooden rabbit"

        elif score >= 151 and score <= 180:
            prize = "wafer-thin mint"

        elif score >= 181 and score <= 200:
            prize = "penguin"

        else:
            print("Oh dear,no prize for this time")
            break
    if not prize  == "" :
        print(f"congratulations! you won a {prize}")
        break
    else:
        pass
EXIT = input()

