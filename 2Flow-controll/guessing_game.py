import random


def get_integer(prompt):
    """
    Get an integer from Standard Input (stdin).
    The function will continue looping, and prompting
    the user, until a valid `int` is entered.

    :param prompt: The String that user will see, when
        they're prompted to enter the value.

    :return: The integer that user entered.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        print("{} is not a valid number".format(prompt))


highest = 10
answer = random.randint(1, highest)
print(answer)  # TODO: Remove after testing
# print(get_integer.__doc__) # show docstrings of function get_integer
# help(get_integer) # show docstrings of function get_integer
print("Please guess number between 1 and {}: ".format(highest), end="")
guess = get_integer("input: ")

if guess == answer:
    print("You got it fist time.")
else:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it.")
    else:
        print("Sorry, you have not guessed correctly.")
