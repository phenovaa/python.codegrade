def license_plate(x):

    x = x.replace("-", "")
    # xx-xx-xx pattern
    x_patterns_1 = x[0:2]
    x_patterns_2 = x[2:4]
    x_patterns_3 = x[4:15]

    # xx-xxx-x pattern
    x_patterns_4 = x[0:2]
    x_patterns_5 = x[2:5]
    x_patterns_6 = x[5:15]

    # x-xxx-xx pattern
    x_patterns_7 = x[0:1]
    x_patterns_8 = x[1:4]
    x_patterns_9 = x[4:15]

    # xxx-xx-x pattern
    x_patterns_10 = x[0:3]
    x_patterns_11 = x[3:5]
    x_patterns_12 = x[5:15]

    # x-xx-xxx pattern
    x_patterns_13 = x[0:1]
    x_patterns_14 = x[1:3]
    x_patterns_15 = x[3:15]


    if len(x_patterns_1) == 2 and len(x_patterns_2) == 2 and len(x_patterns_3) == 2 and x_patterns_1.isalpha() and x_patterns_2.isdigit() and x_patterns_3.isdigit():
        print("Valid")
    elif len(x_patterns_1) == 2 and len(x_patterns_2) == 2 and len(x_patterns_3) == 2 and x_patterns_1.isdigit() and x_patterns_2.isalpha() and x_patterns_3.isdigit():
        print("Valid")
    elif len(x_patterns_1) == 2 and len(x_patterns_2) == 2 and len(x_patterns_3) == 2 and x_patterns_1.isalpha() and x_patterns_2.isdigit() and x_patterns_3.isalpha():
        print("Valid")
    elif len(x_patterns_1) == 2 and len(x_patterns_2) == 2 and len(x_patterns_3) == 2 and x_patterns_1.isalpha() and x_patterns_2.isalpha() and x_patterns_3.isdigit():
        print("Valid")
    elif len(x_patterns_1) == 2 and len(x_patterns_2) == 2 and len(x_patterns_3) == 2 and x_patterns_1.isdigit() and x_patterns_2.isalpha() and x_patterns_3.isalpha():
        print("Valid")
    elif len(x_patterns_4) == 2 and len(x_patterns_5) == 3 and len(x_patterns_6) == 1 and x_patterns_4.isdigit() and x_patterns_5.isalpha() and x_patterns_6.isdigit():
        print("Valid")
    elif len(x_patterns_7) == 1 and len(x_patterns_8) == 3 and len(x_patterns_9) == 2 and x_patterns_7.isdigit() and x_patterns_8.isalpha() and x_patterns_9.isdigit():
        print("Valid")
    elif len(x_patterns_4) == 2 and len(x_patterns_5) == 3 and len(x_patterns_6) == 1 and x_patterns_4.isalpha() and x_patterns_5.isdigit() and x_patterns_6.isalpha():
        print("Valid")
    elif len(x_patterns_7) == 1 and len(x_patterns_8) == 3 and len(x_patterns_9) == 2 and x_patterns_7.isalpha() and x_patterns_8.isdigit() and x_patterns_9.isalpha():
        print("Valid")
    elif len(x_patterns_10) == 3 and len(x_patterns_11) == 2 and len(x_patterns_12) == 1 and x_patterns_10.isalpha() and x_patterns_11.isdigit() and x_patterns_12.isalpha():
        print("Valid")
    elif len(x_patterns_13) == 1 and len(x_patterns_14) == 2 and len(x_patterns_15) == 3 and x_patterns_13.isdigit() and x_patterns_14.isalpha() and x_patterns_15.isdigit():
        print("Valid")
    else:
        print("Invalid")
    
user_input = input("License: ")
license_plate(user_input)
