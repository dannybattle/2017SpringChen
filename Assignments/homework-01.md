```python
"""
Name: Huiluo Chen
Email: dannysirchen@gmail.com
Assignment: Homework 1 - Lists and Dictionaries
Due: 31 Jan @ 9:30 a.m.
"""

#A
a = [1, 5, 4, 2, 3] 
print(a[0], a[-1])
# Prints: 1 3

a[4] = a[2] + a[-2]
print(a)
# Prints: [1, 5, 4, 2, 6]

print(len(a))
# Prints: 5

print(4 in a)
# Prints: True

a[1] = [a[1], a[0]]
print(a)
# Prints: [1, [5, 1], 4, 2, 6]

#B
"""
Removes all instances of el from lst. 
Given: x = [3, 1, 2, 1, 5, 1, 1, 7]
Usage: remove_all(1, x)
Would result in: [3, 2, 5, 7]
"""
def remove_all(el, lst):
    while el in x:  #check if el is present in list x 
        lst.remove(el)  #remove the element el
x = [3, 1, 2, 1, 5, 1, 1, 7]
remove_all(1, x)
print(x)

#C
"""
Adds y to the end of lst the number of times x occurs in lst. 
Given: lst = [1, 2, 4, 2, 1]
Usage: add_this_many(1, 5, lst)
Results in: [1, 2, 4, 2, 1, 5, 5]
"""
def add_this_many(x, y, lst):
    for i in range(len(lst)):   #loop through the list
        if lst[i] == x:     #check if x presents
            lst.append(y)   #append y if x presents
lst = [1, 2, 4, 2, 1]
add_this_many(1, 5, lst)
print(lst)

#D
a = [3, 1, 4, 2, 5, 3]
print(a[:4])
# Prints: [3, 1, 4, 2]

print(a)
# Prints: [3, 1, 4, 2, 5, 3]

print(a[1::2])
# Prints: [1, 2, 3]

print(a[:])
# Prints: [3, 1, 4, 2, 5, 3]

print(a[4:2])
# Prints: []

print(a[1:-2])
# Prints: [1, 4, 2]

print(a[::-1])
# Prints: [3, 5, 2, 4, 1, 3]

#E
"""
Reverses lst in place. 
Given: x = [3, 2, 4, 5, 1] 
Usage: reverse(x)
Results: [1, 5, 4, 2, 3]
"""
def reverse(lst):      
    size = len(lst)             # get the length of the list
    hiindex = size - 1
    its = int(size/2)       # number of iterations required
    for i in range(0, its):    # i is the low index pointer
        temp = lst[hiindex]     # perform a classic swap
        lst[hiindex] = lst[i] 
        lst[i] = temp
        hiindex -= 1            # decrement the high index pointer
x = [3, 2, 4, 5, 1]
reverse(x)
print(x)
#The "in place" solution does not need a new lis.

#F
"""
Return a new list, with the same elements of lst, rotated to the right k.
Given: x = [1, 2, 3, 4, 5]
Usage: rotate(x, 3)
Results: [3, 4, 5, 1, 2]
"""
def rotate(lst, k):
  lst_new = [0]*len(lst)    #create a new list 
  for i in range(len(lst)):     #loop through the list
    lst_new[i] = lst[i-k]   #rotate the list
  return lst_new    #return the new list
x = [1, 2, 3, 4, 5]
rotate(x, 3)
print(x)

#H
superbowls = {'joe montana': 4, 'tom brady':3, 'joe flacco': 0}
print(superbowls['tom brady'])
# Prints: 3

superbowls['peyton manning'] = 1
print(superbowls)
# Prints: {'peyton manning': 1, 'tom brady': 3, 'joe flacco': 0, 'joe montana': 4}

superbowls['joe flacco'] = 1
print(superbowls)
# Prints:{'peyton manning': 1, 'tom brady': 3, 'joe flacco': 1, 'joe montana': 4}

print('colin kaepernick' in superbowls)
#Prints: False

print(len(superbowls))
#Prints: 4

print(superbowls['peyton manning'] == superbowls['joe montana'])
#Prints: False

superbowls[('eli manning', 'giants')] = 2
print(superbowls)
#Prints: {'joe montana': 4, 'tom brady': 3, 'joe flacco': 1, 'peyton manning': 1, ('eli manning', 'giants'): 2}

superbowls[3] = 'cat'
print(superbowls)
#Prints: {'joe montana': 4, 'tom brady': 3, 'joe flacco': 1, 'peyton manning': 1, ('eli manning', 'giants'): 2, 3: 'cat'}

superbowls[('eli manning', 'giants')] =  superbowls['joe montana'] + superbowls['peyton manning']
print(superbowls)
#Prints: {'joe montana': 4, 'tom brady': 3, 'joe flacco': 1, 'peyton manning': 1, ('eli manning', 'giants'): 5, 3: 'cat'}

superbowls[['steelers', '49ers']] = 11
print(superbowls)
#Prints: TypeError: unhashable type: 'list'

#I
"""
Replaces all values of x with y. 
Given: d = {1: {2:3, 3:4}, 2:{4:4, 5:3}} 
Usage: replace_all(d,3,1)
Results: {1: {2: 1, 3: 4}, 2: {4: 4, 5: 1}} 
"""
def replace_all(d, x, y):
  for k, v in d.items():   #retrive all pairs in the dictionary
    if type(v) is dict:     #check if v is a dictionary 
      replace_all(v, x, y)
    else:
      if v == x:   #check is the value is x
        d[k] = y     #replace the x value with y
d = {1: {2:3, 3:4}, 2:{4:4, 5:3}}
replace_all(d,3,1)
print(d)
 
#J
"""
Removes all pairs with value x. 
Given:  d = {1:2, 2:3, 3:2, 4:3}
Usage:  rm(d,2)
Results: {2:3, 4:3}
"""
def rm(d, x):
  mark =[]  #create a list to store keys to be deleted
  for k, v in d.items():    #loop through the dictionary
    if v == x:  #check if the values is x
      mark.append(k)    #mark the key
  for i in mark:    #loop through the list to delete all items being marked
    del d[i]
d = {1:2, 2:3, 3:2, 4:3}
rm(d,2)
print(d)
```
