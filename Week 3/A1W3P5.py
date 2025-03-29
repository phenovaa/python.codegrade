def multiplication_table():

    print("  1 2 3 4 5 6 7 8 9 10")

    for a in range(1, 11):
        print(a, end=" ")
        for b in range(1, 11):
            print(a * b, end=" ")
        print()

multiplication_table()