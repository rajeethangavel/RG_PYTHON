# Q1
# Print 'Hello Python'
print("Hello Python")
# Q2
# Addition
Num1 = int(input("Enter addend1: "))
Num2 = int(input("Enter addend 2: "))
Total = Num1 + Num2
print(f"Sum of: {Num1} + {Num2} = {Total}")
# Division
Num3 = int(input("Enter Dividend: "))
Num4 = int(input("Enter Divisor: "))
if Num3 == 0:
    print("Error : Division by 0 is not possible")
else:
    Div_Res = Num3 / Num4
    print(f"{Num3} divided by {Num4} = {Div_Res}")
# Q3
# Area of Triangle
base = float(input("Enter base of the Triangle: "))
height = float(input("Enter height of the Triangle: "))
area = 0.5 * base * height
print(f"Area of Triangle with base of {base} and height of {height} = {area}")
# Q4
# Swap values between 2 variables
var1 = input("Enter value of variable1: ")
var2 = input("Enter value of  variable2: ")
print(f"Original value of  var1= {var1} and var2 = {var2}")
temp = var1
var1 = var2
var2 = temp
print(f"Swapped values of var1 = {var1} and var2 = {var2}")
# Q5
# Generate Random Number
import random
print(f"Random number between 1 and 10 is {random.randint(1, 200)}")
# Q6
# Convert Kilometers to Miles
kilo1 = float(input(f"Enter Kilometer value: "))
kilo_conv_val = 0.621
mile1 = kilo1 * kilo_conv_val
print(f"{kilo1} kilometers equals {mile1} miles")
# Q7
# Convert Celsius to Fahrenheit
celsius1 = float(input(f"Enter Celsius Value: "))
fahren1 = (celsius1 * 2) + 30
print(f"{celsius1} Celsius equals {fahren1} Fahrenheit")
# Q 8
# Display Calendar
import calendar
year = int(input("Enter Year: "))
mnth = int(input("Enter Month: "))
caln = calendar.month(year, mnth)
print(caln)
# Q 10
# Swap variable values without using temp variable
var3 = float(input("Enter value of variable1: "))
var4 = float(input("Enter value of  variable2: "))
print(f"Original value of  var1= {var3} and var2 = {var4}")
var3, var4 = var4, var3
print(f"Swapped values of var1 = {var3} and var2 = {var4}")
# Q11
# Check if a number is positive,negative or 0.
chk_num = float(input(f"Enter Number for +/- chk: "))
if chk_num > 0:
    print(f"{chk_num} is Positive")
else:
    if chk_num == 0:
        print("The number is Zero")
    else:
        print(f"{chk_num} is Negative")
# Q12
# Check if a number is Even or Odd
Num5 = int(input("Enter number for Odd/Even Chk: "))
if Num5 % 2 == 0:
    print(f"{Num5} is Even")
else:
    print(f"{Num5} is Odd")