#!/usr/bin/python3
value = str(input())
values = value[:140]

def main(values):
    separate_values = values.split()
    no_of_values = len(separate_values)
    total = 0
    for i in separate_values:
        total += eval(i)

    print(total)

if __name__ == "__main__":
    main(values)
