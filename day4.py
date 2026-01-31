#1. Reverse a number
num = int(input("Enter a number :"))
org = num
rev = 0
while num!=0:
    digit = num%10
    rev = rev*10+digit
    num //= 10
print(f'Reverse of {org} is {rev}')

#2. Check palindrome number
num = int(input("Enter a number :"))
org = num
rev = 0
while num!=0:
    digit = num%10
    rev = rev*10+digit
    num //= 10
if rev == org:
    print(f'{org} is a palindrome')

#3. Count digits
num = int(input("Enter a number :"))
numbers = str(num)
digits = 0
for char in numbers:
    if char in "0123456789":
        digits += 1
print(f"Number of digits in {num} are {digits}")


#4. Sum of digits
num = int(input("Enter a number :"))
numbers = str(num)
sum = 0
for char in numbers:
    if char in "0123456789":
        sum += int(char)
print(f"sum of digits in {num} are {sum}")

#5. Armstrong number
num = int(input("Enter a number :"))
length = len(str(num))
num_str = str(num)
armsstrong = 0
for char in num_str:
    armsstrong += int(char)**length
if armsstrong == num:
    print("Armstrong..")