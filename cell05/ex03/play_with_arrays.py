#!/usr/bin/env python3

original = [2, 8, 9, 48, 8, 22, -12, 2]

new_array = []

for number in original:
    if number > 5:
        value = number + 2
        if value not in new_array:
            new_array.append(value)

print(original)
print(new_array)