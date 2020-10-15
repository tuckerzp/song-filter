from filter import *
import sys
import lyricsgenius

# Driver of Song Filter


def main():

    
    # Open genius api
    genius = open_genius()

    with open(sys.argv[1]) as file:

        for line in file:
            t = line.split("---")
            author = t[0].strip()
            song = t[1].strip()

            # Check both a song and author provided
            if (song == "" or author == ""):
                print("No song or author inputed")
                return -1

            lyrics = grab_genius(author, song, genius)

            # grabing lyrics failed
            if (lyrics == -1):
                print("Getting song failed... exiting")
                return -1

            blacklist = get_blacklist()

            word_list = list_words(blacklist, lyrics)

            output_song_info(author, song, word_list)
    
    return 0


main()

# # Get client_access_token
# with open('key.txt', 'r') as myfile:
#     key = myfile.read().split('\n')

# # Use Key to interact with Genius API
# genius = lyricsgenius.Genius(key[0])
# genius.verbose = False

# print(genius.search_song("Begin Again", "Andy Shauf"))
