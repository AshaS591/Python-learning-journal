# 1. Write a program to print “Hello, World!”
print("Hello, World!")

# 2. Write a program to take user input and display it.
name = input("Enter your name :")
print(f'My name is {name}')

# 3. Write a program to check whether a number is even or odd.
number = int(input('Enter a number :'))
if number%2 == 0 :
    print("Even")
else:
    print("Odd")

# 4. Write a program to find the largest of three numbers.
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

# 5. Write a program to calculate the sum of first N natural numbers.
num = int(input('Enter a number :'))
sum = 0
for number in range(num):
    sum += number
print(f'Sum of {num} natural numbers :{sum}')

# 6. Write a program to print all even numbers between 1 and 100.
even_numbers = [num for num in range(1,100) if num%2 == 0] #list comprehension
print(f"All even numbers between 1 and 100 : {even_numbers}")

# 7. Write a program to check if a number is positive, negative, or zero.
num = int(input("Enter number :"))
if num==0:
    print("Zero..")
elif num>0:
    print("Positive..")
else:
    print("Negative..")

# 8. Write a program to swap two variables without using a third variable.
num1 = 10
num2 = 20
print(f"Before swap num1:{num1} and num2 :{num2}")
num1 = num1+num2
num2 = num1-num2
num1 = num1-num2
print(f"After swap num1:{num1} and num2 :{num2}")

# 9. Write a program to calculate simple interest.

# 10. Write a program to convert Celsius to Fahrenheit.