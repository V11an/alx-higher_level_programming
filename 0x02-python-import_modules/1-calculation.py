#!/usr/bin/python3

from calculator_1 import add,sub,mul,div

my_b = ["b=5"]
my_a = ["a=10"]
key_a,a_string = my_a[0].split('=')
key_b,b_string = my_b[0].split('=')
a = int(a_string)
b = int(b_string)

if __name__ == "__main__":

    print("{} + {} = {}".format(a,b,add(a,b)))
    print("{} + {} = {}".format(a,b,sub(a,b)))
    print("{} + {} = {}".format(a,b,mul(a,b)))
    print("{} + {} = {}".format(a,b,div(a,b)))
