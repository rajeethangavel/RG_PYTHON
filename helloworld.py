# Python Learning
# Commenting
# There is no command for multi line comments in python
print("Hello Rajee")  # Anything given with "" is considered a string and printed
# code execution
# Python syntax can be executed by writing directly in the Command Line
# or by creating a python file on the server, using the .py file extension,
# and running it in the Command Line
# syntax and indentation
# Python uses indentation to indicate a block of code.
if 10 > 5:  # : is must
    print("10 is greater than 5")
    print("This is interesting")
    '''This is another way to add comments.you can use single or double quotes for this purpose'''
x = 25
y = 40
z = x + y
print(z)
# Casting
x1 = str(5)  # x will be '3'
y1 = int(5)  # y will be 3
z1 = float(3)  # z will be 3.0
print(type(x1))  # to print/get the variable type
q = "Iam"
b = 'yellow'  # String can be assigned in double quotes or single quotes.
print(q)  # variable names are case-sensitive
a = 'sweet'
A = 'karam'
print(A)
_var1 = 'Rajee'  # variable name is case-sensitive,can start with character or _ but not with number
print(_var1)
a1, b1, c1 = "apple", "orange", "mango"  # assigning values to multiple variables
d1 = e1 = f1 = "guvava"  # assigning single value to multiple variables
print(e1)
flowers = ["lilly", "jasmine", "rose"]  # unpacking a collection of values
t1, t2, t3 = flowers
print(t1, t2, t3)  # In the print() function, you output multiple variables, separated by a comma
print(t1 + ' ' + t2 + ' ' + t3)  # You can also use the + operator to output multiple variables
x2 = 5
y2 = 44
print(x2 + y2)  # For numbers, the + character works as a mathematical operator
print(t1, x2)  # The best way to output multiple variables in the print() function
# is to separate them with commas,which even support different data types
zz = "happy"
# functions


def myfirstfn():
    print(zz + " tomorrow")
    print(A + " today")


myfirstfn()


def my2ndfn():
    x = 4  # there ia already a global variable x defined outside this function and this is local variable
    y = 3  # there ia already a global variable y defined outside this function and this is local variable
    print(x + y)


my2ndfn()


def my3rdfn():
    # global variable declaring
    global QQ  # can declare a global variable inside function using "global" keyword
    QQ = "Welcome"


my3rdfn()
print(QQ)
# data types
t = 35e4  # float
tt = 34E4  # float
ttt = -456.567e24  # float
print(type(t), type(tt), type(ttt))
s = 4+5j  # complex
ss = -5j   # complex
sss = 5e5j  # complex
print(type(s), type(ss), type(sss))
z = 5
z1 = 5.7
z2 = -7.77
dd = int(z1)  # type conversion
print(dd, type(dd))
# importing module
import random  # python doesn't have random() to make random numbers
# so Import the random module for the purpose
print(random.randrange(1, 10))  # display a random number between 1 and 9
print('I will come')
print("what's this")  # You can use quotes inside a string, as long as
# they don't match the quotes surrounding the string
g = """I'm not feeling good
about this in any way Tilo"""  # You can assign a multiline string to a
# variable by using three quotes either single or double quotes
# to extract substring from string
print(g[1])  # Square brackets can be used to access elements of the string.remember
# that the first character has the position 0
# loop through characters
for TT in 'Tilo':  # Since strings are arrays, we can loop through the characters in a string, with a for loop
    print(TT)
# finding string length
print(len(g))  # find length of string
# to  check for certain character or phrase in a string
print("way" in g)  # To check if a certain phrase or character is present in a string,
# we can use the keyword in.o/p would be True/False
if "way" in g:  # Use it in an if statement
    print("This is very interesting")
if "ways" not in g:  # Use it in an if statement to check not in
    print("This is even more interesting")
# extracting substring from a string using index
AA = "what is happening"
print(AA[2:8])  # Specify the start index and the end index, separated by a colon, to return a part of the string.
print(AA[:10])  # By leaving out the start index, the range will start at the first character
print(AA[5:])  # By leaving out the end index, the range will go to the end
print(AA[-6:-1])  # Use negative indexes to start the slice from the end of the string
X = ' welcome, to the, world '
print(X[3:5])  # this will print only 'co' and not 'com'
# string functions
print(X.upper())  # returns the string in upper case
print(X.lower())  # returns the string in lower case
print(X.strip())   # removes any whitespace from the beginning or the end
print(X.replace('e', 'y'))  # replaces character
print(X.split(","))  # returns a list where the text between the specified separator
# becomes the list items.splits the string into substrings if it finds instances of the separator
print(X.split("e"))  # returns a list where the text between the specified separator
# becomes the list items.splits the string into substrings if it finds instances of the separator
# string concatenation
print(AA + " " + X)  # use + to concatenate two strings.use " " to add space.
# F-string
cost = 40
s = f"The cost of one apple is {cost}"  # F-string is used to combine string and number,
# simply put an f in front of the string and {} as placeholders for variables and other operations.
print(s)
v = f"The cost of one apple is {cost: .2f}"  # modifier is included by adding a colon :
# followed by a legal formatting type, like .2f to display price in 2 decimal
print(v)
vv = f"The cost of one mango is {20*5}"  # placeholder can contain Python code, like math operations
print(vv)
# to insert escape characters
print("Let's try \"this\"")  # to insert an escape character.An escape character
# is a backslash \ followed by the character you want to insert
# more string functions/methods
print(d1.capitalize())  # Converts the first character to upper case
dd = d1.center(20)
print(dd)  # Returns a centered string
print(dd.count("a"))  # Returns the number of times a specified value occurs in a string
# string encoding
W = "My name is åFun"
ww = W.encode()
print(ww)  # encodes the string using the specified encoding.
# If no encoding is specified, UTF-8 will be used.
# boolean values
print(11 == 12)  # boolean values,gives true or false
print(bool(W))  # boolean of any string is True, except empty strings.
print(bool(cost))  # boolean of any list, tuple, set, and dictionary are True, except empty ones.
print(bool(0))  # boolean of any number is True, except 0 is false


def booleanchk():  # You can execute code based on the Boolean answer of a function
    return True


if booleanchk():
    print("Yes")
else:
    print("No")
# isinstance() usage
print(isinstance(W, int))  # isinstance() is a built-in function, which
# can be used to determine if an object is of a certain data type.returns true or false
# Arithmetic operators
print(2**3)  # exponential
print(24//2)  # floor division
# assignment operators
XX = 5
XX += 3  # same as xx=xx+3
print(XX)
YY = 5
YY /= 3  # same as yy=yy/3
print(YY)
print(XX != YY)  # returns true or false
# Logical operators
print(XX > 5 and YY > 5)
print(XX >= 5 or YY > 5)
print(not(XX >= 5 or YY > 5))
# identity operators
# used to compare the objects, not if they are equal, but if they are
# actually the same object, with the same memory location
print(XX, YY, XX is YY)
print(x, y, x is y)  # returns False because x is not the same object as y, even if they have the same content
x = y
print(x, y, x is y)  # returns True because x is  same object as y and shares same memory location
# membership operators
# returns true or false depending on if the sequence with the value is present in the list
SS = [5, 10, 15]
print(5 in SS)  # returns true
print(20 in SS)  # returns false as 20 is not present in the SS list.
fruitlist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruitlist[2:5])  # The search will start at index 2 (included) and end at index 5 (not included)
fruitlist[2] = 'cucumber'  # To change the value of a specific item, refer to the index number
print(fruitlist)
fruitlist[1:3] = ['papaya', 'abc', '123']
print(fruitlist)
fruitlist.insert(5, 'winter-melon')  # to insert items to list
print(fruitlist)
fruitlist.append('watermelon')  # to append items to list
print(fruitlist)
veglist = ['onion', 'tomato', 'potato', 'chilli']
print(veglist)
veglist.extend(fruitlist)  # to extend items  from one list to other list
print(veglist)
fruitlist.remove('abc')
print(fruitlist)   # to remove item from a list
fruitlist.pop(2)  # to remove item based on index.
# If no index is specified it would remove the last item from list
print(fruitlist)
del fruitlist[3]  # to remove item based on index.
print(fruitlist)
for i in veglist:  # Loop through a list
    print(i)
# for x in range(len(veglist)):  # Loop through a list  using  index numbers
#  print(veglist[x])
swtlist = ['Halwa', 'Gulabjamun', 'Kesari']
i = 0
while i < len(swtlist):
    print(swtlist[i])
    i = i + 1