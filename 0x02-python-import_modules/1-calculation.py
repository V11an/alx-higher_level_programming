#!/usr/bin/python3

a = 10
b = 5

def add(a, b):
    return (a + b)
def sub(a, b):
    return(a - b)
def mul(a, b):
    return(a * b)
def div(a, b):
    return(a/b)
print("a + b = " + str(add(a, b)) + "\n" 
        "a - b = " + str(sub(a, b)) + "\n"
        "a * b = " + str(mul(a, b)) + "\n"
        "a / b = " + str(div(a, b)) + "\n")
