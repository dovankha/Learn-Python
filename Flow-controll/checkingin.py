# parrot = "Hello, My name is Vet"
# letter = input("Enter a character: ")
# print(letter.casefold()) #casefold: print lowercase
# if letter in parrot:
#     print('Yes. {} is in "{}"'.format(letter, parrot))
# elif letter not in parrot:
#     print("No. We don't find \"{}\"".format(letter))

#exercise:
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if name == "" or age == "":
    print("Ops! Please enter again!")
# elif 18 <= age < 31:
elif age not in (18, 32):
    print("Oh noo. Age must be over 18 and under 30")
else:
    print("Welcome {} to Python. Are you {} years old?".format(name, age))