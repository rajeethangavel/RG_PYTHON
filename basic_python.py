print('Welcome To The World Of Python')  # Usage of print()
print()
name = input('Enter your Name : ')  # Usage of input () to get user input
print()
print('Welcome ' + name.upper())  # Using one of the String Method
print('*' * 15)
yr_of_birth = input('Enter your year of Birth : ')
import datetime
# from datetime import date  # importing date from the inbuilt python module datetime
prsnt_yr = datetime.date.today().year  # Extracting only year from current date
age = prsnt_yr - int(yr_of_birth)  # Calculating Age
print(f'Your Age is {age}')  # Formatted String usage
print()
color = input('Enter your Fav Color : ')
print(f"{name.title()}'s favourite color is {color.title()}")  # Formatted String usage
print()
str1 = 'Happy Learning'
print(f'{str1} {name.title()}')
print()
str2 = input('Enter any string to test find(),replace() : ')
chr_chk = input(f'Enter any char from "{str2}" to find its position: ')
print(f"The positions of '{chr_chk}' is: {str2.find(chr_chk)}")  # String method
# find() Prints the index/position of the character's 1st appearance
print()
chr_pres = input(f'Enter the char you want replaced in "{str2}": ')
chr_rep = input(f"Enter the char you want '{chr_pres}' replaced with in '{str2}': ")
print()
print(f"Replacing '{chr_pres}' with '{chr_rep}' in '{str2}' resulted in '{str2.replace(chr_pres, chr_rep)}'")
# upper(),lower(),title(),find(),replace() are some of the string methods in Python
# int ,float, boolean ,string are some of the datatypes of Python
bool_chk = True  # Boolean type
# print(f'Datatype of variable boolchk is {type(bool_chk)}')
print()
str_chk = input(f'Enter the char that you want to chk for its presence in "{str2}": ')
x = str_chk in str2
print()
print(f'Is the char "{str_chk}" present ? {x}')  # Boolean type returns True/False
str3 = str2[:]  # Assigns the value of str1 to str2
print()
print(str3)
print()
