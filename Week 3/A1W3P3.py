def modular_rectangles(width, height):
    width = int(width)
    height = int(height)

    typewriter = 0

    for h in range(height):
        for w in range(width):
            print(typewriter, end=" ")
            if typewriter < 9:
                typewriter += 1
            else:
                typewriter = 0
        print()

width_input = input("width: ")
height_input = input("height: ")
modular_rectangles(width_input, height_input)
