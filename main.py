from filter import *

# Driver of Song Filter

def main():
    
    words = ["bad", "sad", "bad", "k", "baddy"]

    n = count_words("bad", words)

    print("%s is printed %d times" % (words[0], n))

main()
