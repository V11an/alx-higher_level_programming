#!/usr/bin/python3
if __name__ == "__main__":

    try:
        values = input()
        separate_values = values.split()
        total = 0
        for i in separate_values:
            total += int(i)

        print(total)
    except EOFError as e:
        print(e)


