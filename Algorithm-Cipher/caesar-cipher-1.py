import string

str = string.ascii_lowercase
arr = []
for i in str:
    arr.append(i)


def encrypt(char):
    return ((char + 3) % 26)  # 3 là key


def decrypt(char):
    return ((encrypt(char) - 6) % 26)  # 6 là 2*3 (key)


str1 = input("Enter plaintext: ")
value = []
print("Cipher: ")
for index in str1:
    for index_1 in arr:
        if index == index_1:
            # in giá trị của mảng tại vị trí index
            print((arr[encrypt(arr.index(index))]), end="")
            # thêm vào mảng value kí tự vừa đc encrypt
            value.append(arr[encrypt(arr.index(index))])


# print("\n", value)
print("\nPlaintext: ")

for index_2 in value:
    for index_3 in arr:
        if index_2 == index_3:
            # print(index_2, end="")
            print((arr[decrypt(arr.index(index_3))]), end="")
