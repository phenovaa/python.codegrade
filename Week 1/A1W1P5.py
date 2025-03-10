four_digit_input = input("Enter four digit numbers: ")

first_digit = four_digit_input[0:1]
second_digit = four_digit_input[1:2]
third_digit = four_digit_input[2:3]
fourth_digit = four_digit_input[3:4]

first_digit_int = int(first_digit)
second_digit_int = int(second_digit)
third_digit_int = int(third_digit)
fourth_digit_int = int(fourth_digit)

result = first_digit_int + second_digit_int + third_digit_int + fourth_digit_int

print(f"{first_digit_int}+{second_digit_int}+{third_digit_int}+{fourth_digit_int}={result}")