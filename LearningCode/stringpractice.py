# String practice
# Cleaning

def clean(text):
    result = ""
    i = 0
    # Avoid index since it is a function
    while i < len(text):
        if text[i].isalpha():
        #Is alpha verifies if a text is alphabetic and returns a booollolllllolololololololollllean value
            result += text[i]
        i += 1
    return result.lower()

def charfinder(X, T):
    if not X: # If len of text == 0 basically but much faster hahahahaha
        return -1
    i = 0
    while i < len(X):
        if X[i] == T:
            return i
        i += 1
    return -1
    # Linear algorithiricimrimineijneijeiroej;aokdl sorryoooo
    # This FUNC. is basically s.find() but probably worse in some way or fashion hehehehehe
    # A LINEAR ALGORITHM IS A SEARCHING ALGORITHM
word = input("whatever word: ")
charToFind = input("whatever char to find: ")

print(f"{clean(word)} clean version")

print(f"{charfinder(word, charToFind)} is the location of {charToFind} in {word}")

