def advanced_palindrome(string):
    string = string.lower()
    string = string.replace(" ", "")
    string = string.replace(",", "")
    string = string.replace(".", "")
    string = string.replace("?", "")
    string = string.replace("!", "")
    string = string.replace(";", "")

    Is_Advanced_Palindrome = True

    for i in range(len(string) // 2):
        if string[i] != string[-i - 1]:
            Is_Advanced_Palindrome = False
    
    if Is_Advanced_Palindrome:
        print(f"{string} is a palindrome")
    else:
        print(f"{string} is not a palindrome")

user_input = input("Sentence: ")
advanced_palindrome(user_input)
