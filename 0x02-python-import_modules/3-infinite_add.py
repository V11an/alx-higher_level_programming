#!/usr/bin/python3
values = input()

def main(values):
    separate_values = values.split()
    total = 0
    for i in separate_values:
        total += int(i)

    print(total)

if __name__ == "__main__":
    main(values)
