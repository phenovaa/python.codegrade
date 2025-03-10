def leap_year(x):
    if x % 400 == 0:
        return "Leap year"
    elif x % 100 == 0:
        return "Not a Leap year"
    elif x % 4 == 0:
        return "Leap year"
    else:
        return "Not a Leap year"

user_input = int(input("Enter a year: "))
print(leap_year(user_input))