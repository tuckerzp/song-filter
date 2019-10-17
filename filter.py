# Counts number of times a word is contained within a list
#   word:  Word to look for
#   words: List of words to search through
def check_for_word(word, words):
    num = 0
    
    for w in words:
        if w == word:
            num += 1

    return num
