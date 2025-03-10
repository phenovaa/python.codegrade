def sides_to_shape(x):
    if x == 3:
        return "triangle"
    elif x == 4:
        return "Square"
    elif x == 5:
        return "pentagon"
    elif x == 6:
        return "hexagon"
    elif x == 7:
        return "heptagon"
    elif x == 8:
        return "octagon"
    elif x == 9:
        return "nonagon"
    elif x == 10:
        return "decagon"
    else:
        return "Amount of sides is out of range"
        
user_input = int(input("Enter amount of sides: "))
print(sides_to_shape(user_input))

