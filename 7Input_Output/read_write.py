from asyncore import write
from os import getcwd


with open(r'D:\Coding\Python\7Input_Output\dog_breeds.txt', 'r') as reader:
    dog_breads = reader.readlines()

# a: appending to a File.
with open(r'D:\Coding\Python\7Input_Output\dog_breeds_reversed.txt', 'a') as writer:
    for breed in dog_breads:
        writer.write(breed)

print("pwd:", getcwd())

# working with two files at the same time

with open(r'D:\Coding\Python\7Input_Output\dog_breeds.txt', 'r') as reader, open(r'D:\Coding\Python\7Input_Output\dog_breeds_reversed.txt', 'a') as writer:
    dog_breeds = reader.readlines()
    writer.writelines(reversed(dog_breeds))



with open(r'D:\Coding\Python\7Input_Output\dog_breeds.txt') as reader:
    line = reader.readline()
    while line != '': # The EOF char is an empty string
        print(line, end='')
        line = reader.readline()
        