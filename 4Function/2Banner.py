def banner(text: str = " ", screen_width: int = 80) -> None:
    if len(text) > screen_width - 4:
        raise ValueError("{} is large to fit {}.".format(text, screen_width))
    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{}**".format(text.center(screen_width - 4))
        print(output_string)


banner("*")
banner("Hello everyone, my name is Kha!")
banner("I studying in PTITHCM. Major is Information Security.")
banner(screen_width=60)
banner("*")

numbers = [1, 3, 2, 6, 4, 9, 8]
print("numbers = ", numbers)
list1 = sorted(numbers)
print("numbers.sort() = ", list1)
