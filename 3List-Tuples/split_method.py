panagram = """The qick brown
fox jump\tover
the lazy dog"""

print(panagram.split())

numbers = "9,234,853,234,234,234,123"

print(numbers.split(","))

generated_list = ['9', ' ',
                  '2', '3', '4', ' ',
                  '8', '5', '3', ' ',
                  '2', '3', '4', ' ']

print("".join(generated_list))        
value_list = "".join(generated_list).split()
print(value_list)

for index in range(len(value_list)):
    value_list[index] = int(value_list[index])

print(value_list)

integer_list = []
for item in value_list:
    integer_list.append(int(item))

print(integer_list)

