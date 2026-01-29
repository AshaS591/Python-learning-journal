#1. Reverse a number
num = int(input("Enter a number :"))
org = num
rev = 0
while num!=0:
    digit = num%10
    rev = rev*10+digit
    num //= 10
print(f'Reverse of {org} = {rev}')

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


#4. Sum of digits

#5. Armstrong number