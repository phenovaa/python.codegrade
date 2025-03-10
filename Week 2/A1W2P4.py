def triangle_type(x):
    x1 = x[2:3] 
    x2 = x[7:8]
    x3 = x[12:13]
    
    int_x1 = int(x1)
    int_x2 = int(x2)
    int_x3 = int(x3)

    if int_x1 == int_x2 and int_x2 == int_x3 and int_x3 == int_x1:
        print("equilateral")
    elif int_x1 == int_x2 or int_x2 == int_x3 or int_x3 == int_x1:
        print("Isosceles")
    else:
        print("Scalene")

user_input = input("Sides: ")
triangle_type(user_input)