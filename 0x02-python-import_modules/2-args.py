#!/usr/bin/python3

argv = input()

def main(argv):

    words = argv.split()
    no_of_words = len(words)

    if no_of_words == 0:
        print(str(no_of_words) + " arguments.")
    elif no_of_words == 1:
        print(str(no_of_words) + " argument:\n" + str(no_of_words) + " : " + argv )
    else:
        print(str(no_of_words) + ": arguments  \n")
        for no in words:
            print(str(words.index(no)+1) + " : " + no)

if __name__ == "__main__":
    main(argv)
