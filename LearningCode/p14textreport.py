def text_report(s):
    dictionary_report = {}
    dictionary_report["chars"] = len(s)

    letters_counter = 0
    for x in s:
        if x.isalpha():
            letters_counter += 1

    dictionary_report["letters"] = letters_counter

    digit_counter = 0
    for x in s:
        if x.isdigit():
            digit_counter += 1
    dictionary_report["digits"] = digit_counter

    dictionary_report["spaces"] = s.count(" ") + s.count("\n") + s.count("\t")

    vowel_counter = 0
    for x in s:
        if x.lower() in "aeiou":
            vowel_counter += 1
    dictionary_report["vowels"] = vowel_counter

    champ = ""
    champnum = 0
    num = 0
    for x in s:
        num = s.count(x)
        if num > champnum:
            champ = x
            champnum = num
        elif num == champnum and x < champ:
            champ = x
    if champ == "":
        dictionary_report["most_common_char"] = "None"
    else:
        dictionary_report["most_common_char"] = champ

    dictionary_report["longest_word"] = max(words, key=len)

    total = 0
    numberofwords = len(words)
    for x in words:
        total += len(x)
    dictionary_report["avg_word_len"] = round(total/numberofwords, 2)

    return dictionary_report


print(text_report("CS 11! Go!"))