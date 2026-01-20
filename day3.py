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