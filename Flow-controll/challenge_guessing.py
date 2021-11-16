import random
import os
highest = 10
answer = random.randint(1, highest)
# print(answer)  # TODO: remove after testing
guess = 0
print("Please enter number between 1 and {}.".format(highest))
while guess != answer:
    guess = int(input("Guess = "))
    if guess == 0:
        print("Thank you!")
        os.system("pause")
        break
    elif guess == answer:
        print("You Win! Contact to KhaDepTrai recive money...")
        os.system("pause")
        break
    else:
        if guess < answer:
            print("Please guess higher.")
        else:
            print("Please guess lower.")
