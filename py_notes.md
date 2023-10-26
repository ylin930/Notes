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

```
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

```
>>> print('C:\some\name')  # here \n means newline!
C:\some
ame
>>> print(r'C:\some\name')  # adding r before the quote will not break string
C:\some\name
```

#### String Slicing

```
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

