# String Stuff
# Tacocat is a palindrome
# Like doggod
# Like 90609
def palindrome(word):
    return word == word[::-1]

possiblepalindrome = input("Enter possible palindrome: ")
if palindrome(possiblepalindrome):
    print(f"{possiblepalindrome} IS A PALINDROME!")
else:
    print(f"{possiblepalindrome} IS NOT A PALINDROME")