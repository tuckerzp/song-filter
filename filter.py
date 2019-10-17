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
    found = []

    for w in lyrics:
        if word in w:
            found.append(w)

    return found

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
        word_list.extend(count_word(b, lyrics))

    return word_list

