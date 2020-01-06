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

### String Assignments
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
* Slicing allows you to grab a subsection of multiple characters, a "slice" of
 the string. This has the following syntax: **[start:stop:step]**
  * **start** is a numerical index for the slice start
  * **stop** is the index you will go up to but not include
  * **step** is the size of the "jump" you take
```
>>> test = 'hello world'
>>> test
'hello world'
>>> test = "hello world"
>>> test
'hello world'
>>> test = "Hello world, I'm here"
>>> test
"Hello world, I'm here"
>>> print(test)
Hello world, I'm here
>>> len("Hello")
5
```
