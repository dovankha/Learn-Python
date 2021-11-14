i = 0
while i < 10:
    print("i is {} now!".format(i))
    i += 1

available_exit = ['east', 'west', 'north', 'south']
chosen_exit = ''

while chosen_exit not in available_exit:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit.casefold() == "quit":
        print("Game over")
        break

print("Aren't you glad you got out of there")
