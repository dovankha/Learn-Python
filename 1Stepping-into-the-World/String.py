name = input("Please enter your name: ")
greeting = "Hello"
print(greeting + ' ' + name)
parrot = "Norwegian Blue"
print(parrot)
print(parrot[2])
print(parrot[-4:2])
print(parrot[0:6:2]) # step in a slice (từ 0 tới vị trí 6, step: 2)

number = "9,223,372,036,137,085,755,708"
seperators = number[1::4]
print(seperators)

value = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in value])
print("VALUE: ", value)
