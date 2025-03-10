def chessboard_colors(x):
    x_char = x [0:1]
    x_number = x[1:2]

    x_char = x_char.upper()
    x_number = int(x_number)

    if x_char in "ACEG" and x_number % 2 == 1:
        print("Black")
    elif x_char in "ACEG" and x_number % 2 == 0:
        print("White")
    elif x_char in "BDFH" and x_number % 2 == 1:
        print("White")
    elif x_char in "BDFH" and x_number % 2 == 0:
        print("Black")

user_input = input("Enter a position: ")
chessboard_colors(user_input)