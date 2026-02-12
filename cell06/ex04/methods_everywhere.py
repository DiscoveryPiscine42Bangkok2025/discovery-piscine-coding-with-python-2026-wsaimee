#!/usr/bin/env python3

import sys

def enlarge(s: str) -> None:
    result = s + "Z" * (8 - len(s))
    print(result)

def shrink(s: str) -> None:
    print(s[:8])

if len(sys.argv) < 2:
    print("none")
else:
    for arg in sys.argv[1:]:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)