user_word = input("Enter a word: ")

def paldrm(string): 
    string = "".join(reversed(string)) 
    return string

if paldrm(user_word) == user_word:
    print("Word is a palindrome")
else:
    print("Word is not a palindrome")