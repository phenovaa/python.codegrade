def dog_years(x):
    dog_years = 0

    if x == 1:
        dog_years += 10.5
        print(dog_years)
    elif x == 2:
        dog_years += 10.5 + 10.5
        print(dog_years)
    elif x == 3:
        dog_years += 10.5 + 10.5
        dog_years += 4
        print(dog_years)
    elif x == 4:
        dog_years += 10.5 + 10.5
        dog_years += 8
        print(dog_years)
    elif x == 5:
        dog_years += 10.5 + 10.5
        dog_years += 12
        print(dog_years)
    elif x < 0:
        print("Only positive numbers are allowed")

user_input = int(input("Enter human years: "))
dog_years(user_input)
