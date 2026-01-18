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

#14. Find the frequency of characters in a string.
string = 'Practice'
output = {}
count = 0
for char in string:
    if char not in output:
        output[char] = 1
    else:
        output[char] += 1
print(f"Frequency of characters in a string :{output}")

#15. Remove duplicate characters from a string.
string = "Good work"
new = ''
for char in string:
    if char not in new:
        new += char
print(f"String after removing duplicates : {new}")

"""Lists"""

#16. Find the largest and smallest element in a list.
numbers = [2,1,9,6]
max_num, min_num = max(numbers),min(numbers)
print(f"Largest element is {max_num} and smallest element is {min_num}")

#17. Remove duplicate elements from a list.
names = ['asha','anu','shashi','vasu','anu']

for name in names:
   if names.count(name) > 1:
       names.remove(name)
print(f"After removing duplicate :{names}")



