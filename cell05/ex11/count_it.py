#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
    print("none")
else:
    params = sys.argv[1:]
    print(f"{len(params)} parameters:")
    for param in params:
        print(f"{param}: {len(param)}")