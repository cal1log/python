#!/usr/bin/env python3

x = 10

for i in range(0, x):
    if i % 2 == 0:
        print(i)
    if i % 3 == 0:
        print("this is multiple of 3 but I do not print")
        continue
    if i % 5 == 0:
        print("I am multiple of 5 but I just pass")
        pass

print("bye")