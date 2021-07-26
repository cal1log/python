#!/usr/bin/env python3

for i in range(4):
    for j in range(4):
        print("# ", end="")
    print()

print()

for i in range(5):
    for j in range(i):
        print("# ", end="")
    print()

print()

for i in range(4, 0, -1):
    for j in range(i):
        print("# ", end="")
    print()