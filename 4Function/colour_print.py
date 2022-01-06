BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[33m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


def colour_function(text: str, effect: str) -> None:
    """
    Print `text` using the ANSI sequences change colors, etc
    :param text: The text to print
    :param effect: The effect we want. One of the constants defined at the start of this module.
    """
    output_string = "{0}{1}{2}".format(effect, text, RESET)
    print(output_string)


colour_function("Meo...meo", RED)
print("This text doesn't change color!")
colour_function("gau...gau", BLUE)
