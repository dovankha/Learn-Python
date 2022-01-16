import colorama
import time

CYAN = '\u001b[36m'
RED = '\u001b[31m'
RESET = '\u001b[0m'
GREEN = '\u001b[32m'
tool_name = '''
 ██████╗  ██████╗██████╗ 
██╔════╝ ██╔════╝██╔══██╗
██║  ███╗██║     ██║  ██║
██║   ██║██║     ██║  ██║
╚██████╔╝╚██████╗██████╔╝
 ╚═════╝  ╚═════╝╚═════╝ 
'''


def gcd(x, y):
    while x*y != 0:
        if x > y:
            x %= y
        else:
            y %= x
    return x + y


def colour_function(text: str, effect: str) -> None:
    """
    Print `text` using the ANSI sequences change colors, etc.
    :param text: The text to print
    :param effect: The effect we want. One of the constants defined at the start of this module.
    """
    output_string = "{0}{1}{2}".format(effect, text, RESET)
    print(output_string)


colorama.init()
colour_function(tool_name, CYAN)
choice = '_a'
while True:

    a = int(input("Please enter an integer 1: "))
    b = int(input("Please enter an integer 2: "))
    print(GREEN, "GCD({},{}) = {}".format(a, b, gcd(a, b)), RESET)
    print("\nDo you want to try again? \
          1. Yes \
          2. No")
    choice = int(input("Please choice 1 or 2: "))
    if choice == 1:
        continue
    elif choice == 2:
        colour_function("Done!", CYAN)
        time.sleep(2)
        exit()
    else:
        colour_function("Your choice incorrect!", RED)
        time.sleep(2)
        exit()
colorama.deinit()
