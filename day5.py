#1. Multiplication table
number = int(input("Enter a number :"))
for num in range(1,11):
    print(f"{number} x {num} = {number*num}")

#2. GCD of two numbers
def gcd(num1,num2):
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1%num2)
num1,num2 =20,0
print(f"GCD of {num1}, {num2} = {gcd(num1,num2)}")

#3. LCM of two numbers
def gcd(num1,num2):
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1%num2)
num1,num2 =2,9
lcm = (num1*num2)//gcd(num1,num2)
print(f'lcm of {num1}, {num2} = {lcm}')

#4. Power of a number
num = int(input("Enter a number :"))
power = int(input("Enter power :"))
print(f"{num} power {power} is {num**power}")

#5.Pattern:
"""
*
**
***
****
"""
rows = int(input("Enter no of rows :"))
for row in range(1,rows+1):
    for col in range(1,row+1):
        print("*",end=" ")
    print()

