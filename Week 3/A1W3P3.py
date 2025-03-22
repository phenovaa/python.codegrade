def modular_rectangles(width, height):

    counter = 0

    for a in range(height):
        for b in range(width):
            print(counter, end=" ")
            counter += 1
            if counter > 9:
                counter = 0
        print()

width_input = int(input("width: "))
height_input = int(input("Height: "))
modular_rectangles(width_input, height_input)
