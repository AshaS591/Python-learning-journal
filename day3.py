"""Dictionaries"""

#21. Count word frequency in a sentence.
sentence = "In every day, there are 1,440 minutes. That means we have 1,440 daily opportunities to make a positive impact."
words = sentence.split()
output = {}
for word in words:
    output[word] = words.count(word)
print(output)

#22. Merge two dictionaries.
products = {
    101: {"name": "Laptop", "price": 1200},
    102: {"name": "Smartphone", "price": 800},
    103: {"name": "Headphones", "price": 150}
}
names = {
    'name':'asha'
}
products.update(names)
print(products)

#23 Find keys with maximum value.
max_key =[]
student_ages = {"asha":23, "suki":25, "divya":25}
max_value = max(student_ages.values())
for key ,value in student_ages.items():
    if value == max_value:
        max_key.append(key)
print(max_key)

#24. Sort a dictionary by value.
inventory = {"apples": 10, "bananas": 5, "cherries": 25}
order = dict(sorted(inventory.items(), key=lambda item:item[1]))
print(order)

#25. Create a dictionary from two lists.
names = ['asha','anusha','ram','raghu']
ages = [23,24,22,21]
out = {}
for index in range(len(names)):
    out[names[index]] = ages[index]
print(out)

#26. Print all prime numbers between 1 and N
num = int(input("Enter a number :"))
if num == 1:
    print('Not a prime..')

else:
    for num1 in range(2,num):
        for number in range(2,num1):
            if num1%number == 0:
                break
        else:
            print(num1)


#27. Find factorial of a number

#28. Fibonacci series up to N terms

#29. Reverse a number

#30. Check if a number is palindrome