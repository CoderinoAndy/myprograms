def scrabble(word):
    total = 0
    for character in word:
        if character in "ALEIOULNSTR":
            total += 1
        elif character in "DG":
            total += 2
        elif character in "BCMP":
            total += 3
        elif character in "FHVWY":
            total += 4
        elif character in "JX":
            total += 8
        elif character in "QZ":
            total += 10
        else:
            total += 5
    return total

def scrabble_game(word_list):
    score_list = []
    for word in word_list:
        score_list.append(scrabble(word))
    return score_list

def sorter_scrabble(word_listy, score_listy):
    switched = True
    while switched:
        switched = False
        for i in range(1, len(score_listy)):
            if score_listy[i] > score_listy[i - 1]:
                word_listy[i - 1], word_listy[i] = word_listy[i], word_listy[i - 1]
                switched = True
    return word_listy

