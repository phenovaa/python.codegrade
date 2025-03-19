def simple_palindrome(string):
    string = string.lower()
    string = string.replace(",", "")
    string = string.replace(".", "")
    string = string.replace("?", "")
    string = string.replace(";", "")
    
    first_string_half = string[0:len(string) // 2]
    second_string_half = string[len(string) // 2:]
    palindrome = True

    for i in range(0,len(string) // 2):
        if first_string_half[i] == second_string_half[-i - 1]:
            palindrome = True
        else:
            palindrome = False
            break
    
    if palindrome == True:
        print(f"{string} is a palindrome")
    elif palindrome == False:
        print(f"{string} is not a palindrome")

user_input = input("")
simple_palindrome(user_input)