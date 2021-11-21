result = True
another_result = result
print(id(result))
print(id(another_result))

str = "Hello"
result = False
print(id(result))
print(id(str))
str += " A" # sẽ thay đổi ID.
print(id(str))