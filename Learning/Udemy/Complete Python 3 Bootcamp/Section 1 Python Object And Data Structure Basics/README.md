# Python Objects and Data Structure Basics

## Python Data Types

| Name           | Type  | Description                            |
|:---------------|:------|:---------------------------------------|
| Integers       | int   | whole numbers                          |
| Floating Point | float | number with a decimal point            |
| Strings        | str   | ordered sequence of characters         |
| Lists          | list  | ordered sequence of objects            |
| Dictionaries   | dict  | unordered key:value pairs              |
| Tuples         | tup   | ordered immutable sequence of objects  |
| Sets           | set   | unordered collection of unique objects |
| Booleans       | bool  | logical values true or false           |

What's the difference between floating point and an integer? An integer has no 
 decimals in it, a floating point number can display digits past the decimal point.

Why doesn't 0.1+0.2-0.3 equal 0.0? This has to do with floating point accuracy 
 and computer's abilities to represent numbers in memory.

## Basic Math In Python

| Name           | Symbol | Example |
|:---------------|:------:|:--------|
| Addition       | +      | 2 + 1   |
| Subtraction    | -      | 2 - 1   |
| Multiplication | *      | 2 \* 1  |
| Division       | /      | 2 / 1   |
| Modulus        | %      | 7 % 4   |
| Exponents      | **     | 2 ** 3  |

Order of Operations: 2 + 10 * 10 + 3 = 105, (2 + 10) * (10 + 3) = 156

## Variable Assignments
 
Rules for variable names
* Names cannot start with a number.
* There cannot be spaces in the name, use underscore instead.
* Cannot use any of these symbols
  * : ' " , < > / ? | \ ( ) ! @ # $ % ^ & * ~ - +
* Python uses **Dynamic Typing**, which means you can reassign variables to
 different data types.


### Number Assignments
```
>>> a = 10
>>> a
10
>>> a = a + a
>>> a
20
>>> type(a)
<class 'int'>
>>> b = 30.1
>>> type(b)
<class 'float'>
>>> my_income = 100
>>> tax_rate = 0.1
>>> my_taxes = my_income * tax_rate
>>> my_taxes
10
```

### String Assignments & Slicing
* Strings are sequences of characters, using the syntax of either single quotes
 or double quotes
* Strings are ordered sequences, which means we can use **indexing** and
 **slicing** to grab sub-sections of the string.
* Indexing notation uses [] notation after the string (or variable assigned the
 string).
* Indexing allows you to grab a single character from the string.
* These actions use [] square brackets and a number index to indicate positions
 of what you wish to grab.
  * Character: [ 'h', 'e', 'l', 'l', 'o' ]
  * Index: [ 0, 1, 2, 3, 4 ]
  * Reverse Index: [ 0, -4, -3, -2, -1 ]
```
>>> mystring = 'hello world'
>>> mystring
'hello world'
>>> mystring = "hello world"
>>> mystring
'hello world'
>>> mystring = "Hello world, I'm here"
>>> mystring
"Hello world, I'm here"
>>> print(mystring)
Hello world, I'm here
>>> len(mystring)
11
>>> mystring[0]
'H'
>>> mystring[8]
'r'
>>> mystring[-6]
'm'
```

## String Slicing
Slicing allows you to grab a subsection of multiple characters, a "slice" of
 the string. This has the following syntax: **[start:stop:step]**
* **start** is a numerical index for the slice start
* **stop** is the index you will go up to but not include
* **step** is the size of the "jump" you take
```
>>> mystring = "abcdefghijk"
>>> mystring[2:]
'cdefghijk'
>>> mystring[:3]
'abc'
>>> mystring[3:6]
'def'
>>> mystring[::2]
'acegik'
>>> mystring[2:7:2]
'ceg'
>>> mystring[::-1]
'kjihgfedcba'
```

## String Properties & Methods
```
>>> "Hello " + "world"
'Hello world'
>>> 'z' * 10
'zzzzzzzzzz'
>>> 2 + 3
5
>>> '2' + '3'
'23'
>>> "Dog"[0] = "H"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> "H" + "Dog"[1:]
'Hog'
>>> mystring = "Hello World"
>>> mystring.upper()
'HELLO WORLD'
>>> mystring.lower()
'hello world'
>>> mystring.upper
<function str.upper>
>>> mystring.split()
['Hello', 'World']
>>> mystring.split('l')
['He', '', 'o Wor', 'd']
```

## Print Formatting With Strings
```
>>> print('This is a string {}.format('INSERTED'))
This is a string INSERTED
>>> print('The {} {} {}'.format('fox','brown','quick'))
The fox brown quick
>>> print('The {2} {1} {0}'.format('fox','brown','quick'))
The quick brown fox
>>> print('The {0} {0} {0}'.format('fox','brown','quick'))
The fox fox fox
>>> print('The {q} {b} {f}'.format(f='fox',b='brown',q='quick'))
The quick brown fox
>>> result = 100/777
>>> print('The result was {r}'.format(r=result))
The result was 0.1287001287001287
>>> print('The result was {r:1.3f}'.format(r=result))
The result was 0.129
>>> print('The result was {r:10.5f}'.format(r=result))
The result was     0.12870
>>> result = 104.12345
>>> print('The result was {r:1.2f}'.format(r=result))
The result was 104.12
name = "Jose"
age = "20"
print(f'Hello, his name is {name} and he is {age} years old.')
Hello, his name is Jose and he is 20 years old.
```

## Lists
* Lists are ordered sequences that can hold a variety of object types.
* They use [] brackets and commas to separate objects in the list: [1,2,3,4,5]
* Lists support indexing and slicing. Lists can be nested and also have a
 variety of useful methods that can be called off of them.
* Unlike a string, lists are mutable.
```
>>> mylist = [1,2,3]
>>> mylist = ['string', 100, 23.4]
>>> len(mylist)
3
>>> mylist = ['one', 'two', 'three']
>>> mylist
['one', 'two', 'three']
>>> mylist[0]
'one'
>>> mylist[1:]
['two', 'three']
>>> anotherlist = ['four', 'five']
>>> newlist = mylist + anotherlist
>>> newlist
['one', 'two', 'three', 'four', 'five']
>>> newlist[0] = newlist[0].upper()
>>> newlist
['ONE', 'two', 'three', 'four', 'five']
>>> newlist.append('six')
>>> newlist
['ONE', 'two', 'three', 'four', 'five', 'six']
>>> poppeditem = newlist.pop()
>>> newlist
['ONE', 'two', 'three', 'four', 'five']
>>> poppeditem 
'six'
>>> newlist.pop(0)
'ONE'
>>> letters = ['a', 'e', 'x', 'b', 'c']
>>> numbers = [4, 1, 8, 3]
>>> letters.sort()
>>> letters
['a', 'b', 'c', 'e', 'x']
>>> letters = letters.sort()
>>> type(letters)
NoneType
>>> numbers.sort()
>>> numbers
[1, 3, 4, 8]
>>> numbers.reverse()
>>> numbers
[8, 4, 3, 1]
>>> nestedlist = [1, 1, [1, 2]]
>>> nestedlist[2]
[1, 2]
>>> nestedlist[2][1]
2
```

## Dictionaries
* Dictionaries are unordered mappings for storing objects using a key-value pair.
* Key-value pair allows users to quickly grab objects without needing to know an
 index location: {'key1':'value1', 'key2':'value2'}
```
>>> mydictionary = {'key1':'value1', 'key2':'value2'}
>>> mydictionary['key1']
'value1'
>>> storeprices = {'apple': 2.99, 'oranges':1.99}
>>> storeprices['apple']
2.99
>>> mydictionary = {'k1':123, 'k2':[0,1,2], 'k3':{'nestedKey': 100}}
>>> mydictionary['k3']['nextedKey']
100
>>> mydictionary = {'k1':['a','b','c']}
>>> mydictionary['k1'][0].upper()
'A'
>>> mydictionary['k2'] = [1, 2, 3]
>>> mydictionary
{'k1': ['a', 'b', 'c'], 'k2': [1, 2, 3]}
>>> mydictionary.keys()
dict_keys(['k1', 'k2'])
>>> mydictionary.values()
dict_values([['a', 'b', 'c'], [1, 2, 3]])
>>> mydictionary.items()
dict_items([('k1', ['a', 'b', 'c']), ('k2', [1, 2, 3]]))
```

## Tuples
* Tuples are similar to lists but are immutable, once an element is inside a
 tuple, it cannot be reassigned.
* Tuples use parenthesis: (1, 2, 3)
```
>>> mytuple = (1, 1, 2, 3)
>>> type(mytuple)
tuple
>>> mylist = [1, 1, 2, 3]
>>> mytuple.count(1)
2
>>> mytuple.index(1)
0
>>> mylist[0] = 0
>>> mylist
[0, 1, 2, 3]
>>> mytuple[0] = 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> mytuple
(1, 1, 2, 3)
```

## Sets
* Sets are unordered collections of unique elements.
```
>>> myset = set()
>>> myset
set()
>>> myset.add(1)
>>> myset
{1}
>>> myset.add(2)
>>> myset
{1, 2}
>>> myset.add(2)
>>> myset
{1, 2}
>>> set([1,1,1,1,1,1,2,2,2,2,3,3,3,3])
{1,2,3}
```
