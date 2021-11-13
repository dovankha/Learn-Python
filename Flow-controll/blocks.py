# name = input("Please enter your name: ")
# age = int(input('How old are you, {}? '.format(name)))
# if age < 18:
#     print("Please come back in {} years".format(18 - age))
# elif age == 200:
#     print("Sorry, Yoda, you die in Rutrun of the Jedi")
# else:
#     print("You are old enough to vote")
#     print("Please put an X in the box")

day = 'Sunday'
temperature = 26
raining = False

if (day == 'Sunday' and temperature > 27) or not raining:
    print("Go swimming")
else:
    print("Learn Python")

for i in range(1, 65):
    if (i % 9 + 1) == 5:
        print(i)