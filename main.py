from filter import *

# Driver of Song Filter

def main():
    
    words = ["bad", "sad", "bad", "k"]

    n = check_for_word("bad", words)

    print("%s is printed %d times" % (words[0], n))

main()
