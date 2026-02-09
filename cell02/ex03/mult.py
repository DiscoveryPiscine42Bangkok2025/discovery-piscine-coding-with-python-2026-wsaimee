#!/usr/bin/env python3

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

result = a * b

print(f"{a} x {b} = {result}")

if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")
