#!/usr/bin/python3
if __name__ == "__main__":

    try:
        values = map(int, input().split())
        total = 0
        for i in values:
            total += int(i)

        print(total)
    except EOFError as e:
        print(e)


