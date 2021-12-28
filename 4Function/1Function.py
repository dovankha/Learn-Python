def multiple(n, m):
    result = n * m
    return result


def is_palindrome(string):
    str_lowercase = string.lower()
    return str_lowercase[::-1] == string.lower()


print("Result = ", multiple(3, 6))

for val in range(1, 11):
    two_times = multiple(2, val)
    print("2 * ", val, " = ", two_times)


word = input("Please enter a word to check: ")
if is_palindrome(word):
    print("{} is a palindrome.".format(word))
else:
    print("{} is not a palindrome.".format(word))


str_test = "CONGACON"
print(str_test.islower())
print(str_test.capitalize()) # in hoa kí tự đầu tiên: Congacon
print(str_test.casefold())
print(str_test.lower())
print(str_test.upper())
print(str_test.casefold() == str_test.lower())