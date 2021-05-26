#!/usr/bin/env python3

''' creating a dictionary '''
dic = {1: 'valuekey1', 2: 'valuekey2', 5: 'valuekey5'}

''' get a dictionary value according the index '''
print(dic[1])

''' get a dictionary value according the index with get function '''
print(dic.get(1))

''' get a dictionary value according not existing index with get function '''
print(dic.get(7))

''' print a message if index does not exist '''
print(dic.get(7, "not found"))

''' creating a dictionary with 2 lists and join them '''
keys = [1, 2, 3]
values = ['valuekey1', 'valuekey2', 'valuekey3']
dic2 = dict(zip(keys, values))
print(dic2.get(1))

''' add a key value pair to a dictionary '''
dic2[4] = 'valuekey4'
print(dic2.get(4))

''' deleting a key value pair from a dictionary '''
print(dic2)
del dic2[1]
print(dic2)

''' creating a dictionary with list and dictionaries values '''
dic3 = {1: 'hola', 'string2': ['list1', 'list2'], 'dt': {1: 'a'}}
print(dic3.get(1))
print(dic3.get('string2'))
print(dic3.get('dt'))
