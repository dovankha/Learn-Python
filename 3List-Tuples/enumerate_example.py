for index, char in enumerate("abcdef"):
    print(index, char)

for t in enumerate("abcdefgh"):
    # t will be tuple
    print(t, type(t))

index, character = (1, 'b')
print(index, character)