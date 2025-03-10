def oddandeven(x):
    if x % 2 == 0:
        return "Even"
    elif x % 2 == 1:
        return "Odd"

user_input = int(input("Enter:"))
print(oddandeven(user_input))