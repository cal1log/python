#!/usr/bin/env python3

'''creating a tuple'''
tup = (10, 20, 30, 40)

'''getting a tuple index value'''
print(tup[2])

'''impossible to change values in a tuple'''
try:
    tup[2] = 60
except:
    print("a tuple can not changes your values")
