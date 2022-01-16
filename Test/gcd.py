def gcd(a, b):
    while a*b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


a = int(input("Please enter a = "))
b = int(input("Please enter b = "))
print("gcd({},{}) = {}".format(a, b, gcd(a, b)))
