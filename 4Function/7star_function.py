numbers = (1, 2, 3, 4, 5)
print(numbers, sep=";")
print(*numbers, sep=";")
print(1, 2, 3, 4, 5, sep=";")


def test_star(*args):
    print(args)
    for x in args:
        print(x)


print()
test_star()  # show () to desktop
test_star(1, 2, 3, 4, 5)
