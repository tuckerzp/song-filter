def get_occurrences(word, lyrics):
    """
    Counts number of times a word is contained within a list

    Paramaters
    ----------
    word   : String
        Word to look for
    lyrics : String[]
        List of words to search through

    Returns
    -------
    String[]
        List of all matching words from the lyrics
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

    Returns
    -------
    String[]
        List of all words from the lyrics that match a word in the blacklist
    """
    word_list = []

    for b in blacklist:
        word_list.extend(get_occurrences(b, lyrics))

    return word_list

def output_song_info(author, song, word_list):
    """
    Prints out a information on a given song

    Parameterts
    -----------
    author    : String
        Name of the author
    song      : String
        Name of the song 
    word_list : String[]
        List of all words from the lyrics that match a word in the blacklist
    """
    
    print("%s's song: %s had %d blacklisted words" % (author, song,
            len(word_list))) 
    
    for w in word_list:
        print(w)
