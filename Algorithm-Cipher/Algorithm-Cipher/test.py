def encrypt(char):
    return ((char + 3) % 26)


def decrypt(x):
    return ((encrypt(x) - 6) % 26)

print(encrypt(12))
print(decrypt(15))