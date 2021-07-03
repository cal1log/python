#!/usr/bin/env python3

''' user input '''
x = input('type your name\n')
y = input('type your lastname\n')
print('my complete name is {} {}'.format(x, y))

''' inputing numbers for operations '''
x = int(input('type a number\n'))
y = int(input('type other number\n'))
z = x + y
print('the sum of {} and {} is {}'.format(x, y, z))

''' choosing one character '''
x = input('type a char')[0]
print(x)

''' evaluating the input '''
x = eval(input('type 2 + 6 * 2\n'))
print(x)