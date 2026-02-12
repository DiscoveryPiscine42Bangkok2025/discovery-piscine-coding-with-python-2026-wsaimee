#!/usr/bin/env python3

def add_one(number):
    number = number + 1
    print("Inside function:", number)

value = 9

print("Before function:", value)

add_one(value)

print("After function:", value)