"""Strings"""

#11. Reverse a string without using built-in functions.
string = 'career'
print(f"Reverse of {string} :{string[::-1]}")

#12. Check whether a string is a palindrome.
string = 'WOW'
if string == string[::-1]:
    print("Palindrome..")
else:
    print("Not a palindrome..")

#13. Count the number of vowels in a string.
string = 'Experiance'
count = 0
for char in string:
    if char in 'AEIOUaeiou':
        count += 1
print(f'Count of vowels in {string} :{count}')





