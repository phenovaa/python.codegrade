def modular_rectangles(w, h):
    w = int(w)
    h = int(h)

    counter = 0

    for a in range(h):
        for b in range(w):
            print(counter, end=" ")
            counter += 1
            if counter > 9:
                counter = 0
        print()

width_input = input("width: ")
height_input = input("height: ")
modular_rectangles(width_input, height_input)
