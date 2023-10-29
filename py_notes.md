# py code notes

#### Using ```format```

```python
x,y,z = [1, 2, 3]
list = "strings {}, {}, and {}".format(x,y,z)
print(list) 
```

#### ```with``` statement

```with```statement in python is commonly used ``` try/finally``` error handling. 

To open and write to a file in python

```python
'''self note: confusing - read more on this'''

# using with statement to open and write file ("w" = write mode vs "r")
with open ("example.txt","w") as file: # opens or creates a file if not already there
    file.write("hello world!") 		   # edits file and closes it

# long way of writing this:
f = open ("example.txt","w")
try:
    f.write("hello world!")
finally:
    f.close()
```

#### ```_``` operator for calculations

The last printed expression is assigned to the variable `_`. 

```python
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
```

#### adding ```r``` to path

If you don’t want characters prefaced by `\` to be interpreted as special characters, you can use *raw strings* by adding an `r` before the first quote:

```python
>>> print('C:\some\name')  # here \n means newline!
C:\some
ame
>>> print(r'C:\some\name')  # adding r before the quote will not break string
C:\some\name
```

#### String Slicing

 * **note**: python strings are immutable
   * Immutable objects include numbers, strings and tuples. Such an object *cannot* be altered. A new object has to be created if a different value has to be stored. 

```python
word = 'Python'

>>>word[0:2]  # characters from position 0 (included) to 2 (excluded)
'Py'
>>> word[:2]   # character from the beginning to position 2 (excluded)
'Py'

>>> word[2:5]  # characters from position 2 (included) to 5 (excluded)
'tho'

>>> word[4:]   # characters from position 4 (included) to the end
'on'
>>> word[-2:]  # characters from the second-last (included) to the end
'on'
```

#### Lists

* lists are a mutable, meaning you can alter a list

```python
>>> cubes = [1, 8, 27, 65, 125]  # something's wrong here
>>> 4 ** 3  # the cube of 4 is 64, not 65!
64
>>> cubes[3] = 64  # replacing the '65' value to a '64'
>>> cubes
[1, 8, 27, 64, 125]
```

It is possible to nest lists

```python
>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1] #indexting the 2nd value of nested list 1 which is 'a'
'b'
```

#### ```while``` loop

```python
# Fibonacci series: the sum of two elements defines the next
a, b = 0, 1
>>> while a < 10:
...     print(a)
...     a, b = b, a+b

#output:
0
1
1
2
3
5
8

```

* step by step explanation

  * ```a``` and ```b``` is assigned to values ```0``` and ```1``` respectively 

  * The ```while``` loop executes as long as the condition (here: `a < 10`) remains true

    * first print value ```a```
    * re-assign values ```a``` and ```b``` to the next sequence 

    

The keyword argument *end* can be used to avoid the newline after the output, or end the output with a different string:

```python
>>> a, b = 0, 1
>>> while a < 1000:
...     print(a, end=',')
...     a, b = b, a+b
...
0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
```

#### ```if``` statements

