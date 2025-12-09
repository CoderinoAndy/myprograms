def scrabbler(word_list):
    score_book = {
        "AEIOULNSTR" : 1,
        "DG" : 2,
        "BCMP" : 3,
        "FHVWY" : 4,
        "K" : 5,
        "JX" : 8,
        "QZ": 10
    }
    record = {}
    for word in word_list:
        word = word.upper()
        score = 0
        for letter in word:
            for key, value in score_book.items():
                if letter in key:
                    score += score_book[key]
        record[word.lower()] = score
    return record
            
print(scrabbler(["mike", "john", "armen"]))