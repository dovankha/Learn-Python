import random

highest = 10
answer = random.randint(1, highest)
print(answer)  # TODO: Remove after testing

print("Please guess number between 1 and {}: ".format(highest), end="")
guess = int(input())

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
