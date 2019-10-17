# Counts number of times a word is contained within a list
#   word:  Word to look for
#   words: List of words to search through
def count_words(word, words):
    num = 0
    
    for w in words:
        if word in w:
            num += 1

    return num
