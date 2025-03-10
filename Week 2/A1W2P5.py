def dutch_holidays(x):
    x = x.replace(",", " ")

    x1 = x[7:9] #Month
    x2 = x[15:18] #Day

    x1 = int(x1)
    x2 = int(x2)

    if x1 == 12 and x2 == 25:
        print("Christmas")
    elif x1 == 12 and x2 == 5:
        print("Sinterklaas")
    else:
        print("No holiday found on given input")

user_input = input("Date: ")
dutch_holidays(user_input)