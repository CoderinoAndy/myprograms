# Creating a function or multiple functions that can help to deine if two text arguments are anagrams
def is_anagram(w1, w2):
    charsineach = []
    uniquechars = []
    w1 = w1.replace(" ", "")
    w2 = w2.replace(" ", "")
    for char in w1:
        charsineach.append(char)
    for char in w2:
        charsineach.append(char)
    for char in charsineach:
        if char not in uniquechars:
            uniquechars.append(char)
    for x in uniquechars:
        if x not in w1 or x not in w2 and w1.count(x) != w2.count(x):
            return False
    return True

word1 = input("w1: ")
word2 = input("w2: ")
if is_anagram(word1, word2):
    print(f"{word1} and {word2} are anagrams")
else:
    print(f"{word1} and {word2} are not anagrams")

