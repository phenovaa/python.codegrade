def advanced_palindrome(string):
    string = string.replace(" ", "")
    string = string.replace(",", "")
    string = string.replace(".", "")
    string = string.replace("?", "")
    string = string.replace("!", "")
    string = string.lower()

    is_palindrome = True

    for i in range(0, len(string) // 2):
        if string[i] != string[-i - 1]:
            is_palindrome = False

    if is_palindrome:
        print(f"is a palindrome")
    else:
        print(f"is not a palindrome")

user_input = input("")
advanced_palindrome(user_input)