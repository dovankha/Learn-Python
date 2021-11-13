number = input("Please enter a series of number, using any separator you like: ")
separator = ""

for char in number:
    if not char.isnumeric():
        separator = separator + char

value = "".join(char if char not in separator else " " for char in number).split()
print("Sum = ", sum([int(val) for val in value]))


for i in range(10, 1, -1):
    print("i is {} now.".format(i))

