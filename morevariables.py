#!/usr/bin/env python3

''' memory position of a variable '''
print('memory id of a variable')
a = 10
print(id(a))
print()

''' a variable taking the value of other variable '''
print('memory id of two variables b = a')
b = a
print('variable a')
print(id(a))
print()
print('variable b')
print(id(b))
print()

''' a variable with the same value of variable a '''
k = 10
print('variable k = 10')
print(id(a))
print()

''' changing value of variable a '''
a = 9
print('variable a = 9')
print(id(a))
print()

''' variable b does not change the id memory '''
print('variable b = a')
print(id(b))
print()

''' changing value of variable k '''
k = a
print('variable k = a')
print(id(k))
print()

''' getting variable type '''
print('using type for getting variable type k')
print(type(k))
print()


