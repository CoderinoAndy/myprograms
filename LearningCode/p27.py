# Create a function or multiple functions that can help to define if two text arguments are anagrams.
# Think about how dicts can help
# Texts that are composed of the same set of characters or symbols

def nagrammam(word1, word2):
    req_table = {}
    for c in word1:
        if c in freq_table:
            freq_table[c] += 1
        else:
            freq_table[c] = 1
    for c in word2:
        if c not in freq_table:
            return False
        else:
            freq_table[c] -= 1
            if freq_table[c] < 0:
                return False
    for key, value in freq_table.items():
        if value != 0:
            return False
    return True