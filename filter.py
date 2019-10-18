import lyricsgenius
import re

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

def grab_genius(author, song, genius):
    """
    Grabs the lyrics from genius of a given song

    Parameters
    ----------
    author : String
        Name of the author
    song   : String
        Name of the song
    genius : Genius
        Genius access to API

    Returns
    -------
    String
        The lyrics of a song
    """
    # Search Genius for song
    song = genius.search_song(song, author)

    return song.lyrics

def open_genius():
    """
    Opens the Genius API

    Returns
    -------
    Genius API
        Access to Genius API
    """
    # Get client_access_token
    with open('key.txt', 'r') as myfile:
        key = myfile.read().split('\n') 

    # Use Key to interact with Genius API
    genius = lyricsgenius.Genius(key[0])
    genius.verbose = False

    return genius

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
        # Print word found without special characters
        print(re.sub(r'[^\w.]', '', w))
