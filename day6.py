# Print this pattern:

"""
1
12
123
1234
12345"""

number = int(input("Enter a number :"))


for row in range(1,number+1):
    for col in range(row):
            print(col+1,end=" ")
    print()