#  Arithmetic operators
addend1 = float(input('Enter Addend1 : '))
addend2 = float(input('Enter Addend2 : '))
addition = round(addend1 + addend2)
print(f'{addend1} + {addend2} = {addition}')
subtn = round(addend1 - addend2)
print(f'{addend1} - {addend2} = {subtn}')
multi = round(addend1 * addend2)
print(f'{addend1} * {addend2} = {multi}')
division = round(addend1 / addend2)  # Normal division
print(f'{addend1} / {addend2} = {division}')
div1 = addend1 // addend2  # Division that will return the result in int type
print(f'{addend1} // {addend2} = {div1}')
modulus = addend1 % addend2  # Returns the reminder
print(f'{addend1} % {addend2} = {modulus}')
expo = round(addend1 ** addend2)  # Exponential
print(f' {addend1} ^ {addend2} = {expo}')
print()
x = int(input('Enter value for X: '))
x += 5  # Augmented/Enhanced assignment operator
print(f' (X += 5) returns {x}')

# Python Modules
import math
addend1 = float(input('Enter Addend1 : '))
addend2 = float(input('Enter Addend2 : '))
print(f' ceil of {addend1} is {math.ceil(addend1)}')
print(f' floor of {addend1} is {math.floor(addend1)}')
