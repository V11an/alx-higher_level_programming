#!/usr/bin/python3

from calculator_1 import add,sub,mul,div

my_b = ["b=5"]
my_a = ["a=10"]
key_a,a_string = my_a[0].split('=')
key_b,b_string = my_b[0].split('=')
a = 10
b = 5

if __name__ == "__main__":

    print("{a_string} + {b_string} = {}".format(add(a,b)))
    print("{a_string} + {b_string} = {}".format(sub(a,b)))
    print("{a_string} + {b_string} = {}".format(mul(a,b)))
    print("{a_strinf} + {b_string} = {}".format(div(a,b)))
