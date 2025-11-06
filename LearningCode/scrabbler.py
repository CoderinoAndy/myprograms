def scrabble(word):
    total = 0
    for letter in word:
        if letter in "sample_string":
            total += 1
        elif letter in "sample_string2":
            total += 2
        #etc.
    return total
def scorer(words):
    score_list = []
    for word in words:
        score_list.append(scrabble(word))
    return score_list
def listlistsort(words, scores):
    switched = True
    while switched:
        switched = False:
            if scores[i - 1] < scores[i]:
                words[i - 1], words[i] = words[i], words[i - 1]
                scores[i - 1], score[i] = scores[i], scores[i - 1]
                switched = True
    return words
