#!/usr/bin/env python3

def print_fibonacci(length):
    fib = []
    if length > 0:
        fib.append(0)
    if length >= 2:
        fib.append(1)
        for i in range (2, length):
            fib.append(fib[-1] + fib[-2])
    print(fib)


    

# length = number of indic