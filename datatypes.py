#!/usr/bin/env python3

''' data types '''

''' none '''
''' not value assigned. Similar to null '''
a = None
print('None')
print(type(a))
print()

''' numeric '''
''' it has four subtypes int, float, complex and bool '''

''' int '''
b = 2
print('2')
print(type(b))
print()

''' float '''
c = 2.5
print('2.5')
print(type(c))
print()

''' complex '''
d = 2.5 + 3j
print('2.5 + 3j')
print(type(d))
print()

d = complex(b, c)
print('complex(2, 2.5)')
print(type(d))
print(d)
print()

''' bool '''
e = 1
f = 2
print('e > f')
print(e > f)
print(type(e > f))
print()

print('int(True)')
print(int(True))
print(type(int(True)))
print()

print('int(False)')
print(int(False))
print(type(int(False)))
print()

''' sequence data types '''

''' list '''
lst = [12, 24, 36, 48 , 60]
print('lst = [12, 24, 36, 48 , 60]')
print(type(lst))
print()

''' set '''
''' set datatype takes unique values of some values '''
s = {1, 2, 3, 4 , 6, 1, 4, 6}
print('s = {1, 2, 3, 4 , 6, 1, 4, 6}')
print(s)
print(type(s))
print()

''' tuple '''
t = (1, 3, 5)
print('t = (1, 3, 5)')
print(type(t))
print()

''' string '''
st = 'orlando'
print('st = \'orlando\'')
print(type(st))
print()

''' range '''
rg = list(range(10))
print('rg = list(range(10))')
print(rg)
print()
print('range(10)')
print(type(range(10)))
print()

''' dictionary '''
dt = {'first_name': 'orlando', 'last_name': 'gomez lopez'}
print("dt = {'first_name': 'orlando', 'last_name': 'gomez lopez'}")
print(dt)
print(type(dt))
print()


print('dictionary keys')
print('print(dt.keys())')
print(dt.keys())
print()

print('dictionary values')
print('print(dt.values())')
print(dt.values())
print()

print('dictionary value accessing with index')
print("print(dt['first_name'])")
print(print(dt['first_name']))
print()


print('dictionary value accessing with get function')
print("print(dt.get('last_name'))")
print(print(dt.get('last_name')))
print()

