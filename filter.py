def count_word(word, lyrics):
    """
    Counts number of times a word is contained within a list

    Paramaters
    ----------
    word   : String
        Word to look for
    lyrics : String[]
        List of words to search through
    """
    num = 0

    for w in lyrics:
        if word in w:
            num += 1

    return num

def list_words(blacklist, lyrics):
    """
    Add all occurrences of blacklisted words found in a list

    Parameters
    ----------
    blacklist : String[]
        Blacklisted words to check against
    words     : String[]
        List of words to search through
    """
    word_list = []

    for b in blacklist:

        n = count_word(b, lyrics)

        for i in range(n):
            word_list.append(b)

    return word_list
