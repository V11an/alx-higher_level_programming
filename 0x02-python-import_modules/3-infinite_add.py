#!/usr/bin/python3

import sys

values = sys.argv[1:]
def main(values):

    total = 0
    for i in values:
        total += eval(i)

    print(total)

if __name__ == "__main__":

    main(values)
