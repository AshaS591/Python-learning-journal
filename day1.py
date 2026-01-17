# 1. Write a program to print “Hello, World!”
print("Hello, World!")

# Write a program to take user input and display it.
name = input("Enter your name :")
print(f'My name is {name}')

# Write a program to check whether a number is even or odd.
number = int(input('Enter a number :'))
if number%2 == 0 :
    print("Even")
else:
    print("Odd")

# Write a program to find the largest of three numbers.
num1, num2, num3 = 10, 20, 30
if num1 == num2 and num2 ==3 and num1 == num3:
    print("All are equal")

else:
    if num1>num2 and num1>num3:
        print(f"{num1} is largest")
    elif num2>num1 and num2>num3:
        print(f"{num2} is largest")
    else:
        print(f"{num3} is largest")

# Write a program to calculate the sum of first N natural numbers.
num = int(input('Enter a number :'))
sum = 0
for number in range(num):
    sum += number
print(f'Sum of {num} natural numbers :{sum}')

# Write a program to print all even numbers between 1 and 100.

# Write a program to check if a number is positive, negative, or zero.

# Write a program to swap two variables without using a third variable.

# Write a program to calculate simple interest.

# Write a program to convert Celsius to Fahrenheit.