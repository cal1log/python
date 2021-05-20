#!/usr/bin/env python3

'''number list'''
list1 = [1, 2, 3]
print(list1)

'''char list'''
list2 = ['a', 'b', 'c']
print(list2)

'''append function to add a value at the end of the list'''
list1.append(4)
print(list1)

'''insert function to add a value in a specific index of the list'''
list2.insert(2, 'd')
print(list2)

'''adding two lists inside one'''
list3 = [list1, list2]
print(list3)

'''remove function to delete a value inside a list depending your value'''
list1.remove(1)
print(list1)

'''pop function to delete a value of a specific index of a list'''
list1.pop(2)
print(list1)

'''pop function to delete the last element of a list'''
list1.pop()
print(list1)

'''del function to delete many elements of a list'''
del list2[2:]
print(list2)

'''extend function to add list elements to a list'''
list1.extend([2,3,4])
print(list1)

'''min function to get the minimum value of a list'''
print(min(list1))

'''max function to get the minimum value of a list'''
print(max(list1))

'''sum function to get the sum of all values of a list'''
print(sum(list1))

'''sort function to sort all values of a list in an incremental way'''
list1.sort()
print(list1)

'''sort function to sort all values of a list in an decremental way'''
list1.sort(reverse=True)
print(list1)