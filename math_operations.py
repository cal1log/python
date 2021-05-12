#!/usr/bin/env python3
''' basic math operations '''


def sum(a, b):
    '''
    sum function
    return: sum of a + b
    '''
    return a + b

def subs(a, b):
    '''
    substraction function
    return: substraction of a - b
    '''
    return a - b

def mul(a, b):
    '''
    multiplication function
    return: multiplication of a * b
    '''
    return a * b  

def divFloat(a, b):
    '''
    division function
    return: float division of a / b
    '''
    if a == 0:
        return "division by zero is not possible"
    return a / b

def divInt(a, b):
    '''
    division function
    return: integer division of a / b
    '''
    if a == 0:
        return "division by zero is not possible"
    return a // b

def pow(a, b):
    '''
    power function
    return: power of a * b
    '''
    return a ** b  

def mod(a, b):
    '''
    module function
    return: module of a * b
    '''
    return a % b  

def separator():
    '''
    separator function
    return: a specifier character repetead X times
    '''
    return print(80 * '*')  


''' testing functions '''

''' print raw string omitting scape chars like \n or \t  '''
print(r'Welcome \newbie')
print(r'\t')
print(r'\n')
print(r'\t')

''' print a sum between a and b using a sum function above '''
a = 1
b = 2
c = sum(a, b)
print("the sum between {} and {} is : {}".format(a, b, c))
separator()

''' print a substraction between a and b using a subs function above '''
a = 4
b = 2
c = subs(a, b)
print("the substraction between {} and {} is : {}".format(a, b, c))
separator()

''' print a multiplication between a and b using a mul function above '''
a = 4
b = 2
c = mul(a, b)
print("the multiplication between {} and {} is : {}".format(a, b, c))
separator()

''' print a float division between a and b using a divFloat function above '''
a = 4
b = 2
c = divFloat(a, b)
print("the float division between {} and {} is : {}".format(a, b, c))
separator()

''' print a float division between a and b using a divInt function above '''
a = 5
b = 2
c = divInt(a, b)
print("the integer division between {} and {} is : {}".format(a, b, c))
separator()

''' print a float division between a and b using a divInt function above '''
''' print message error because a equals zero '''
a = 0
b = 2
c = divInt(a, b)
print("the integer division between {} and {} is : {}".format(a, b, c))
separator()

''' print a power between a and b using a pow function above '''
a = 4
b = 2
c = pow(a, b)
print("the power between {} and {} is : {}".format(a, b, c))
separator()

''' print a module between a and b using a mod function above '''
a = 4
b = 3
c = mod(a, b)
print('the mod or "module" between {} and {} is : {}'.format(a, b, c))
separator()